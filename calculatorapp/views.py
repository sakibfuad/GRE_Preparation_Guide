from django.shortcuts import render
from .modules.stack import Stack
import sys


def index(request):
    """
    Main control function of the site.
    
    Author: Stephen Tse <***@cmu.edu>
    Version: 1.1.0
    """
    # stack for operators to be processed
    op_stack = Stack()
    # stack for operands to be processed
    operand_stack = Stack()

    # context: used to pass values to the html view; default to 0 (which is
    # just operand_stack's initial peek() value)
    context = {'display': 0}

    # Boundaries for the numbers
    UPPER = 99999999
    LOWER = -9999999

    try:
        # initialize the stacks according to the state resubmitted from
        # client side
        if 'op_stack' in request.POST:
            op_stack.parse(request.POST['op_stack'])
        # operand_stack has an initial state; overwrite it if client side
        # has stored state
        operand_stack.push(0)
        if 'operand_stack' in request.POST:
            operand_stack.parse(request.POST['operand_stack'])

        # -- main process procedure below --------------------------

        if 'digit' in request.POST:
            input = int(request.POST['digit'])
            # check if input is an integer within range [0, 9]
            eval_num(input, 0, 9)

            if operand_stack.size() == 1:
                if op_stack.is_empty():
                    # the operand stack contains an unfinished first operand;
                    # add the input digit to it
                    num_collector = operand_stack.pop()
                    num_collector = num_collector * 10 + input
                    # check if num_collector is out of bound
                    eval_num(num_collector, LOWER, UPPER)
                    operand_stack.push(num_collector)

                elif op_stack.size() == 1:
                    if op_stack.peek() == '=':
                        # user just finished an equation; this is the first
                        # operand for a new equation
                        operand_stack.pop()  # pop the old result out
                        # ...and the "=" sign which has served its purpose
                        op_stack.pop()
                        # ...then push the new operand in
                        operand_stack.push(input)

                    else:
                        # we need to create the second operand
                        operand_stack.push(input)

                else:
                    # something's wrong: the program didn't pop out the
                    # previous equation correctly
                    raise RuntimeError("Program didn't pop out the previous "
                                       "equation correctly")

            elif operand_stack.size() == 2:
                if (op_stack.size() == 1) and (op_stack.peek() != "="):
                    # the 2nd operand is already created; add the input digit
                    # to it
                    num_collector = operand_stack.pop()
                    num_collector = num_collector * 10 + input
                    # check if num_collector is out of bound
                    eval_num(num_collector, LOWER, UPPER)
                    operand_stack.push(num_collector)

                else:
                    # everything else is seriously wrong
                    raise RuntimeError("Something's wrong: error code 1")

            else:
                # the operand_stack should neither have more than 2 numbers
                # nor nothing at all
                raise RuntimeError("Something's wrong: error code 2")

        if 'op' in request.POST:
            input = request.POST['op']

            # check if input is a legit operator: (+, -, *, /, =)
            if not (input in {'+', '-', '*', '/', '='}):
                raise ValueError("Operator is not valid")

            if operand_stack.size() == 1:
                if op_stack.is_empty():
                    # user has completed entering the first operand (or just
                    # entered an operator at the very beginning; in this case
                    # assume that we have a previous input of 0, which is
                    # already inserted into operand_stack by default); push
                    # the operator to the stack (if it's "=", then the
                    # calculation is already completed).
                    op_stack.push(input)

                elif op_stack.size() == 1:
                    if op_stack.peek() == "=":
                        # user just finished calculating an equation; just pop
                        # the old "=" sign and start the new equation with the
                        # previous result as the first operand
                        op_stack.pop()
                        op_stack.push(input)

                    else:
                        if input == "=":
                            # user entered something like "2*=";
                            # it will be treated as "2*2="
                            operand = operand_stack.pop()
                            op = op_stack.pop()
                            result = cal(operand, op, operand, LOWER, UPPER)

                            # finally, push the result to the stack
                            op_stack.push(input)
                            # add an "=" to stack to represent the completion
                            # of an equation
                            operand_stack.push(result)

                        else:
                            # user entered operators in an equation
                            # consecutively, such as "2*+"; in this case,
                            # just discard the previous operator
                            op_stack.pop()
                            op_stack.push(input)

                else:
                    # the operator stack shouldn't have more than 2 operators
                    raise RuntimeError("op_stack has more than 2 items")

            elif operand_stack.size() == 2:
                if op_stack.size() == 1:
                    # we already have two operands and an operator, ergo, we
                    # have an equation! solve it before starting a new one
                    operand_2 = operand_stack.pop()
                    operand_1 = operand_stack.pop()
                    op = op_stack.pop()
                    result = cal(operand_1, op, operand_2, LOWER, UPPER)

                    # finally, push the result to the stack
                    op_stack.push(input)
                    # add an "=" to stack to represent the completion of
                    # an equation
                    operand_stack.push(result)

                else:
                    # everything else is seriously wrong
                    raise RuntimeError("Something's wrong: error code 3")

            else:
                # everything else is seriously wrong
                raise RuntimeError("Something's wrong: error code 4")

        # finally, update calculator screen
        context['display'] = operand_stack.peek()
        context['operand_stack'] = str(operand_stack)
        context['op_stack'] = str(op_stack)

    except:
        # all errors will display an "ERROR" message on screen and also
        # reset all states temporarily stored on the client side
        context['display'] = ""
        context['operand_stack'] = ""
        context['op_stack'] = ""
        # print out the exact error message in terminal for debugging
        print(sys.exc_info())

    return render(request, 'calculatorapp/index.html', context)


def cal(x, op, y, lo, hi):
    """
    A simple calculation function.

    Arguments:
    x, y: operands (assumed to be of number type)
    op: operator
    lo, hi: lower / upper bounds (inclusive)
    """
    if op == '+':
        result = x + y
    elif op == '-':
        result = x - y
    elif op == '*':
        result = x * y
    elif op == '/':
        result = x // y
    else:
        raise ValueError("Operator not recognized")

    if (result < lo) or (result > hi):
        raise RuntimeError("Calculation out of bound")

    return result


def eval_num(x, lo, hi):
    """
    Raise errors if x does not meet the expectation.

    Arguments:
    x: the value to be evaluated
    lo, hi: lower / upper bounds (inclusive)
    """
    if not isinstance(x, int):
        raise TypeError("x must be an integer, but instead %d" % x)

    if (x < lo) or (x > hi):
        raise ValueError("x must be within this range: [%d, %d], but "
                         "instead %d" % (lo, hi, x))

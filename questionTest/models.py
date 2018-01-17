# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Comparison(models.Model):
    question = models.TextField()
    difficulty_level = models.CharField(max_length=20)
    column_a = models.CharField(db_column='column_A', max_length=500, blank=True, null=True)  # Field name made lowercase.
    column_b = models.CharField(db_column='column_B', max_length=500, blank=True, null=True)  # Field name made lowercase.
    option_right1 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comparison'


class Comprehension(models.Model):
    passage = models.TextField()
    question = models.TextField()
    difficulty_level = models.CharField(max_length=20)
    option_1 = models.CharField(max_length=100, blank=True, null=True)
    option_2 = models.CharField(max_length=100, blank=True, null=True)
    option_3 = models.CharField(max_length=100, blank=True, null=True)
    option_4 = models.CharField(max_length=100, blank=True, null=True)
    option_5 = models.CharField(max_length=100, blank=True, null=True)
    option_right1 = models.CharField(max_length=100, blank=True, null=True)
    option_right2 = models.CharField(max_length=100, blank=True, null=True)
    option_right3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comprehension'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FillBlanks(models.Model):
    question = models.TextField()
    difficulty_level = models.CharField(max_length=20, blank=True, null=True)
    option_1 = models.CharField(max_length=100, blank=True, null=True)
    option_2 = models.CharField(max_length=100, blank=True, null=True)
    option_3 = models.CharField(max_length=100, blank=True, null=True)
    option_right1 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fill_Blanks'


class MultipleMath(models.Model):
    question = models.TextField()
    difficulty_level = models.CharField(max_length=20)
    option_1 = models.CharField(max_length=100, blank=True, null=True)
    option_2 = models.CharField(max_length=100, blank=True, null=True)
    option_3 = models.CharField(max_length=100, blank=True, null=True)
    option_4 = models.CharField(max_length=100, blank=True, null=True)
    option_5 = models.CharField(max_length=100, blank=True, null=True)
    option_6 = models.CharField(max_length=100, blank=True, null=True)
    option_right1 = models.CharField(max_length=100, blank=True, null=True)
    option_right2 = models.CharField(max_length=100, blank=True, null=True)
    option_right3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'multiple_math'


class NumericEntry(models.Model):
    question = models.TextField()
    difficulty_level = models.CharField(max_length=20)
    option_right_int = models.CharField(max_length=100, blank=True, null=True)
    option_right_frac = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'numeric_entry'


class SentenceEquivalence(models.Model):
    question = models.TextField()
    difficulty_level = models.CharField(max_length=20)
    option_1 = models.CharField(max_length=100, blank=True, null=True)
    option_2 = models.CharField(max_length=100, blank=True, null=True)
    option_3 = models.CharField(max_length=100, blank=True, null=True)
    option_4 = models.CharField(max_length=100, blank=True, null=True)
    option_5 = models.CharField(max_length=100, blank=True, null=True)
    option_6 = models.CharField(max_length=100, blank=True, null=True)
    option_right1 = models.CharField(max_length=100, blank=True, null=True)
    option_right2 = models.CharField(max_length=100, blank=True, null=True)
    option_right3 = models.CharField(max_length=100, blank=True, null=True)
    option_right4 = models.CharField(max_length=100, blank=True, null=True)
    option_right5 = models.CharField(max_length=100, blank=True, null=True)
    option_right6 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sentence_equivalence'

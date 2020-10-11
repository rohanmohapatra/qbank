"""Declare models for YOUR_APP app."""

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

class Syllabus(models.Model):
    syllabus = models.CharField(max_length=10)
    classes = models.CharField(max_length=10)
    def __str__(self):
        return self.syllabus + str(self.classes)

class Subject(models.Model):
    syllabus = models.ForeignKey(Syllabus, related_name='subjects', on_delete=models.CASCADE)
    subject1 = models.CharField(max_length=25, blank = True)
    subject2 = models.CharField(max_length=25, blank = True)
    subject3 = models.CharField(max_length=25, blank = True)
    subject4 = models.CharField(max_length=25, blank = True)
    subject5 = models.CharField(max_length=25, blank = True)
    subject6 = models.CharField(max_length=25, blank = True)

    def __str__(self):
        return str(self.subject1) + str(' subjects')

class StudentDetail(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    student_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    syllabus = models.CharField(max_length=10)
    Class = models.CharField(max_length=10)
    sub1 = models.CharField(max_length=20, blank = True)
    sub2 = models.CharField(max_length=20, blank = True)
    sub3 = models.CharField(max_length=20, blank = True)
    sub4 = models.CharField(max_length=20, blank = True)
    sub5 = models.CharField(max_length=20, blank = True)
    sub6 = models.CharField(max_length=20, blank = True)

    def __str__(self):
        return self.student_name

class leftWhere(models.Model):
    user = models.IntegerField(primary_key=True)
    Subject = models.CharField(max_length=50, blank=True)
    Year = models.IntegerField(blank=True)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to ='media', blank = True)

class ImageScience(models.Model):
    qid = models.ForeignKey('Science', models.DO_NOTHING, db_column='qid')
    image = models.ImageField(upload_to ='imagesScience', blank = True)

class ImageCommerce(models.Model):
    qid = models.ForeignKey('Commerce', models.DO_NOTHING, db_column='qid')
    image = models.ImageField(upload_to ='imagesCommerce', blank = True)

class ImageClass10(models.Model):
    qid = models.ForeignKey('Class10', models.DO_NOTHING, db_column='qid')
    image = models.ImageField(upload_to ='imagesClass10', blank = True)

class Class10Answer(models.Model):
    qid = models.ForeignKey('Class10', models.DO_NOTHING)
    subject = models.CharField(max_length=100, blank=True, null=True)
    answer = models.TextField(max_length=10000, blank=True)
    image1 = models.ImageField(upload_to = 'class10Answer', blank=True)
    image2 = models.ImageField(upload_to='class10Answer', blank=True)

class ScienceAnswer(models.Model):
    qid = models.ForeignKey('Science', models.DO_NOTHING)
    subject = models.CharField(max_length=100, blank=True, null=True)
    answer = models.TextField(max_length=10000, blank=True)
    image1 = models.ImageField(upload_to = 'Science12Answer', blank=True)
    image2 = models.ImageField(upload_to='ScienceAnswer', blank=True)

class CommerceAnswer(models.Model):
    qid = models.ForeignKey('Commerce', models.DO_NOTHING)
    subject = models.CharField(max_length=100, blank=True, null=True)
    answer = models.TextField(max_length=10000, blank=True)
    image1 = models.ImageField(upload_to = 'CommerceAnswer', blank=True)
    image2 = models.ImageField(upload_to='CommerceAnswer', blank=True)

class BookmarkQuest(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    qid = models.IntegerField(blank = True)
    year = models.CharField(blank = True, max_length= 10)
    subject = models.CharField(blank=True, max_length=20)

class SolvedQuest(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    qid = models.IntegerField(blank = True)
    yearsub = models.CharField(blank = True, max_length=40)

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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


class Class10(models.Model):
    qid = models.IntegerField(primary_key=True)
    qclass = models.IntegerField()
    qno = models.IntegerField()
    subject = models.CharField(max_length=100, blank=True, null=True)
    topic = models.CharField(max_length=500, blank=True, null=True)
    question = models.CharField(max_length=5000, blank=True, null=True)
    image1 = models.ImageField(upload_to ='question', blank = True)
    image2 = models.ImageField(upload_to ='question', blank = True)


    class Meta:
        managed = False
        db_table = 'class10'

    def __str__(self):
        return str(self.subject + str(self.qid))


class Commerce(models.Model):
    qid = models.IntegerField(primary_key=True)
    qclass = models.IntegerField()
    qno = models.IntegerField()
    subject = models.CharField(max_length=100, blank=True, null=True)
    topic = models.CharField(max_length=500, blank=True, null=True)
    question = models.CharField(max_length=5000, blank=True, null=True)
    image1 =  models.ImageField(upload_to ='question', blank = True)
    image2 =  models.ImageField(upload_to ='question', blank = True)

    class Meta:
        managed = False
        db_table = 'commerce'

    def __str__(self):
        return str(self.subject + str(self.qid))



class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('StudentsUser', models.DO_NOTHING)

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


class KnoxAuthtoken(models.Model):
    digest = models.CharField(primary_key=True, max_length=128)
    salt = models.CharField(unique=True, max_length=16)
    created = models.DateTimeField()
    user = models.ForeignKey('StudentsUser', models.DO_NOTHING)
    expiry = models.DateTimeField(blank=True, null=True)
    token_key = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'knox_authtoken'


class Science(models.Model):
    qid = models.IntegerField(primary_key=True)
    qclass = models.IntegerField()
    qno = models.IntegerField()
    subject = models.CharField(max_length=100, blank=True, null=True)
    topic = models.CharField(max_length=500, blank=True, null=True)
    question = models.CharField(max_length=5000, blank=True, null=True)
    image1 = models.ImageField(upload_to ='question', blank = True)
    image2 = models.ImageField(upload_to ='question', blank = True)


    class Meta:
        managed = False
        db_table = 'science'

    def __str__(self):
        return str(self.subject + str(self.qid))



class StudentsSubject(models.Model):
    subject1 = models.CharField(max_length=25)
    subject2 = models.CharField(max_length=25)
    subject3 = models.CharField(max_length=25)
    subject4 = models.CharField(max_length=25)
    subject5 = models.CharField(max_length=25)
    subject6 = models.CharField(max_length=25)
    syllabus_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'students_subject'


class StudentsSyllabus(models.Model):
    syllabus = models.CharField(max_length=10)
    classes = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'students_syllabus'


class StudentsUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    email = models.CharField(unique=True, max_length=254)

    class Meta:
        managed = False
        db_table = 'students_user'


class StudentsUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'students_user_groups'


class StudentsUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'students_user_user_permissions'


class YearClass10(models.Model):
    qid = models.ForeignKey(Class10, related_name='year', primary_key=True, db_column='qid', on_delete=models.DO_NOTHING, )
    years = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'year_class10'
    def __str__(self):
        return str(self.years)


class YearCommerce(models.Model):
    qid = models.ForeignKey(Commerce, related_name='year', primary_key=True, on_delete=models.DO_NOTHING, db_column='qid')
    years = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'year_commerce'

    def __str__(self):
        return str(self.years)


class YearScience(models.Model):
    qid = models.ForeignKey(Science, related_name='year', primary_key=True, on_delete=models.DO_NOTHING, db_column='qid')
    years = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'year_science'

    def __str__(self):
        return str(self.years)

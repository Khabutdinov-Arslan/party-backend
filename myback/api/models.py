from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
	def create_user(self, username, password, surname, name, patronymic, department, course, **extra_fields):
		if not username:
			raise ValueError('No login')
		user = self.model(username=username, surname=surname, name=name, patronymic=patronymic, department=department, course=course, **extra_fields)
		user.set_password(password)
		user.save()
		return user


	def create_superuser(self, username, password, surname="Adminov", name="Admin", patronymic="Adminovich", department="PSAMI", course="admin", **extra_fields):
		if not username:
			raise ValueError('No login')

		extra_fields.setdefault('staff', True)
		extra_fields.setdefault('admin', True)
		extra_fields.setdefault('active', True)

		return self.create_user(username, password, surname, name, patronymic, department, course, **extra_fields)



class User(AbstractBaseUser):
	username = models.CharField(max_length=20, unique=True)
	surname = models.CharField(max_length=20)
	name = models.CharField(max_length=20)
	patronymic = models.CharField(max_length=20)
	department = models.CharField(max_length=10)
	course = models.CharField(max_length=10)

	active = models.BooleanField(default=True)
	staff = models.BooleanField(default=False) 
	admin = models.BooleanField(default=False) 

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []

	def get_full_name(self):
		return self.surname + ' ' + self.name + ' ' + self.patronymic

	def get_short_name(self):
		return self.username

	def __str__(self):
		return self.username

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		return self.staff

	@property
	def is_admin(self):
		"Is the user a admin member?"
		return self.admin
	
	@property
	def is_active(self):
		"Is the user active?"
		return self.active

	objects = UserManager()


class Event(models.Model):
	author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
	name = models.CharField(max_length=20, unique=True)
	place = models.CharField(max_length=20)
	time = models.DateTimeField()
	people = models.IntegerField()
	chat = models.CharField(max_length=100)
	description = models.CharField(max_length=1000)

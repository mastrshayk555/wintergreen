from django.db import models
from localflavor.us.models import USStateField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError('Superusers must have an email address')
        
        superuser = self.model(
            email=self.normalize_email(email),
        )

        superuser.is_admin = True
        superuser.set_password(password)
        superuser.save(using=self._db)

        return superuser


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    phone = PhoneNumberField(null=True, blank=True)
    email = models.CharField(max_length=200, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserAccountManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email
    
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
        return self.is_admin
    

class UserAddress(models.Model):
    class Meta:
        verbose_name = "user address"
        verbose_name_plural = "user address"

    ADDRESS_TYPE_CHOICES = {
        'home': 'Home',
        'billing': 'Billing',
    }

    address_type = models.CharField(
        max_length=20, 
        choices=ADDRESS_TYPE_CHOICES
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_one = models.CharField(max_length=300, null=True)
    address_two = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=200, null=True)
    state = USStateField(null=True)
    zipcode = models.IntegerField(null=True)

    
    def __str__(self):
        return f'{self.user}'
    
class UserProfile(models.Model):
    class Meta:
        verbose_name = "user profile"

    MARITAL_STATUS_CHOICES = {
        'single': 'Single',
        'married': 'Married',
        'widowed': 'Widowed',
        'divorced': 'Divorced',
        'other': 'Other',
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    industry = models.CharField(max_length=100, null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    marital_status = models.CharField(
        max_length=50, 
        choices=MARITAL_STATUS_CHOICES, 
        null=True,
        blank=True,
    )
    number_of_children = models.IntegerField(null=True, blank=True)
    life_goals = models.TextField(null=True, blank=True)
    financial_goals = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user}"
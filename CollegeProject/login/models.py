from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator

class User(models.Model):
    username = models.CharField(max_length=50,null=False,blank=False,primary_key=True)
    password = models.CharField(
                max_length=20,unique=True,
                validators=[MinLengthValidator(6),
                            RegexValidator(
                                regex=r'^[A-Za-z0-9@#$%^&+=!]*$',
                                message="Password can contain letters, numbers and special characters"
                )],null=False,blank=False)
    phone_number = models.CharField(
                max_length=10,unique=True,
                validators=[RegexValidator(
                                regex=r'^[0-9]{10}$',
                                message="Phone number must be exactly 10 digits"
                )])
    pincode = models.CharField(
                max_length=6,
                validators=[
                            RegexValidator(
                                regex=r'^[0-9]{6}$',
                                message="Pincode must be exactly 6 digits"
                )])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.username


class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=150,primary_key=True)
    password = models.CharField(
                max_length=20,unique=True,
                validators=[MinLengthValidator(6),
                            RegexValidator(
                                regex=r'^[A-Za-z0-9@#$%^&+=!]*$',
                                message="Password can contain letters, numbers and special characters"
                )],null=False,blank=False)
    phone_number = models.CharField(
                max_length=10,unique=True,
                validators=[RegexValidator(
                                regex=r'^[0-9]{10}$',
                                message="Phone number must be exactly 10 digits"
                )])
    address = models.TextField()
    pincode = models.CharField(default="000000",
                max_length=6,
                validators=[
                            RegexValidator(
                                regex=r'^[0-9]{6}$',
                                message="Pincode must be exactly 6 digits"
                )])
    total_gathering = models.PositiveIntegerField()
    specification = models.CharField(max_length=100)
    description = models.TextField()
    photo1 = models.ImageField(upload_to='restaurant_photos/')
    photo2 = models.ImageField(upload_to='restaurant_photos/', blank=True, null=True)
    photo3 = models.ImageField(upload_to='restaurant_photos/', blank=True, null=True)
    photo4 = models.ImageField(upload_to='restaurant_photos/', blank=True, null=True)
    photo5 = models.ImageField(upload_to='restaurant_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.restaurant_name
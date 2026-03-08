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
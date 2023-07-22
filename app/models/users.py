from django.db import models

class Users(models.Model):
    UserID = models.AutoField(primary_key=True)
    RoleID = models.ForeignKey('Role', on_delete=models.CASCADE)
    UserName = models.CharField(max_length=100)
    PasswordHash = models.CharField(max_length=128)
    FullName = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    PhoneNumber = models.CharField(max_length=20)

    def __str__(self):
        return self.UserName

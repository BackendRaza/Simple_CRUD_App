from django.db import models
from django.db.models.fields import BigIntegerField

class student(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = BigIntegerField()

    def __str__(self) -> str:
        return "{} | {} | {} | {}" .format(self.FirstName, self.LastName, self.Email, self.Contact)

class Userr(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.EmailField(max_length=50)
    Password = models.CharField(max_length=20)
    ProfilePic = models.ImageField(blank=True, upload_to='static/')

    @property
    def imageURL(self):
        try:
            url = self.ProfilePic.url
        except:
            url=''
        return url

    def __str__(self) -> str:
        return "{} | {} | {} | {}" .format(self.FirstName, self.LastName, self.Email, self.Contact)

class Posts(models.Model):
    pheading = models.CharField(max_length=150)
    pimg = models.ImageField(blank=True, upload_to='posts/')
    ptext = models.CharField(max_length=500)
    userid = models.ForeignKey(Userr, on_delete=models.CASCADE)
    pdate = models.DateTimeField()

    @property
    def imageURL(self):
        try:
            url = self.pimg.url
        except:
            url=''
        return url

    def __str__(self) -> str:
        return super().__str__()
from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Title(models.Model):
    title = models.CharField(max_length=123)
    text = models.CharField(max_length=123)
    rasm = models.ImageField(upload_to='title/')


    def __str__(self):
        return self.title
class Service(models.Model):
    title = models.CharField(max_length=123)
    text = models.CharField(max_length=123)
class Service2(models.Model):
    
    title = models.CharField(max_length=123)
    text = models.CharField(max_length=123)
    text1 = models.CharField(max_length=123)
    text2 = models.CharField(max_length=123)
    text3 = models.CharField(max_length=123)
    rasm  = models.ImageField(upload_to = 'Service/')
class Service3(models.Model):
    rasm = models.ImageField(upload_to = 'Servise3/')
    title = models.CharField(max_length=1223)
    text = models.CharField(max_length=1232)
    text2 = models.CharField(max_length=1232)
class Features(models.Model):
    title = models.CharField(max_length=123)
    text = models.CharField(max_length=123)

    title1 = models.CharField(max_length=123)
    text1 = models.CharField(max_length=123)

    title2 = models.CharField(max_length=123)
    text2= models.CharField(max_length=123)

    title3 = models.CharField(max_length=123)
    text3= models.CharField(max_length=123)

    title4 = models.CharField(max_length=123)
    text4 = models.CharField(max_length=123)

    title5 = models.CharField(max_length=123)
    text5 = models.CharField(max_length=123)

    title6 = models.CharField(max_length=123)
    text6 = models.CharField(max_length=123)
class Features1(models.Model):
    title = models.CharField(max_length=1234)
    rasm = models.ImageField(upload_to = 'Features1/')
    titles=models.CharField(max_length=123)
    text = models.CharField(max_length=123)

    title1 = models.CharField(max_length=1234)
    rasm1 = models.ImageField(upload_to = 'Features1/')
    title1s=models.CharField(max_length=123)
    text1 = models.CharField(max_length=123)

    title2 = models.CharField(max_length=1234)
    rasm2 = models.ImageField(upload_to = 'Features1/')
    title2s=models.CharField(max_length=123)
    text2 = models.CharField(max_length=123)

class Narxlar(models.Model):
    title = models.CharField(max_length=121)
    text = models.CharField(max_length=1234)
class Narxlar2(models.Model):
    title = models.CharField(max_length=123)
    rasm = models.ImageField(upload_to= 'Narxlar2/')
    text = models.TextField()

    title1 = models.CharField(max_length=123)
    rasm1 = models.ImageField(upload_to= 'Narxlar2/')
    text1 = models.TextField()

    title2 = models.CharField(max_length=123)
    rasm2 = models.ImageField(upload_to= 'Narxlar2/')
    text2 = models.TextField()

class Narxlar33(models.Model):
    title = models.CharField(max_length=123)
    rasm1 = models.ImageField(upload_to='Narxlar4/')
    rasm2 = models.ImageField(upload_to='Narxlar4/')
    rasm3 = models.ImageField(upload_to='Narxlar4/')
    rasm4 = models.ImageField(upload_to='Narxlar4/')
    rasm5 = models.ImageField(upload_to='Narxlar4/')
    rasm6 = models.ImageField(upload_to='Narxlar4/')
    rasm7 = models.ImageField(upload_to='Narxlar4/')
    rasm8 = models.ImageField(upload_to='Narxlar4/')

class YouTubeVideo(models.Model):
    rasm = models.ImageField(upload_to='YoutubeVideo')
    video = models.CharField(max_length=234)

class Team(models.Model):
    title = models.CharField(max_length=234)
    text = models.CharField(max_length=234)

class Jamoa(models.Model):
    rasm = models.ImageField(upload_to='Jamoarasm/')
    ism = models.CharField(max_length=234)
    soha = models.CharField(max_length=234)

    rasm1 = models.ImageField(upload_to='Jamoarasm/')
    ism1 = models.CharField(max_length=234)
    soha1 = models.CharField(max_length=234)

    rasm2 = models.ImageField(upload_to='Jamoarasm/')
    ism2 = models.CharField(max_length=234)
    soha2 = models.CharField(max_length=234)
 
class Contact(models.Model):
    title = models.CharField(max_length=234)
    text = models.TextField()

class Contact1(models.Model):
    name = models.CharField(max_length=123)
    email = models.EmailField()
    phone = models.CharField(max_length=123)
    subject = models.CharField(max_length=123)
    message = models.TextField()
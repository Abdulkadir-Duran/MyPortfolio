from django.db import models

# Create your models here.
class Home(models.Model):

    img = models.ImageField()
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    text = models.TextField(max_length=500)
    def __str__(self):
        return self.name

class About(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    titlespan = models.CharField(max_length=250)
    text = models.TextField(max_length=1500)
    def __str__(self):
        return self.name


class ProjectsML(models.Model):
    title = models.CharField(max_length=200)
    btn = models.CharField(max_length=200)
    img = models.ImageField()
    projectNo = models.IntegerField()
    def __str__(self):
        return self.title


class ProjectsWeb(models.Model):
    title = models.CharField(max_length=200)
    btn = models.CharField(max_length=200)
    img = models.ImageField()
    projectNo = models.IntegerField()
    def __str__(self):
        return self.title


class Projects(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
    img = models.ImageField()
    detailbtn = models.CharField(max_length=200)
    backbBtn = models.CharField(max_length=200)
    projectID = models.IntegerField()
    projectLink = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    

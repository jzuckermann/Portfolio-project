from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    question1 = models.TextField(max_length=350)#Please tell us what type of even you are wanting captured?
    question2 = models.TextField(max_length=350)#What first attracted you to my work & what would you like to see in your own photographs?
    question3 = models.TextField(max_length=350)
    question4 = models.TextField(max_length=350)

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    mail = models.EmailField(null=True)
    phone = models.CharField(max_length=32,null=True)

    def __str__(self):
        return self.name

class Questionnaire(models.Model):
    type = models.IntegerField(default=0,null=True)

    publishTime = models.DateTimeField(null=True)
    endTime = models.DateTimeField(null=True)
    answerTime = models.TimeField(null=True)

    isClose = models.BooleanField(default=False,null=True)
    isDeleted = models.BooleanField(default=False,null=True)
    isPublished = models.BooleanField(default=False,null=True)

    recoverNum = models.IntegerField(default=0,null=True)
    limitNum = models.IntegerField(null=True)

    title = models.CharField(max_length=64,null=True)
    FQID = models.CharField(max_length=64,null=True)

class Question(models.Model):
    content = models.TextField()

    quesNum = models.IntegerField(null=True)
    participantsNum = models.IntegerField(default=0)
    limitNum = models.IntegerField(null=True)

    class Meta:
        abstract = True

class Complition(Question):
    CMPID = models.CharField(max_length=64,unique=True)
    NQID = models.CharField(max_length=64)

class ChoiceQuestion(Question):
    CHID = models.CharField(max_length=64,unique=True)
    NQID = models.CharField(max_length=64)
    FOID = models.IntegerField(null=True)
    isMulti = models.BooleanField(default=False,null=True)

class Option(models.Model):
    NOID = models.IntegerField(null=True)

    content = models.TextField()

    selectedNum = models.IntegerField(default=0,null=True)
    score = models.IntegerField(null=True)
    limitNum = models.ImageField(null=True)

    isCorrect = models.BooleanField(null=True)

class Answer(models.Model):
    content = models.TextField()

    NAID = models.IntegerField()


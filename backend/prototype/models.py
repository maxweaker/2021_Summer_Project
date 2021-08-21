from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Questionnaire(models.Model):
    type = models.IntegerField(default=0)

    publishTime = models.DateTimeField()
    endTime = models.DateTimeField(null=True)
    answerTime = models.TimeField(null=True)

    isClose = models.BooleanField(default=False,null=True)
    isDeleted = models.BooleanField(default=False,null=True)

    recoverNum = models.IntegerField(default=0,null=True)
    limitNum = models.IntegerField(null=True)

    FQID = models.CharField(max_length=64,null=True)

class Question(models.Model):
    content = models.TextField()

    quesNum = models.IntegerField()
    participantsNum = models.IntegerField()
    limitNum = models.IntegerField()

    class Meta:
        abstract = True

class Complition(Question):
    CMPID = models.CharField(max_length=64,primary_key=True)
    NQID = models.CharField(max_length=64)

class ChoiceQuestion(Question):
    CHID = models.CharField(max_length=64,primary_key=True)
    NQID = models.CharField(max_length=64)

class Option(models.Model):
    OID = models.CharField(max_length=64,primary_key=True)
    NOID = models.CharField(max_length=64)

    content = models.TextField()

    selectedNum = models.IntegerField(default=0,null=True)
    score = models.IntegerField()
    limitNum = models.ImageField()

    isCorrect = models.BooleanField()

class Answer(models.Model):
    content = models.TextField()

    NAID = models.IntegerField()


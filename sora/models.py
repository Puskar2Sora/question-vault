from django.db import models

class questions(models.Model):
    question = models.TextField()
    frequency = models.IntegerField()
    years = models.IntegerField()     
    marks = models.IntegerField()

    university = models.CharField(max_length=60)
    course = models.CharField(max_length=60)
    department = models.CharField(max_length=60)
    semester = models.SmallIntegerField()
    subject = models.CharField(max_length=60)
    topic = models.CharField(max_length=60)

    class Meta:
        db_table = "sora_questions"

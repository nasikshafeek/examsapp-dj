"""
DB related model imports
"""
from django.db import models


class Exam(models.Model):
    """
    Exam Model
    """
    title = models.CharField(max_length=200)
    exam_duration = models.DurationField(null=True)
    published_status = models.BooleanField(default=False)
    pub_date = models.DateTimeField('published date')

    def __str__(self):
        return self.title


class Question(models.Model):
    """
    Question Model
      - Relates to the Exam model in one-to-many relationship
    """
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text = models.TextField()
    question_type = models.CharField(max_length=50, default='') 

    def __str__(self):
        return self.question_text


class Answers(models.Model):
    """
    Answers Model
     - Relates to the Question Model with one to many relationship
    """
    IMAGE_ANS = 'IM'
    TEXT_ANS = 'TX'
    ANSWER_TYPES = [
        (IMAGE_ANS, 'Image'),
        (TEXT_ANS, 'Text'),
    ]
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True)
    answer_image = models.ImageField(blank=True)
    answer_type = models.CharField(max_length=2, choices=ANSWER_TYPES, default=TEXT_ANS)


class CorrectAnswer(models.Model):
    """
    Pivot table which contains Question id and Answer id for correct answers
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE)
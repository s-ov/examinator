from django.db import models
from examinator.models.test_paper import TestPaper


class Question(models.Model):
    """Class representing a question instance."""
    
    ordinal_number = models.IntegerField('ordinal number')
    question_text = models.TextField('question text')
    paper_test = models.ForeignKey(
        TestPaper, 
        on_delete=models.CASCADE, 
        related_name='questions',
        blank=True, 
        null=True,
        )

    def save(self, *args, **kwargs):
        """Automatically set or increment ordinal number."""

        if not self.pk: 
            last_question = Question.objects.filter().order_by('ordinal_number').last()
            self.ordinal_number = last_question.ordinal_number + 1 if last_question else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question_text

from django.db import models
from examinator.models.question import Question

class Answer(models.Model):
    """Class representing an answer instance."""
    
    question = models.ForeignKey(
        Question, 
        on_delete=models.CASCADE, 
        related_name='answers',
        )
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
    
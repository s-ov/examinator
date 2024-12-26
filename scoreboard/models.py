from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class ScoreBoard(models.Model):
    """Model representing a scoreboard for a user's performance on any type of test."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='scoreboards'
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        related_name='knowledge_tests'
    )
    object_id = models.PositiveIntegerField()
    knowledge_test = GenericForeignKey('content_type', 'object_id')
    answers = models.JSONField(
        default=dict,
        help_text="Stores the user's answers. Example: {'1': 'A', '2': 'B', '3': 'C'}"
    )
    correct_answers = models.IntegerField(default=0)
    wrong_answers = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.knowledge_test}\
                 (Correct: {self.correct_answers_count},\
                  Wrong: {self.wrong_answers_count})"

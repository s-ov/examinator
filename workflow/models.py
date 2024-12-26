from django.db import models

from examinator.models.knowledge_test import KnowledgeTest
from examinator.models.test_paper import TestPaper
from examinator.models.question import Question
from examinator.models.answer import Answer
from scoreboard.models import ScoreBoard


class Workflow(models.Model):
    knowledge_test = models.ForeignKey(KnowledgeTest, on_delete=models.CASCADE)
    test_papers = models.ManyToManyField(TestPaper, blank=True)
    questions = models.ManyToManyField(Question, blank=True)
    answers = models.ManyToManyField(Answer, blank=True)
    scoreboards = models.ManyToManyField(ScoreBoard, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.knowledge_test

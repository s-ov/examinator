from django.db import models
from examinator.models.knowledge_test import KnowledgeTest


class TestPaper(models.Model):
    """Class representing a question instance."""
    ordinal_number = models.IntegerField()
    slug = models.SlugField(max_length=255, unique=True)
    knowledge_test = models.ForeignKey(
        'examinator.KnowledgeTest', 
        on_delete=models.CASCADE, 
        related_name='test_papers',
        blank=True, 
        null=True,
    )       

    def __str__(self):
        return f'Білет N{self.ordinal_number}.'
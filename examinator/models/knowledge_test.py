from django.db import models


class KnowledgeTest(models.Model):
    """Class representing a question instance."""
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title
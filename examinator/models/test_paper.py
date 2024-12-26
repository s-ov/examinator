from django.db import models
from django.urls import reverse

from examinator.models.question import Question


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

    def save(self, *args, **kwargs):
        if self.ordinal_number is None:
            max_number = TestPaper.objects.aggregate(
                models.Max('ordinal_number')
            )['ordinal_number__max']
            self.ordinal_number = 1 if max_number is None else max_number + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Білет N{self.ordinal_number}.'
    
    def get_absolute_url(self):
        return reverse(
            'examinator:testpaper_detail', 
            kwargs={'slug': self.slug},
        )

from django.db import models
from django.utils.text import slugify
import uuid

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    slug = models.SlugField(max_length=120, null=True,blank=True, unique=True)
    
    class Meta:
        ordering = ['completed']
        db_table = 'todos'
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.description)
        super().save(*args, **kwargs)

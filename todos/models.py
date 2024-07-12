from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    slug = models.SlugField(unique=True,blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo_detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Todo, self).save(*args, **kwargs)

    class Meta:
        ordering = ['completed']
        db_table = 'todos'

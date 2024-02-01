from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, default='')
    time_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_of_creation']
        indexes = [
            models.Index(fields=['-time_of_creation'])
        ]

    def get_absolute_url_for_more_info(self):
        return reverse('notes:info', kwargs={'slug': self.slug})

    def get_absolute_url_for_delete(self):
        return reverse('notes:delete', kwargs={'slug': self.slug})

    def get_absolute_url_for_edit(self):
        return reverse('notes:edit', kwargs={'slug': self.slug})


    # class Author(models.Model):
    #     name = models.CharField(max_length=50)
    #     password = models.CharField(max_length=10)
    #
    #     def __str__(self):
    #         return self.name
    #

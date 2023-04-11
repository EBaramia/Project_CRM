from django.db import models
from django.contrib.auth.models import User
from team.models import Team


class Client(models.Model):
    class Meta:
        ordering = ('name',)

    team = models.ForeignKey(
        Team, related_name='clients', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, related_name='client', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    team = models.ForeignKey(Team, related_name='client_comments',
                             on_delete=models.CASCADE)
    client = models.ForeignKey(
        Client, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, related_name='client_comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created_by.username

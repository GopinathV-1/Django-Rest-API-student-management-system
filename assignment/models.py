from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


class Assignment(models.Model):
    SUBJECT_CHOICES = (
        ('English', 'English'),
        ('Tamil', 'Tamil'),
        ('Maths', 'Maths'),
        ('Physics', 'Physics'),
        ('Chemistry', 'Chemistry'),
        ('Biology', 'Biology'),
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    staff = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    due_date = models.DateField()
    subject = models.CharField(max_length=10, choices=SUBJECT_CHOICES)

    def __str__(self):
        return self.title


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

from django.db import models
from django.utils import timezone


class BasicModel(models.Model):
    create_user = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    update_user = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_user = models.IntegerField(null=True, blank=True)
    is_del = models.BooleanField(default=False)

    class Meta:
        abstract = True

from django.db import models
import uuid
from model_utils.models import TimeStampedModel


class CommonInfo(TimeStampedModel):
    id = models.UUIDField(primary_key=True,db_index=True, default=uuid.uuid4, editable=False, serialize=True)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)
    
    class Meta:
        abstract = True

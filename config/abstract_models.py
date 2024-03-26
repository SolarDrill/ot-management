from django.db import models
import uuid
from model_utils.models import TimeStampedModel
from django.urls import reverse

class CommonInfo(TimeStampedModel):
    id = models.UUIDField(primary_key=True,db_index=True, default=uuid.uuid4, editable=False, serialize=True)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)
    
    def get_absolute_url(self):
        """
        Returns the absolute URL for the object in the API.
        """
        # 'api:{model_name}-detail' is the assumed naming convention for detail views in your API
        return reverse(f'api:{self._meta.model_name}-detail', kwargs={'pk': self.pk})
    class Meta:
        abstract = True
    


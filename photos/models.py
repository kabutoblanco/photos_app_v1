from django.db import models

# Create your models here.
from django.db import models

from utils.models import BaseModel

class Photo(BaseModel):
    id_unsplash = models.CharField(max_length=255)
    preview = models.CharField(max_length=255)
    favorite = models.BooleanField(default=False)
from django.db import models

# Create your models here.
class RamenCorner(models.Model):
   title = models.CharField(max_length=100)
   videoUrl = models.URLField(max_length=200)

   def _str_(self):
     return self.title
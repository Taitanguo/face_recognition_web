from django.db import models

# Create your models here.
class Topic(models.Model):
    # Tell database the size of this text we need
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text
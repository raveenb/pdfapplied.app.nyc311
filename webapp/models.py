from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
import logging
logger = logging.getLogger(__name__)

class ThreeOneOneData(models.Model):
    name = models.CharField(max_length = 128)
    count = models.IntegerField()
    json_data = models.CharField(max_length = 2048, blank = True, null = True)
    
    def __unicode__(self):
        return self.name + ' - ' + str(self.count)

class CommunityName(models.Model):
	name = models.CharField(max_length = 128)

	def __unicode__(self):
		return self.name

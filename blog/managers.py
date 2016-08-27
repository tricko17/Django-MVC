from django.db import models

class PublishedManager(models.Manager):
	status = None
	def get_queryset(self):
		if not self.status:
			return super (PublishedManager,self).get_queryset()\
												.filter(status='published')
		else:
			return super (PublishedManager,self).get_queryset()\
												.filter(status=self.status)	
												
	@staticmethod
	def set_status(status):
		a = PublishedManager()
		a.status = status
		return a	
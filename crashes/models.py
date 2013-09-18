from django.db import models

# Create your models here.
class Crash(object):
	"""docstring for Crash"""
	timestamp = models.IntegerField(default=0, blank=False)
	crashInfo = models.TextField()
	def __init__(self, arg):
		super(Crash, self).__init__()
		self.arg = arg
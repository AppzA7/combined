from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tickets(models.Model):
	journey_id=models.BigIntegerField(default=1)
	PNR= models.BigIntegerField()
	train_no=models.BigIntegerField()
	date=models.DateTimeField()
	price=models.BigIntegerField()
	train_name=models.CharField(max_length=200)
	location_from=models.CharField(max_length=200)
	location_to=models.CharField(max_length=200)
	
	def __str__(self):
		return self.train_name

	def view(cls):
		m=journey_id+"#"+location_from
		return m

	

class Map(dict):
    """
    Example:
    m = Map({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])
    """
    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.iteritems():
                    self[k] = v

        if kwargs:
            for k, v in kwargs.iteritems():
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Map, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        del self.__dict__[key]
from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from django.conf import settings
from django.core.urlresolvers import reverse


# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	#image = models.ImageField(null=True, blank=True,width_field="width_field", height_field="height_field" )
	#height_field.models.IntegerField(default=0)
	#width_field = models.IntegerField(defult=0)
	body = models.TextField()
	slug = models.SlugField(unique =True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	image = models.CharField(max_length=1000, null=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
	def __str__(self):
		return self.title
	def get_absolute_url(self):	
		return reverse("detail", kwargs={'slug': self.slug})
##create a signal 
def pre_save_post_reciever(sender, instance, *args, **kwargs):
	slug = slugify(instance.title) # this makes the title into a slug
	exists = Post.objects.filter(slug=slug).exists()
	if exists:
		slug = "%s-%s" %(slug, instance.id)#this is when a slug already existss
	instance.slug = slug
pre_save.connect(pre_save_post_reciever, sender=Post)
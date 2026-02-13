from django.db import models
from django.utils import timezone
from django.urls import reverse



class Category(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name
	



class News(models.Model):

	class Status(models.TextChoices):
		DRAFT ="DR", "Draft"
		PUBLISH ="PB", "Publish"


	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200)
	body = models.TextField()
	image = models.ImageField(upload_to="news/images/")
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	publish_time = models.DateTimeField(default=timezone.now)
	created_time = models.DateTimeField(auto_now_add=True)
	uploaded_time = models.DateTimeField(auto_now=True)
	status = models.CharField(
		max_length=2,
		choices = Status.choices,
		default="DRAFT"
	)

	def __str__(self):
		return self.title
	


	def get_absolute_url(self):
		return reverse("one_new", args=[self.slug])
	




class ContactAdmin(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=150)
    message = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.name
from django.shortcuts import render, get_object_or_404, redirect
from . import models
import datetime

def info(request):

	news = models.News.objects.filter(status="PB")
	last_news = models.News.objects.order_by("created_time").filter(status="PB")[:5]
	categories = models.Category.objects.all()
	local_news = models.News.objects.filter(category__name="mahalliy")
	time = datetime.datetime.now()

	context = {
		"news": news,
		"categories": categories,
		"local_news": local_news,
		"last_news": last_news,
		"time": time,
	}
	

	return render(request, 'index.html', context=context)


def news_detail(request, news):
	new = get_object_or_404(models.News, slug=news, status="PB")
	news = models.News.objects.filter(status="PB")
	last_news = models.News.objects.order_by("created_time").filter(status="PB")[:5]
	categories = models.Category.objects.all()
	local_news = models.News.objects.filter(category__name="mahalliy")
	time = datetime.datetime.now()

	context = {
		"new": new,
		"news": news,
		"categories": categories,
		"local_news": local_news,
		"last_news": last_news,
		"time": time,
	}

	return render(request, 'single_page.html', context=context)


def contact_uc(request):
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get('email')
		message = request.POST.get("message")


		models.ContactAdmin.objects.create(
			name=name,
			email =email, 
			message = message
		)
		return redirect("contact")


	return render(request, 'contact.html' )


def about(request):
	time = datetime.datetime.now()
	context = {
		"time":time,
	}
	return render(request, 'about.html', context=context)

def error(request):
	return render(request, '404.html')


# Create your views here.

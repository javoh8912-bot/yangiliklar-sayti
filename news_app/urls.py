from django.urls import path
from . import views

urlpatterns = [
	path('', views.info, name = 'info'),
	path('news<slug:news>', views.news_detail, name='one_new'),
	path('contact/', views.contact_uc, name ='contact'),
    path('about/', views.about, name='about'),
    path('error/', views.error, name="error")

]
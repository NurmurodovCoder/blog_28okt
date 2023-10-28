from django.urls import path
from .views import index, blog, detail, about, contact


urlpatterns = [

    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),

]

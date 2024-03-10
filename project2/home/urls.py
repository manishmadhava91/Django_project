from home import views
from django.urls import path,include
urlpatterns = [
        path('home/',views.home),
        path('template/',views.index)
]
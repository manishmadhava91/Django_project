from login import views
from django.urls import path,include
urlpatterns=[
    path('login/',views.login)
]
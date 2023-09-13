from django.urls import path
from . import views

urlpatterns = [
    path('', views.PersonView.as_view(), name='users'),
    path('<int:pk>', views.PersonDetailView.as_view(), name='user'),
]
from django.urls import path
from .views import HomeViews


app_name = 'apps.web'

urlpatterns = [
    path('', HomeViews.as_view(), name='home'),
]
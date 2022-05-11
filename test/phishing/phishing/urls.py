from django.urls import path
from pages.views import *

urlpatterns = [
    path('', index_page, name='index_page'),
]

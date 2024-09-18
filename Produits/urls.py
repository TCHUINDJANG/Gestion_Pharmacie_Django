
from django.urls import path
from .views import *

urlpatterns = [

    # path('', home, name='home')
    path('',affichage.as_view(),name='home'),
]
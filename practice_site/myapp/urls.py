# this file is supposed to be created by me myself
# we need to create this file to call the view (from views.py) and map them to a URL.
# for this we need to create a URLconf

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # after this we go to practice_site/urls.py and point the
                                        # root urlconfig at myapp.urls module
]

from django.urls import  path
from watchlist_app.views import moivelist,moive_details

urlpatterns = [
  
    path('list/',moivelist,name='moivelist' ),
    path('<int:pk>/',moive_details,name='moive_details' ),
]

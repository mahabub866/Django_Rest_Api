
from django.urls import  path
from watchlist_app.api.views import moivelist,moive_details,user_list,user_details

urlpatterns = [
  
    path('list/',moivelist,name='moivelist' ),
    path('userlist/',user_list,name='user_list' ),
    path('moive_id:<int:pk>/',moive_details,name='moive_details' ),
    path('user_id:<int:pk>/',user_details,name='user_details' ),
]

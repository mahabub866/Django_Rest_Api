
from django.urls import  path
from watchlist_app.api.views import MoiveDetailsAV, MoiveListAV,user_list,user_details

urlpatterns = [
  
    # path('list/',moivelist,name='moivelist' ),
    path('list/',MoiveListAV.as_view(),name='moivelist' ),
    path('userlist/',user_list,name='user_list' ),
    # path('moive_id:<int:pk>/',moive_details,name='moive_details' ),
    path('moive_id:<int:pk>/',MoiveDetailsAV.as_view(),name='moive_details' ),
    path('user_id:<int:pk>/',user_details,name='user_details' ),
]

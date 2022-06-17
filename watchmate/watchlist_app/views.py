from django.shortcuts import render
from watchlist_app.models import Moive
from django.http import JsonResponse
# Create your views here.
def moivelist(request):
    moives=Moive.objects.all()
    data={'moives':list(moives.values())}
    return JsonResponse(data  )

def moive_details(request,pk):
    moive=Moive.objects.get(pk=pk)
    data={
        'name':moive.name,
        'active':moive.active,
        'description':moive.description
  
        
    }
    return JsonResponse(data  )
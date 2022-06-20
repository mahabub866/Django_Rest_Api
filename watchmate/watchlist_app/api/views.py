
from watchlist_app.api.serializers import MoiveSerializer
from watchlist_app.models import Moive
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view()
def moivelist(request):
    moives = Moive.objects.all()
    serializer=MoiveSerializer(moives,many=True)
    return Response(serializer.data)

@api_view()
def moive_details(request, pk):
    moive = Moive.objects.get(pk=pk)
    serializer=MoiveSerializer(moive)
    return Response(serializer.data)
 
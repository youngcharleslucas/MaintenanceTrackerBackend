from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import RunMiles
from .serializers import RunMiles, RunMilesSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_runmiles(request):
    runmiles = RunMiles.objects.all()
    serializer = RunMilesSerializer(runmiles, many=True)
    return Response(serializer.data)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Shirt, Pant
from .serializers import ShirtSerializer, PantSerializer
from video_processing import process_video


class ShirtViewSet(viewsets.ModelViewSet):
    queryset = Shirt.objects.all()
    serializer_class = ShirtSerializer

class PantViewSet(viewsets.ModelViewSet):
    queryset = Pant.objects.all()
    serializer_class = PantSerializer

@api_view(['POST'])
def try_on_clothes(request):
    shirt_id = request.data.get('shirt')
    pant_id = request.data.get('pant')

    try:
        shirt = Shirt.objects.get(id=shirt_id)
        pant = Pant.objects.get(id=pant_id)
    except (Shirt.DoesNotExist, Pant.DoesNotExist):
        return Response({'error': 'Shirt or Pant not found'}, status=404)

    # Call the video processing function
    process_video(shirt.image.path, pant.image.path)

    return Response({
        'shirt': ShirtSerializer(shirt).data,
        'pant': PantSerializer(pant).data
    })
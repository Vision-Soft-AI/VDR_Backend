from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import render
from django.urls import reverse

from .models import Shirt, Pant
from .serializers import ShirtSerializer, PantSerializer


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

    # Generate URL for the try-on clothes page
    page_url = reverse('try_on_clothes_page', kwargs={'shirt_id': shirt_id, 'pant_id': pant_id})
    full_url = request.build_absolute_uri(page_url)

    return Response({
        'shirt': ShirtSerializer(shirt).data,
        'pant': PantSerializer(pant).data,
        'url': full_url
    })

def try_on_clothes_page(request, shirt_id, pant_id):
    return render(request, 'index.html', {
        'shirt_id': shirt_id,
        'pant_id': pant_id
    })

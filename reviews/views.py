from rest_framework import generics
from .models import Reviews
from .serializers import ReviewSerializer
# Create your views here.

class ReviewView(generics.ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from places.models import Place
from .models import Review

class AddReviewView(APIView):
    def post(self, request):
        place, _ = Place.objects.get_or_create(
            name=request.data['name'],
            address=request.data['address']
        )

        review, created = Review.objects.get_or_create(
            user=request.user,
            place=place,
            defaults={
                'rating': request.data['rating'],
                'text': request.data.get('text', '')
            }
        )

        if not created:
            return Response(
                {"error": "Already reviewed"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response({"message": "Review added"}, status=201)

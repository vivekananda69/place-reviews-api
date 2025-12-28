from django.db.models import Avg
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Place

class SearchPlaceView(APIView):
    def get(self, request):
        name = request.query_params.get('name')
        min_rating = request.query_params.get('min_rating')

        qs = Place.objects.annotate(avg_rating=Avg('reviews__rating'))

        if min_rating:
            qs = qs.filter(avg_rating__gte=min_rating)

        if name:
            exact = qs.filter(name__iexact=name)
            partial = qs.filter(name__icontains=name).exclude(id__in=exact)
            qs = exact | partial

        return Response([
            {"name": p.name, "average_rating": round(p.avg_rating or 0, 2)}
            for p in qs
        ])

class PlaceDetailView(APIView):
    def get(self, request, place_id):
        place = Place.objects.get(id=place_id)

        user_review = place.reviews.filter(user=request.user)
        other_reviews = place.reviews.exclude(user=request.user)

        reviews = list(user_review) + list(other_reviews)

        return Response({
            "name": place.name,
            "address": place.address,
            "average_rating": place.average_rating(),
            "reviews": [
                {
                    "user": r.user.name,
                    "rating": r.rating,
                    "text": r.text,
                    "created_at": r.created_at
                } for r in reviews
            ]
        })

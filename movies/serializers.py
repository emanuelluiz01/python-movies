from rest_framework import serializers
from .models import ParentalRating
from movies.models import Movie
import ipdb


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(
        max_length=10,
        allow_null=True,
        default=None,
    )
    rating = serializers.ChoiceField(
        choices=ParentalRating.choices,
        default=ParentalRating.RATED_G,
    )
    synopsis = serializers.CharField(allow_null=True, default=None)
    added_by = serializers.CharField(source="user.email", read_only=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

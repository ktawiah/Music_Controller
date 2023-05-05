from .models import Room
from rest_framework import serializers


class RoomSerializer(serializers.ModelSerializer):
    """Serializes the room model"""

    class Meta:
        model = Room
        fields = (
            "id",
            "code",
            "host",
            "guest_can_pause",
            "votes_to_skip",
            "created_at",
        )

from rest_framework import serializers
from .models import Team


class TeamSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Team
        fields = ('id', 'first_name', 'last_name', 'age', 'role',
                  'phone', 'email', 'created_on', 'updated_on')
        read_only_fields = ('created_on', 'updated_on')

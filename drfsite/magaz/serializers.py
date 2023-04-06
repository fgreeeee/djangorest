from rest_framework import serializers

from .models import Magaz


class MagazSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magaz
        fields = ('title', 'cat_id')
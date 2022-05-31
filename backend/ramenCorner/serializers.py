from rest_framework import serializers
from .models import RamenCorner

class RamenCornerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RamenCorner
        fields = ('id' ,'title', 'videoUrl')
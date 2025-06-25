from rest_framework import serializers
from .models import Transfer , Rumor


class TransferSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Transfer
        fields = ['player_name', 'from_team', 'to_team', 'fee', 'description', 'image', 'date']


class RumorSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Rumor
        fields = ['player_name', 'from_team', 'source', 'credibility', 'date', 'image_url']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None

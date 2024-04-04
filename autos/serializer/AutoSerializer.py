from rest_framework.serializers import ModelSerializer

from autos.models.Auto import Auto


class AutoSerializer(ModelSerializer):
    class Meta:
        model = Auto
        fields ='__all__'
import re

from rest_framework import serializers
from .models import Link

from utils.get_random_string import get_random_string
from config.settings import URL_REXEX

class LinkSerializer(serializers.ModelSerializer):
    short_address = serializers.SerializerMethodField()

    def get_short_address(self, obj):
        domain = self.context['domain']
        return f"{domain}/{obj.key}"

    def validate_full_address(self, value):
        print("URL_REXEX:", URL_REXEX)
        print("value:", value)
        if re.search(URL_REXEX, value):
            return value
        raise serializers.ValidationError('invalid url')

    def create(self, validated_data):
        key = get_random_string()
        full_address = validated_data['full_address']

        link_object, created = Link.objects.get_or_create(full_address=full_address)

        if created:
            link_object.key = key
            link_object.save()

 
        return link_object


    class Meta:
        model = Link
        fields = ['full_address', 'short_address', 'access_count', 'key', 'created_at']
        read_only_fields = ['access_count', 'key', 'created_at']
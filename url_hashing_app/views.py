from django.http import HttpResponseRedirect
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from utils.get_random_string import get_random_string
from . import tests

from .models import Link
from .serializers import LinkSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    lookup_field = 'key'

    def get_serializer_context(self):
        return {"domain": self.request.META["HTTP_HOST"]}

    def get_permissions(self):
        if self.action in ['create', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]

    # def retrieve(self, request, key=None):
    #     try:
    #         shortened_url = Link.objects.get(key=key)
    #     except Link.DoesNotExist:
    #         return Response({'detail': 'Shortened URL not found.'}, status=status.HTTP_404_NOT_FOUND)
    #     shortened_url.access_count += 1
    #     shortened_url.save()
    #     serializer = self.get_serializer(shortened_url)
    #     return Response(status=status.HTTP_302_FOUND, headers={'Location': shortened_url.full_address})

    def retrieve(self, request, key=None):
        instance = self.get_object()

        if instance.access_count >= 5:
            # Generate a new short URL key
            new_key = get_random_string()

            # Create a new instance with the new short URL
            new_instance = Link.objects.create(
                key=new_key, full_address=instance.full_address)

            # Delete the previous instance
            instance.delete()

            # Reset the access count for the original instance
            new_instance.access_count = 0
            new_instance.save()

            serializer = self.get_serializer(new_instance)
            return Response({'Detail': 'Old URL Expired', 'New_URL': serializer.data['short_address'], })

        try:
            shortened_url = Link.objects.get(key=key)
        except Link.DoesNotExist:
            return Response({'detail': 'Shortened URL not found.'}, status=status.HTTP_404_NOT_FOUND)
        shortened_url.access_count += 1
        shortened_url.save()
        serializer = self.get_serializer(shortened_url)

        return Response(status=status.HTTP_302_FOUND, headers={'Location': shortened_url.full_address})

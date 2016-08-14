from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from npnbase.models import NameRecord, NameGroupRecord, GroupRecord, NameZodiacRecord
from serializers import NameSerializer, GroupSerializer, NameGroupSerializer, NameZodiacSerializer


@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'names': reverse('name-list', request=request),
        'groups': reverse('group-list', request=request),
        'zodiacs': reverse('zod-list', request=request),
    })


class NameList(generics.ListCreateAPIView):
    model = NameRecord
    serializer_class = NameSerializer


class NameGroupList(generics.ListCreateAPIView):
    model = NameGroupRecord
    serializer_class = NameGroupSerializer


class NameZodiacList(generics.ListCreateAPIView):
    model = NameZodiacRecord
    serializer_class = NameZodiacSerializer

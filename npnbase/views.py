from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from npnbase.models import NameRecord
from npnbase.serializers import NameSerializer



@api_view(['GET', 'POST'])
@csrf_exempt
def names_list(request):
    if request.method == 'GET':
        snippets = NameRecord.objects.all()
        serializer = NameSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NameSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@csrf_exempt
def names_detail(request, pk):
    try:
        name = NameRecord.objects.get(pk=pk)
    except NameRecord.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = NameSerializer(name)
        return Response(serializer.data)
    return HttpResponse(status=404)


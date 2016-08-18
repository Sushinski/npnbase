from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from npnbase.models import NameRecord, NameZodiacRecord, NameGroupRecord
from npnbase.serializers import NameSerializer


@api_view(['GET', 'POST'])
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
    return HttpResponse(status=404)


@api_view(['GET'])
def names_detail(request, month, sex, group):
    try:
        name = NameRecord.objects.all()
        if month != u'0':
            ids = NameZodiacRecord.objects.filter(zodiac_id__zod_month=month).values_list("name_id", flat=True)
            name = name.filter(_id__in=ids)
        if sex != u'2':
            name = name.filter(sex=sex)
        if group != u'all':
            ids = NameGroupRecord.objects.filter(group_id__group_name=group).values_list("name_id", flat=True)
            name = name.filter(_id__in=ids)
        serializer = NameSerializer(name, many=True)
        return Response(serializer.data)
    except NameRecord.DoesNotExist:
        return HttpResponse(status=404)


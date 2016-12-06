from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from npnbase.models import NameRecord
from npnbase.serializers import NameSerializer
from npnbase.forms import NameForm


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
            name = name.filter(zodiac__zod_month=month).values_list("name_id", flat=True)
        if sex != u'2':
            name = name.filter(sex=sex)
        if group != u'all':
            name = name.filter(group__group_name=group).values_list("name_id", flat=True)
        serializer = NameSerializer(name, many=True)
        return Response(serializer.data)
    except NameRecord.DoesNotExist:
        return HttpResponse(status=404)


def names_new(request):
    if request.method == "POST":
        post_form = NameForm(request.POST)
        if post_form.is_valid():
            post_name = post_form.save(commit=False)
            new_name, created = NameRecord.objects.get_or_create(
                name=post_name.name
            )
            if created:
                new_name.sex = post_name.sex
                new_name.description = post_name.description
                new_name.groups = post_name.groups
                new_name.zodiacs = post_name.zodiacs
                new_name.save()
    form = NameForm()
    return render(request, 'npnbase/base.html', {'form': form})

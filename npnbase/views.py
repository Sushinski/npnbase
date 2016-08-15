from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from npnbase.models import NameRecord
from npnbase.serializers import NameSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def names_list(request):
    if request.method == 'GET':
        snippets = NameRecord.objects.all()
        serializer = NameSerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NameSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def names_detail(request, pk):
    try:
        name = NameRecord.objects.get(pk=pk)
    except NameRecord.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = NameSerializer(name)
        return JSONResponse(serializer.data)
    return HttpResponse(status=404)


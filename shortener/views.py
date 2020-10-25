from rest_framework.viewsets import ViewSet
from rest_framework.generics import CreateAPIView
from django.http import HttpResponseRedirect
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny
from .models import ShortLink
from .serializers import ShortenURLSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status


class ShortenURLView(ViewSet, CreateAPIView):
    http_method_names = ['post', 'head', 'options']
    renderer_classes = [JSONRenderer]
    parser_classes = [JSONParser]
    permission_classes = (AllowAny,)
    serializer_class = ShortenURLSerializer


@api_view(['GET', 'HEAD'])
def redirector(request, slug):
    link_obj = ShortLink.objects.filter(slug=slug)
    if link_obj.exists():
        original_url = link_obj.first().url
        return HttpResponseRedirect(original_url)
    return Response(status.HTTP_404_NOT_FOUND)

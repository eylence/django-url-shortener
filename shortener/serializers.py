from rest_framework.serializers import ModelSerializer
from .models import ShortLink
import base58
import secrets
from django.conf import settings


def generate_short_url(url):
    slug = str(base58.b58encode(secrets.token_bytes(4)), "utf-8")
    exists = ShortLink.objects.filter(slug=slug).exists()
    if exists:
        generate_short_url(url)
    return slug


class ShortenURLSerializer(ModelSerializer):
    class Meta:
        model = ShortLink
        fields = ['url', 'shortened_url']
        read_only_fields = ['shortened_url']

    def create(self, validated_data):
        url = validated_data['url']
        generated_slug = generate_short_url(url)
        shortened_url = "{}/{}".format(settings.SHORT_DOMAIN, generated_slug)
        return ShortLink.objects.create(url=url, slug=generated_slug, shortened_url=shortened_url)

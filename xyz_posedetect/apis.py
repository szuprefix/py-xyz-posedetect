# -*- coding:utf-8 -*-
from __future__ import division

from django.http import FileResponse
from xyz_restful.mixins import BatchActionMixin
from . import models, serializers
from rest_framework import viewsets
from xyz_restful.decorators import register


@register()
class VideoViewSet(BatchActionMixin, viewsets.ModelViewSet):
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer
    search_fields = ('source_url',)
    filter_fields = {
        'id': ['in', 'exact'],
        'create_time': ['range']
    }
    ordering_fields = ('is_active', 'create_time',)


    def proxy(self, request):
        url = request.query_params.get('url')
        from urlparse import urlsplit
        from xyz_util.crawlutils import http_get
        ps = urlsplit(url)
        referer = request.GET.get('referer') or '%s://%s' % (ps.scheme, ps.netloc)
        r = http_get(url, proxy=False, referer=referer)
        data = r.content
        return FileResponse(data, content_type=r.headers['Content-Type'])

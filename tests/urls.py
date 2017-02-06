# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from virtual_field.urls import urlpatterns as virtual_field_urls

urlpatterns = [
    url(r'^', include(virtual_field_urls, namespace='virtual_field')),
]

# -*- coding: UTF-8
import django

from .decorators import VirtualField


def _values(self, *fields):
    annotations = {}
    for fname in fields:
        v = getattr(self.model, fname, None)
        if v and isinstance(v, VirtualField):
            annotations[v.name] = v.func(self.model)
    annoted_queryset = self.annotate(**annotations)
    return _values.original(annoted_queryset, *fields)


def apply_all():
    _values.original = django.db.models.query.QuerySet.values
    django.db.models.query.QuerySet.values = _values

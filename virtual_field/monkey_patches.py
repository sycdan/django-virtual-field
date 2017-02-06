# -*- coding: UTF-8
import django

from .utils import VirtualField


def _values(self, *fields):
    real_fields = list(fields)
    annotations = {}
    for fname in fields:
        v = self.model.__dict__.get(fname)
        if v and isinstance(v, VirtualField):
            annotations[v.name] = v.func(self.model)
            real_fields.remove(fname)
    clone = _values.original(self, *real_fields)
    return clone.annotate(**annotations)


def apply_all():
    _values.original = django.db.models.query.QuerySet.values
    django.db.models.query.QuerySet.values = _values

# -*- coding: UTF-8
class VirtualField:
    """Generally not used directly."""
    def __init__(self, func, *args, **kwargs):
        self.name = func.__name__
        self.func = func


def virtual_field(func):
    """Decotator.

    class MyModel(models.Model):
        @virtual_field
        def spam(cls):
            return models.ExpressionWrapper(...)
    """
    return VirtualField(func)

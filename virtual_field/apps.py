# -*- coding: UTF-8
from django.apps import AppConfig

import monkey_patches


class VirtualFieldConfig(AppConfig):
    name = 'virtual_field'

    def ready(self):
        monkey_patches.apply_all()

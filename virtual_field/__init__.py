__version__ = '0.1.0'

from .decorators import virtual_field, VirtualField
from .monkey_patches import apply_all

apply_all()

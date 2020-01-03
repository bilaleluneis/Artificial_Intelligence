from functools import wraps
from typing import no_type_check

__author__ = "Bilal El Uneis"
__since__ = "Jan 2020"
__email__ = "bilaleluneis@gmail.com"


@no_type_check
def frozen(cls):
    """
    based on https://stackoverflow.com/questions/3603502/prevent-creating-new-attributes-outside-init
    class level decorator to prevent class instances from creating dynamic properties and attributes
    """
    cls.__frozen = False

    def frozensetattr(self, key, value):
        valid_dunder_attrs = ['__orig_class__']
        if self.__frozen and key not in valid_dunder_attrs and not hasattr(self, key):
            raise AttributeError(f"Class {cls.__name__} is frozen. Cannot set {key} = {value}")
        object.__setattr__(self, key, value)

    def init_decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            func(self, *args, **kwargs)
            self.__frozen = True

        return wrapper

    cls.__setattr__ = frozensetattr
    cls.__init__ = init_decorator(cls.__init__)
    return cls

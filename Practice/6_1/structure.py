# structure.py
import logging
from typing import Any

logger = logging.getLogger(__name__)

class Structure():
    _fields = () # 모든 것은 _fields 중심으로 돌아간다
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f"Expected {len(self._fields)} arguments")
        for name, arg in zip(self._fields, args):
            setattr(self, name, arg)

    def __repr__(self):
        return "%s(%s)" % (type(self).__name__, 
                           ", ".join(repr(getattr(self, name)) for name in self._fields))

    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            # _fields 내부의 name attiribute들에 대한 private 접근, public 접근만 허용
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"No attribute {name}")

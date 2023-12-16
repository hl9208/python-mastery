# structure.py
import sys
import logging
import inspect
from typing import Any

logger = logging.getLogger(__name__)

class Structure():
    _fields = () # 모든 것은 _fields 중심으로 돌아간다

    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals # 현재 사용하는 함수 기준 n번째 계층의 locals 가져오기
        self = locs.pop('self') # dictionary의 key 값으로 pop이 가능하다
        for name, val in locs.items():
            setattr(self, name, val)

    def __repr__(self):
        return "%s(%s)" % (type(self).__name__, 
                           ", ".join(repr(getattr(self, name)) for name in self._fields))

    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            # _fields 내부의 name attiribute들에 대한 private 접근, public 접근만 허용
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"No attribute {name}")

    @classmethod
    def set_fields(cls):
        sig = inspect.signature(cls)
        cls._fields = tuple(sig.parameters)
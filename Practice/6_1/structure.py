# structure.py
import logging
from typing import Any

logger = logging.getLogger(__name__)

class Structure():
    def __init__(self, *args):
        self.name, self.shares, self.price = args

    def __repr__(self):
        return f"Stock({self.name}, {self.shares}, {self.price})"

    def __setattr__(self, name, value):
        private_name = '_' + name
        if not isinstance(private_name, self._fields):
            raise AttributeError(f'No attrivute {name}')
        setattr(self, name, value)

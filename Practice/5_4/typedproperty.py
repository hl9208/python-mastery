# typedproperty.py

def typedproperty(expected_type):
    class TypedProperty:
        def __init__(self, expected_type):
            self.expected_type
            self.private_name = None

        def __set_name__(self, cls, name):
            self.private_name = name

        @property
        def value(self):
            return getattr(self, self.private_name)

        @value.setter
        def value(self, val):
            if not isinstance(val, self.expected_type):
                raise TypeError(f'Expected {self.expected_type}')
            setattr(self, self.private_name, val)

    return TypedProperty

String = lambda : typedproperty(str)
Integer = lambda : typedproperty(int)
Float = lambda : typedproperty(float)
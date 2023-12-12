# typedproperty.py

def typedproperty(name, expected_type):
    private_name = '_' + name # private_name이 문자열이어도 getattr, setattr에서 접근하는데 문제가 없다.

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {self.expected_type}')
        setattr(self, private_name, val)

    return value

String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)
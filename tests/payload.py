class TestPayLoad(object):

    def __init__(self, val=10, yes=True):

        self._value = val
        self._yes = yes

    def yes(self):
        return self._yes

    def value(self):
        return self._value

    def increment_by(self, val):
        self._value += val

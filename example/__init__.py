import processing_engine


class PayLoad(object):

    def __init__(self, initial_value):
        self.val = initial_value

    def increment(self, by):
        self.val += by


engine = processing_engine.load("/path/to/test_data.xml")

payload = PayLoad(initial_value=5)
engine.process(payload)

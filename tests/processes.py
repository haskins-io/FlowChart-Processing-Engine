from processing_engine.model import Process


"""
This is a test module used for testing the engine.
"""


class Start(Process):

    def process(self, payload):
        print "At Start"


class EndOne(Process):

    def process(self, payload):
        payload.increment_by(5)


class EndTwo(Process):

    def process(self, payload):
        payload.increment_by(10)


class ProcessOne(Process):

    def process(self, payload):
        print "ProcessOne"

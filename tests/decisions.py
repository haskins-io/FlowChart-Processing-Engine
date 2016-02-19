
from processing_engine.model import Decision


"""
This is a test module used for testing the engine.
"""


class DecisionOne(Decision):

    def process(self, payload):

        if payload.yes():
            return True
        else:
            return False

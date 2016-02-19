import random

from processing_engine.model import Decision


class DecisionOne(Decision):

    def process(self, payload):
        print "DecisionOne"
        return random.choice([True, False])


class DecisionTwo(Decision):

    def process(self, payload):
        print "DecisionTwo"
        return random.choice([True, False])


class DecisionThree(Decision):

    def process(self, payload):
        print "DecisionThree"
        return random.choice([True, False])


class DecisionFour(Decision):

    def process(self, payload):
        print "DecisionFour"
        return random.choice([True, False])


class DecisionFive(Decision):

    def process(self, payload):
        print "DecisionFive"
        return random.choice([True, False])


class DecisionSix(Decision):

    def process(self, payload):
        print "DecisionSix"
        return random.choice([True, False])


class DecisionSeven(Decision):

    def process(self, payload):
        print "DecisionSeven"
        return random.choice([True, False])

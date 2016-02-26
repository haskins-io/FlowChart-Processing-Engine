from processing_engine.model import Process


class Start(Process):

    def process(self, payload):
        print "Starting with {}".format(payload.val)


class End(Process):

    def process(self, payload):
        print "Ending with {}".format(payload.val)


class ProcessOne(Process):

    def process(self, payload):

        if 'SnsTopic' in self._attrib:
            print self._attrib['SnsTopic']

        print "Incrementing by : 1"
        payload.increment(1)


class ProcessTwo(Process):

    def process(self, payload):
        print "Incrementing by : 2"
        payload.increment(2)


class ProcessThree(Process):

    def process(self, payload):
        print "Incrementing by : 3"
        payload.increment(3)


class ProcessFour(Process):

    def process(self, payload):
        print "Incrementing by : 4"
        payload.increment(4)


class ProcessFive(Process):

    def process(self, payload):
        print "Incrementing by : 5"
        payload.increment(5)


class ProcessSix(Process):

    def process(self, payload):
        print "Incrementing by : 6"
        payload.increment(6)


class ProcessSeven(Process):

    def process(self, payload):

        print "Incrementing by : 7"
        payload.increment(7)


class ProcessEight(Process):

    def process(self, payload):
        print "Incrementing by : 8"
        payload.increment(8)


class ProcessNine(Process):

    def process(self, payload):
        print "Incrementing by : 9"
        payload.increment(9)

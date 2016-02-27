import os

import processing_engine


class PayLoad(object):

    def __init__(self, initial_value):
        self.val = initial_value

    def increment(self, by):
        self.val += by


data_file_path = os.getcwd() + "/data/test_data.xml"
engine = processing_engine.load(data_file_path)

payload = PayLoad(initial_value=5)
engine.process(payload)

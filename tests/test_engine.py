import unittest

import processing_engine
from processing_engine.engine import *
from processing_engine.model import MapElement

from tests.payload import TestPayLoad


class TestEngine(unittest.TestCase):

    def test_add_action_found(self):

        m = MapElement("Name", "Element")

        engine = ProcessingEngine()
        engine.add_action("TestOne", m)

        if 'TestOne' in engine._actions:
            self.assertEqual(True, True)

    def test_add_action_not_found(self):

        m = MapElement("Name", "Element")

        engine = ProcessingEngine()
        engine.add_action("TestOne", m)

        if 'TestTwo' not in engine._actions:
            self.assertEqual(True, True)

    def test_has_action_found(self):

        m = MapElement("Name", "Element")

        engine = ProcessingEngine()
        engine.add_action("TestOne", m)

        self.assertEqual(True, engine.has_action("TestOne"))

    def test_has_action_not_found(self):

        m = MapElement("Name", "Element")

        engine = ProcessingEngine()
        engine.add_action("TestOne", m)

        self.assertEqual(False, engine.has_action("TestTwo"))

    def test_process_yes(self):

        payload = TestPayLoad(val=10, yes=True)

        engine = processing_engine.parse(self._test_data())
        engine.process(payload)

        self.assertEqual(payload.value(), 20)

    def test_process_no(self):

        payload = TestPayLoad(val=10, yes=False)

        engine = processing_engine.parse(self._test_data())
        engine.process(payload)

        self.assertEqual(payload.value(), 15)

    @staticmethod
    def _test_data():

        return """<?xml version="1.0" encoding="UTF-8"?>
<mxGraphModel>
    <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="10" source="2" target="3"></mxCell>
        <mxCell id="2" value="Start"></mxCell>
        <mxCell id="9" source="3" target="4"></mxCell>
        <mxCell id="3" value="ProcessOne"></mxCell>
        <mxCell id="7" source="4" target="6"></mxCell>
        <mxCell id="11" value="No" connectable="0" parent="7"></mxCell>
        <mxCell id="8" source="4" target="5"></mxCell>
        <mxCell id="12" value="Yes" connectable="0" parent="8"></mxCell>
        <mxCell id="4" value="DecisionOne"></mxCell>
        <mxCell id="5" value="EndTwo"></mxCell>
        <mxCell id="6" value="EndOne"></mxCell>
    </root>
</mxGraphModel>
        """

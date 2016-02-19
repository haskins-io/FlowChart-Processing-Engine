import unittest

import processing_engine


class TestLoadAndParse(unittest.TestCase):

    def test_parse(self):

        """
        The purpose of this test is to prove the parsing of the mxGraphModel XML. The parse functionality is called by
        the LOAD function which only provides the extra functionality of testing the file exists.
        """

        xml_data = """<?xml version="1.0" encoding="UTF-8"?>
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

        processing_engine.parse(xml_data)

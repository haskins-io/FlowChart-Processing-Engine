import unittest

from processing_engine.model import MapElement


class TestModel(unittest.TestCase):

    def test_constructor(self):

        m = MapElement("Name", "Element")

        self.assertEqual("Name", m.name())
        self.assertEqual("Element", m.element_class())

    def test_set_type(self):

        m = MapElement("Name", "Element")
        m.set_element_type("Decision")

        self.assertEqual("Decision", m._el_type)

    def test_set_yes(self):

        m = MapElement("Name", "Element")
        m.set_yes_element("AnElement")

        self.assertEqual("AnElement", m._el_yes)

    def test_yes(self):

        m = MapElement("Name", "Element")
        m.set_yes_element("AnElement")

        self.assertEqual("AnElement", m.yes_action())

    def test_set_no(self):

        m = MapElement("Name", "Element")
        m.set_no_element("AnElement")

        self.assertEqual("AnElement", m._el_no)

    def test_no(self):

        m = MapElement("Name", "Element")
        m.set_no_element("AnElement")

        self.assertEqual("AnElement", m.no_action())

    def test_attributes(self):

        m = MapElement("Name", "Element")
        m.set_attribs({"TestKey": "TestValue"})

        test_attibutes = m.attribs()
        test_attribute = test_attibutes['TestKey']
        self.assertEqual("TestValue", test_attribute)

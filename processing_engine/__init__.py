import os.path

import untangle

from engine import ProcessingEngine
from model import MapElement


def load(xml_file):

    """
    Public function used to load XML data from a file and create a processing engine

    :param xml_file: Full path to file that contains the XML data
    :return: an instance of ProcessingEngine
    """
    if not os.path.isfile(xml_file):
        raise Exception("Unable to find the XML File")

    return parse(xml_file)


def parse(xml_string):

    """
    Public function used to parse XML data and create a processing engine

    :param xml_string: XML data to parse
    :return: an instance of ProcessingEngine
    """

    xml = _parse_xml(xml_string)

    return _create_processing_engine(xml)


def _parse_xml(xml_string):

    try:
        xml_obj = untangle.parse(xml_string)
    except Exception as e:
        raise Exception("Unable to parse the XML : {}".format(e.message))

    return xml_obj


def _create_processing_engine(xml_obj):

    maps = {}
    links = {}

    mx_cells = xml_obj.mxGraphModel.root.mxCell

    #
    # Find all Actions and Links
    #
    for cell in mx_cells:

        cell_id = str(cell['id'])
        if cell_id != '0' and cell_id != '1':

            # Is Action cell
            if cell.get_attribute('value') is not None and cell.get_attribute('connectable') is None:

                map_name = cell.get_attribute('value')
                map_element = MapElement(name=map_name, element=map_name)
                maps[cell_id] = map_element
                
            # Is Link Cell
            if cell.get_attribute('source') is not None and cell.get_attribute('target') is not None:

                links[cell_id] = {
                    'source': cell.get_attribute('source'),
                    'target': cell.get_attribute('target'),
                    'boolean': True
                }

    #
    # Update links with YES or NO value
    #
    for cell in mx_cells:

        cell_id = str(cell['id'])
        if cell_id != '0' and cell_id != '1' and cell.get_attribute('connectable') is not None:

            link_type = cell.get_attribute('value').lower()
            link_parent = cell.get_attribute('parent')

            link_data = links[link_parent]
            if 'no' in link_type:
                link_data['boolean'] = False
                links[link_parent] = link_data

    processengine = ProcessingEngine()

    #
    # Update Action yes/no elements
    #
    for key, value in links.iteritems():

        source_action = maps[value['source']]
        target_action = maps[value['target']]

        if value['boolean']:
            source_action.set_yes_element(target_action.element_class())
        else:
            source_action.set_no_element(target_action.element_class())

        if source_action.yes_action() is not None and source_action.no_action() is not None:
            source_action.set_element_type("Decision")
        else:
            source_action.set_element_type("Processor")

        processengine.add_action(source_action.name(), source_action)

    #
    # Need to add 'End' as it has no target links so won't be picked up in the last section
    #
    for key, map_element in maps.iteritems():

        element_name = map_element.name()
        if not processengine.has_action(element_name):
            map_element.set_element_type("Processor")
            processengine.add_action(element_name, map_element)

    return processengine

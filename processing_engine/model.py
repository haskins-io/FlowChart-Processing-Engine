import abc


class MapElement(object):

    """
    A Class that models an element on the FlowChart.
    """

    def __init__(self, name, element):

        """
        Class initialiser

        :param name: This the unique name of the Element.
        :param element: This is the Class that will be instantiated when the engine is running.
        """

        self._el_name = name
        self._el_class = element
        self._el_type = None
        self._el_yes = None
        self._el_no = None

    def name(self):
        """
        Returns the name of the Element
        :return: Element name as a String
        """
        return self._el_name

    def yes_action(self):
        """
        Returns the name of the Element that would be processed next if the outcome of a decision is TRUE. This is also
        the response that will be called for a Process Action.
        :return: Element name as a String
        """
        return self._el_yes

    def no_action(self):
        """
        Returns the name of the Element that would be processed next if the outcome of a decision is False. This is not
        used by a Process Action as they should only have one outcome.
        :return: Element name as a String
        """
        return self._el_no

    def element_type(self):
        """
        The type of the Element e.g. Processor or Decision
        :return: Type as String
        """
        return self._el_type

    def element_class(self):
        """
        The class of the Element
        :return: Type as String
        """
        return self._el_class

    def set_yes_element(self, element):
        """
        Sets the element that will be called next if the outcome is TRUE
        :param element: Element name as String
        """
        self._el_yes = element

    def set_no_element(self, element):
        """
        Sets the element that will be called next if the outcome is FALSE
        :param element: Element name as String
        """
        self._el_no = element

    def set_element_type(self, element_type):
        """
        Sets the Type of the Element
        :param element_type: String that is either 'Decision' or 'Processor'
        """
        self._el_type = element_type

    def __str__(self):
        return "{} : yes -> {} : no -> {} : Type -> {}".format(self._el_name, self._el_yes, self._el_no, self._el_type)


class Decision(object):

    """
    Abstract class that all Decision Action should extend
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def process(self, payload):

        """
        A Decision should return a boolean value to indicate which decision was made

        :param payload: Object to be passed around the FlowChart
        """


class Process(object):

    """
    Abstract class that all Process Actions should extend
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def process(self, payload):

        """
        A Process should return a boolean value

        :param payload: Object to be passed around the FlowChart
        :return: The name of the element that should be processed next
        """

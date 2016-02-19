class ProcessingEngine(object):

    """
    ProcessingEngine class that performs the main logic of working down a Flow Chart, calling the relevant Element and
    continuing depending on the result of the call to the Element.
    """

    def __init__(self):

        """
        Default constructor. This will attempt to import two modules 'decisions' and 'processes', if either could not be imported an exception will be thrown.

        :return:
        """

        self._actions = {}
        self._decisions = __import__("decisions")
        self._processes = __import__("processes")

    def add_action(self, name, action):

        """
        Adds an Action to the Processing Engine

        :param name: Name of the Action to add
        :param action: Instance of MapElement
        """
        self._actions[name] = action

    def has_action(self, action_name):

        """
        Returns a boolean flag to indicate if the action name is already registered with the engine

        :param action_name: Name of action to check
        :return: True or False
        """

        return action_name in self._actions

    def process(self, payload, start_point='Start'):

        """
        Processes the payload through the Flow Chart starting at the start_point

        :param payload: Payload to pass through the Flow Chart
        :param start_point: Name of initial Action to enter Flow Chart. This defaults to 'Start'
        """

        current_action_name = start_point

        keep_processing = True
        while keep_processing:

            current_action = self._actions[current_action_name]
            element_type = current_action.element_type()

            if 'Decision' in element_type:
                my_class = getattr(self._decisions, current_action_name)
            else:
                my_class = getattr(self._processes, current_action_name)

            instance = my_class()

            yes = True
            if 'Decision' in element_type:
                yes = instance.process(payload)
            else:
                instance.process(payload)

            if yes:
                current_action_name = current_action.yes_action()
            else:
                current_action_name = current_action.no_action()

            if current_action_name is None:
                keep_processing = False

FlowChart Processing Engine
===========================

Provides a simple Processing Engine for Python applications utilising a Flow Chart based on mxGraph.


## Using the engine

The engine is designed to process Flow Charts that have been exported to XML that conform to the mxGraph standard.
You can use a website like [draw.io](http://draw.io "draw.io") to create your flow chart.

Once you have drawn your chart using draw.io you need to export it as an XML file (not compressed).

The XML file will be parsed by FlowChart Processing Engine and starting at an element at a named element (or 'Start' if not provided) will traverse the chart 
passing in a payLoad to each element until it reaches the bottom.


### Creating your Flow Chart

There are few simple rules when creating your Flow Chart that you must follow in order for the Engine to work. This assumes you are using draw.io to create your
Flow Chart.

* Each element on the chart needs to be named, you can do this by double clicking on the element and entering a name. If you are creating the XML manually you
  will need to add an attribute to the **mxCell** called 'value' with the cell name. 
* The name of the element indicates a Python Class to be used at this stage of the processing, this means the name must conform to Python naming conventions e.g
  'IsUKClient' and not 'Is UK Client'
* Lines from a Decision have to be named either 'yes' or 'no', again double click on a line to give it name or use the Value attribute.

Currently the engine only has the concept of two types of elements on a chart:

* Decision : Can have multiple Sources but only two targets
* Process : Can have multiple Sources but only single target


#### XML Attributes

All attributes associated with the XML elements contained within the XML file will be loaded and associated with the appropriate Decision and Process. This means
that you can follow good OO principals by only creating an Action once and using it in multiple places customising it for it's position in the chart. An example
of this might be a **SendEmail** process that is capable of sending an email to the address that is defined by the Attribute of the individual Action.


#### Gotchas

Currently the Processing Engine performs no validation of the XML data provided other than - is it valid XML. It simply parses the XML and attempts to create a 
working engine.

If you are having problems the first things you should check are:

* Have you given a unqiue name to each element?
* Have you given a name to the joining connectors from a Decision ('yes' or 'no')?
* Do you have a Class that matches the name of an element? This is case-sensitive
* Has you defined the Class in the correct place, that is; are your Decisions in decisions.py and Processes in process.py?
* Does your line actually connect to the element, or stop short?
 
 
### Defining your Decisions and Processes

Decisions and Processes are implemented as Python classes, you need to create two modules to store them. The file names must be:
 
* decisions.py
* processes.py

The 'Start' and 'End' elements are classed as a Process so should be placed in processes.py.

There are two Abstract classes that should be implemented by a Decision or Process. The abstract classes has an abstract function called 'process' that will be 
called by the engine so needs to be implemented.

Both Decisions and Processes should be considered to be stateless, that is they contain any information that changes based on a processed payload. Though obviously
this is based on what you are doing.


#### Process

A Process is an element that could either mutate the contents of the PayLoad, or performs an action based on the state of the payload. A Process element does not
return a value and only has a single exit.

The following is a very simple example of a Process. When the **process** function is called it calls a function on the PayLoad and prints out a message.

    class ProcessOne(Process):

        def process(self, payload):
            print "Incrementing by : 1"
            payload.increment(1)


#### Decision

A Decision is an element that makes a decision based on the received state of the PayLoad, and returns a boolean value to indicate the next step in the Flow.
Currently you are only have two routes (or targets) out of a decision.

The following is a very simple example of a Process. When the **process** function is called it prints its name and then randomly chooses an outcome to return

    class DecisionTwo(Decision):

        def process(self, payload):
            print "DecisionTwo"
            return random.choice([True, False])

The function needs to return either True or False which relates to the yes or no on the Flow Chart.


## Using the Engine

Using the Processing Engine is very simple; you import the module, load your Flow Chart XML, and then call process with your PayLoad. If you have already loaded
your XML you can call the **parse** function instead.

    import processing_engine

    class PayLoad(object):

        def __init__(self, initial_value):
            self.val = initial_value

        def increment(self, by):
            self.val += by

    engine = processing_engine.load("/path/to/flowchart.xml")

    payload = PayLoad(initial_value=5)
    engine.process(payload)


#### Example

The above code snippets are taken from an example implementation that can be found in the **example** directory. In here you will find a decisions.py and 
processes.py file that contains the definitions of the example elements.

In the **data** directory you will find the following files:

* draw.io.xml : a compressed XML file that can be loaded into draw.io to be examined or modified.
* test_data.xml : an XML representation of the above Flow Chart that was exported from draw.io
* draw.io.png : an image showing the flowchart that the two above files represent.


Runing the module __init__ (after changing the path to the XML file) you should get an output like this. Depending on which route is taken through the FlowChart
the values might be different.

    Starting with 5
    DecisionOne
    Incrementing by : 1
    DecisionFive
    Incrementing by : 3
    DecisionSeven
    Incrementing by : 4
    Ending with 13

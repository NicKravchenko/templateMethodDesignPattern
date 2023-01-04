from abc import ABC, abstractmethod
import json
import pandas

import xmltodict
import pprint
from xml.dom import minidom


class TemperatureRecordSummary(ABC):
    """
    The Abstract Class defines a template method that contains a skeleton of
    some algorithm, composed of calls to (usually) abstract primitive
    operations.

    Concrete subclasses should implement these operations, but leave the
    template method itself intact.
    """
    temperaturesData = {}
    dataOut = {'Min': 0, 'Max': 0, 'Average': 0}

    def template_method(self):
        """
        The template method defines the skeleton of an algorithm.
        """

        self.temperaturesData = self.readFile()
        self.process()

    # These operations have to be implemented in subclasses.
    @abstractmethod
    def readFile(self):
        print("AbstractClass says: I am doing the bulk of the work")

    # These operations already have implementations.

    def process(self):
        minTemp = float(self.temperaturesData[0]['meassure'])
        maxTemp = float(self.temperaturesData[0]['meassure'])
        avgTemp = 0
        summTemp = 0

        for i in self.temperaturesData:
            temp = float(i['meassure'])
            if (minTemp < temp):
                minTemp = temp
            if (maxTemp > temp):
                maxTemp = temp
            summTemp = summTemp + temp
        avgTemp = summTemp / len(self.temperaturesData)
        self.dataOut = {'Min': minTemp, 'Max': maxTemp, 'Average': avgTemp}

        print(self.dataOut)


class ReadFlatFile(TemperatureRecordSummary):
    """
    Concrete classes have to implement all abstract operations of the base
    class. They can also override some operations with a default implementation.
    """

    def readFile(self):
        rawFile = open('text.txt')
        content = pandas.read_csv(rawFile)
        print(content)


class ReadJsonFile(TemperatureRecordSummary):
    """
    Concrete classes have to implement all abstract operations of the base
    class. They can also override some operations with a default implementation.
    """

    def readFile(self):
        rawJson = open('text.json')
        content = json.load(rawJson)

        return content


class ReadXmlFile(TemperatureRecordSummary):
    """
    Concrete classes have to implement all abstract operations of the base
    class. They can also override some operations with a default implementation.
    """

    def readFile(self):
        with open('text.xml', 'r') as f:
            data = f.read()

        content = xmltodict.parse(data)['data']['row']
        return content


def client_code(abstract_class: TemperatureRecordSummary):
    """
    The client code calls the template method to execute the algorithm. Client
    code does not have to know the concrete class of an object it works with, as
    long as it works with objects through the interface of their base class.
    """
    abstract_class.template_method()


client_code(ReadXmlFile())

# client_code(ReadFlatFile())


# if __name__ == "__main__":
#     print("Same client code can work with different subclasses:")
#     client_code(ReadFlatFile())
#     print("")

#     print("Same client code can work with different subclasses:")
#     client_code(ConcreteClass2())

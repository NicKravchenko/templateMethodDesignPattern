from temperatureRecordSummary import TemperatureRecordSummary

import json
import pandas

import xmltodict
from xml.dom import minidom

class ReadFlatFile(TemperatureRecordSummary):
    """
    Concrete classes have to implement all abstract operations of the base
    class. They can also override some operations with a default implementation.
    """

    def readFile(self):
        rawFile = open('sample-files/text.flat')
        content = pandas.read_csv(rawFile)
        print(content)


class ReadJsonFile(TemperatureRecordSummary):
    """
    Concrete classes have to implement all abstract operations of the base
    class. They can also override some operations with a default implementation.
    """

    def readFile(self):
        rawJson = open('sample-files/text.json')
        content = json.load(rawJson)

        return content


class ReadXmlFile(TemperatureRecordSummary):
    """
    Concrete classes have to implement all abstract operations of the base
    class. They can also override some operations with a default implementation.
    """

    def readFile(self):
        with open('sample-files/text.xml', 'r') as f:
            data = f.read()

        content = xmltodict.parse(data)['data']['row']
        return content

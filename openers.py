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
        rawFlat = pandas.read_csv(
            "sample-files/text.flat", delimiter=" ", header=None).to_dict()[0]
        dictionary = []
        for i in rawFlat:
            res = {}
            if (i == 0):
                names = rawFlat[i].split("|")
                names = [element.lower() for element in names]
            else:
                values = rawFlat[i].split("|")

                for key in names:
                    for value in values:
                        res[key] = value
                        values.remove(value)
                        break

                dictionary.append(res)

        return dictionary


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

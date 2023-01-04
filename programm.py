from temperatureRecordSummary import TemperatureRecordSummary

from openers import ReadFlatFile, ReadJsonFile, ReadXmlFile


def client_code(abstract_class: TemperatureRecordSummary):
    """
    The client code calls the template method to execute the algorithm. Client
    code does not have to know the concrete class of an object it works with, as
    long as it works with objects through the interface of their base class.
    """
    abstract_class.template_method()


client_code(ReadXmlFile())
client_code(ReadJsonFile())
client_code(ReadFlatFile())

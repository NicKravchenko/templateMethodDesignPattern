from abc import ABC, abstractmethod


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

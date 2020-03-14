

class PopulationProportion:
    @staticmethod
    def proportion(data):
        subData = data
        proportion = len(subData)/(len(data) - 10)
        return proportion
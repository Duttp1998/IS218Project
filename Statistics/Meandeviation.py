
from Statistics.Mean import Mean

class Meandeviation():
    @staticmethod
    def meandeviation(array):
        mean = Mean.mean(array)
        numerator = 0
        for elem in array:
            numerator += abs((elem - mean))
        return (numerator / len(array))
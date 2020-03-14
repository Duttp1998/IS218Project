import statistics


class Mean:
    @staticmethod
    def mean(array):
        total = 0
        for num in array:
            total = total + num
        return total / len(array)

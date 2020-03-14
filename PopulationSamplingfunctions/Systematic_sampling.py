class SystemicSample:
    @staticmethod
    def systematicSample(array, n):
        result = []
        while n > 0:
            index = len(array) // n
            if index >= len(array):
                index -= 1
            result.append(array.pop(index))
            n -= 1
        return result

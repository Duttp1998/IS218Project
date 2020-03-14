from Random.Numbers import Numbers
class RandomSample:
   @staticmethod
    def simpleSample(array, n):
        result = []
        while n >= 0:
            result.append(array.pop(Numbers.randINT(0, len(array) - 1)))
            n -= 1
        return result


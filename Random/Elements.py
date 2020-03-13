import random


class Elements:
    @staticmethod
    def randElem(arr):
        return arr[random.randrange(0, len(arr))]

    @staticmethod
    def prandElem(arr, seed):
        random.seed(seed)
        return arr[random.randrange(0, len(arr))]

    @staticmethod
    def randElems(arr, n):
        result = []
        for i in range(n):
            result.append(arr[random.randrange(0, len(arr))])
        return result

    @staticmethod
    def prandElems(arr, n, seed):
        random.seed(seed)
        result = []
        for i in range(n):
            result.append(arr[random.randrange(0, len(arr))])
        return result
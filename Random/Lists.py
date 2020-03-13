import random


class Lists:
    @staticmethod
    def prandINTL(lowest, highest, n, seed):
        result = []
        random.seed(seed)
        for i in range(n):
            result.append(random.randrange(lowest, highest))
        return result

    @staticmethod
    def prandFLTL(lowest, highest, n, seed):
        result = []
        random.seed(seed)
        for i in range(n):
            result.append(random.uniform(lowest, highest))
        return result

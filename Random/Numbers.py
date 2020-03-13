import random


class Numbers:
    @staticmethod
    def randINT(lowest, highest):
        return random.randrange(lowest, highest)

    @staticmethod
    def randFLT(lowest, highest):
        return random.uniform(lowest, highest)

    @staticmethod
    def prandINT(lowest, highest, seed):
        random.seed(seed)
        return random.randrange(lowest, highest)

    @staticmethod
    def prandFLT(lowest, highest, seed):
        random.seed(seed)
        return random.uniform(lowest, highest)

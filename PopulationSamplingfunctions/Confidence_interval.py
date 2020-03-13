from scipy.stats import sem
from scipy.stats import t
from Statistics.Mean import Mean

class ConfidenceInterval:
    @staticmethod
    def confidenceIntervalPopulation(confidence, data):
        ld = len(data)
        mn = Mean.mean(data)
        std_er = sem(data)
        high = std_er * t.ppf((1 + confidence) / 2, ld - 1)

        start = mn - high
        end = mn + high

        return start, end

    @staticmethod
    def confidenceIntervalSample(confidence, data, seed, high):
        data = RandomSample.random_sample(seed, data, high)
        cip = ConfidenceInterval.confidenceIntervalPopulation(confidence, data)
        return cip

from Statistics.Zscore import Zscore
from PopulationSamplingfunctions.Margin_error import MarginError
from Statistics.Standarddeviation import Standarddeviation


class SampleSize:
    @staticmethod
    def unknown_pop_sample(data, percent):
        z_s = Zscore.zscore(data)
        m_e = MarginError.margin(data)
        p = percent
        q = 1 - p

        val = z_s / m_e
        samplePop = val**(0.5) * p * q

        return samplePop

    @staticmethod
    def known_pop_sample(data, seed):
        z_s = Zscore.zscore(data)
        m_e = MarginError.margin(data)
        s_d = Standarddeviation.standarddeviation(data)

        value = (z_s * s_d) / m_e

        popSample = value**0.5

        return popSample

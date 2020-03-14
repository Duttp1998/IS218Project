from Statistics.Zscore import Zscore
from PopulationSamplingfunctions.Margin_error import MarginError
from Statistics.PopulationProportion import PopulationProportion

class Cochran:
    @staticmethod
    def cochran(data, lstLen, seed):
        z_s = Zscore.zscore(data)
        p_p = PopulationProportion.proportion(data, lstLen, seed)
        m_e = MarginError.margin(data)
        q = 1 - p_p

        cochran = ((z_s**2) * p_p * q)/(m_e**2)

        return cochran

from Statistics.Standarddeviation import Standarddeviation
from Statistics.Zscore import Zscore


class MarginError:
    @staticmethod
    def margin(data):
        zs = Zscore.zscore(data)
        sd = Standarddeviation.standarddeviation(data)
        margin = zs * sd
        return margin

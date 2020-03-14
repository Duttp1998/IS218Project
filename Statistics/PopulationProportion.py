

class PopulationProportion:
    @staticmethod
    def proportion(data, lstLen, seed):
        subData = RandomList.list_Of_Ints(data, lstLen, seed)
        proportion = len(subData)/len(data)
        return proportion
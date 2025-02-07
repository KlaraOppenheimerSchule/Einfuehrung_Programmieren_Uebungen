class Tageskurs:
    def __init__(self, datum, aktienkurs, dax_wert, proz_v_aktie, proz_v_dax):
        self.__datum = datum
        self.__aktienkurs = aktienkurs
        self.__dax_wert = dax_wert
        self.__proz_v_aktie = proz_v_aktie
        self.__proz_v_dax = proz_v_dax

    def get_aktienkurs(self):
        return self.__aktienkurs

tageskurse = [Tageskurs('15.04.2024', 100, 15000, 0.0300, 0.0500),
              Tageskurs('15.04.2026', 110, 14900, 0.0476, 0.0132),
              Tageskurs('15.04.2025', 105, 15100, 0.0500, 0.0067)]


def sort(array):
    for i in range(len(array) - 1):
        swapped = False
        for j in range(len(array) - i - 1):
            if (array[j].get_aktienkurs() > array[j + 1].get_aktienkurs()):
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break

sort(tageskurse)
for i in tageskurse:
    print(i.get_aktienkurs())
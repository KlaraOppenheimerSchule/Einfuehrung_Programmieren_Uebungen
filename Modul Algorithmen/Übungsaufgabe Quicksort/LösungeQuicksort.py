liste = [3,1,6,6,2,9,4]

def sort(liste):
    less = []
    equal = []
    more = []

    if  len(liste)>1:
        pivot = liste[len(liste)-1]
        for x in liste:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                more.append(x)
        return (sort(less) + equal + sort(more))
    return liste

print(sort(liste))   


''' Erklärung der Vorgehensweise
1.	Pivot auswählen
2.	Partitionierung: Teile die Liste in zwei Teillisten:
3.	Eine Teilliste mit Elementen kleiner als das Pivot.
4.	Eine Teilliste mit Elementen größer als das Pivot.
5.	Rekursiver Aufruf: Wende Quicksort auf die beiden Teillisten an.
6.	Zusammenfügen: Die rekursiven Aufrufe sortieren die Teillisten, die zusammen mit dem Pivotelement die sortierte Liste ergeben.
'''

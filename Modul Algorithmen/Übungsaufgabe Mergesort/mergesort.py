def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively apply merge_sort to each half
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    merged = []
    i = j = 0
    
    # Merge the two sorted arrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Append remaining elements (if any)
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

# Example usage
if __name__ == "__main__":
    liste = [3, 1, 6, 6, 2, 9, 4]
    sorted_list = merge_sort(liste)
    print("Sorted list:", sorted_list)

'''Erklärung
merge_sort Funktion:
Die Funktion merge_sort implementiert den Mergesort-Algorithmus.
Wenn die Länge des Arrays arr kleiner oder gleich 1 ist, wird das Array direkt zurückgegeben.
Andernfalls teilt die Funktion das Array in zwei Hälften (left_half und right_half) und wendet rekursiv merge_sort auf jede Hälfte an.
Die sortierten Hälften werden dann mit der merge-Funktion zusammengeführt.

merge Funktion:
Die Funktion merge nimmt zwei sortierte Arrays (left und right) entgegen und fusioniert sie zu einem sortierten Array merged.
Ein Zeiger i durchläuft das linke Array left, und ein Zeiger j durchläuft das rechte Array right.
Elemente werden basierend auf ihrem Wert in das merged Array eingefügt, und die Zeiger i und j werden entsprechend erhöht.
Am Ende werden die restlichen Elemente aus den beiden Arrays (falls vorhanden) in das merged Array eingefügt.

Genauere Erkärung zu den Mergen:
Merge-Funktion im Mergesort-Algorithmus
Die merge-Funktion im Mergesort-Algorithmus ist dafür verantwortlich, zwei bereits sortierte Arrays (left und right) zu kombinieren und dabei ein neues sortiertes Array (merged) zu erzeugen. Hier ist eine detaillierte Erklärung der einzelnen Schritte:

Initialisierung der Zeiger:

Zwei Zeiger i und j werden eingeführt, um durch die beiden Arrays left und right zu iterieren.
i beginnt am Anfang von left (Index 0), und j beginnt am Anfang von right (ebenfalls Index 0).
Vergleichen und Einfügen:

Die merge-Funktion vergleicht die Elemente, auf die die Zeiger i und j zeigen:
Wenn das Element in left[i] kleiner oder gleich dem Element in right[j] ist, wird left[i] in das merged Array eingefügt, und der Zeiger i wird um eins erhöht (i += 1).
Andernfalls wird right[j] in das merged Array eingefügt, und der Zeiger j wird um eins erhöht (j += 1).
Dies stellt sicher, dass die Elemente in aufsteigender Reihenfolge in das merged Array eingefügt werden.
Restliche Elemente einfügen:

Nachdem ein Element aus einem der Arrays in das merged Array eingefügt wurde, wird der entsprechende Zeiger (i oder j) erhöht.
Dies wird wiederholt, bis alle Elemente aus entweder left oder right in das merged Array eingefügt wurden.
Wenn nach Abschluss der Schleife noch Elemente in einem der Arrays übrig sind (d.h., i oder j nicht das Ende des Arrays erreicht haben), werden diese verbleibenden Elemente direkt in das merged Array kopiert.


'''
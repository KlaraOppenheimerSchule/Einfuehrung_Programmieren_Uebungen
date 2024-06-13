def quicksort(li, re):
    if li < re:
        t = teilen(li, re)
        quicksort(li, t)
        quicksort(t + 1, re)

def teilen(li, re):
    i = li - 1
    j = re + 1
    pivot = Liste[(li + re) // 2]
    
    while True:
        while True:
            i += 1
            if Liste[i] >= pivot:
                break
        while True:
            j -= 1
            if Liste[j] <= pivot:
                break
        if i >= j:
            return j
        # Vertausche Liste[i] und Liste[j]
        Liste[i], Liste[j] = Liste[j], Liste[i]

# Beispielaufruf der Funktion mit passenden Argumenten
Liste = [5, 6, 3, 1, 8, 7, 2, 4]
print("Initiales Liste:", Liste)
quicksort(0, len(Liste) - 1)
print("Sortiertes Liste:", Liste)

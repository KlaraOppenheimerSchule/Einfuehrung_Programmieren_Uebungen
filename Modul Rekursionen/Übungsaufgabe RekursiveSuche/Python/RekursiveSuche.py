def recursive_search(arr, target, start=0):
    # Basisfall: Wenn die Startposition größer oder gleich der Länge des Arrays ist,
    # bedeutet das, dass das Element nicht gefunden wurde.
    if start >= len(arr):
        return -1
    
    # Wenn das aktuelle Element mit dem Ziel übereinstimmt, geben wir die Indexposition zurück.
    if arr[start] == target:
        return start
    
    # Ansonsten rufen wir die Funktion erneut auf und suchen im Rest der Liste.
    return recursive_search(arr, target, start + 1)

# Beispielanwendung
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
index = recursive_search(arr, target)
if index != -1:
    print(f"Das Element {target} wurde an der Position {index} gefunden.")
else:
    print(f"Das Element {target} wurde nicht gefunden.")

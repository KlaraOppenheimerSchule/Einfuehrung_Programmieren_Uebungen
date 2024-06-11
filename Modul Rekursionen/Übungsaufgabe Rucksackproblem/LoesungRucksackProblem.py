def print_dp_table(dp):
    for row in dp:
        print(" ".join(map(str, row)))
    print()

def knapsack(values, weights, capacity):
    # Anzahl der Gegenstände
    n = len(values)
    
    # DP-Tabelle initialisieren
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Initiale DP-Tabelle ausgeben
    print("Initiale DP-Tabelle:")
    print_dp_table(dp)
    
    # Füllen der DP-Tabelle
    # Von 1 bis Anzahl der Elemente
    for i in range(1, n + 1):

        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
        
        # DP-Tabelle nach jedem Schritt ausgeben
        print(f"DP-Tabelle nach dem Hinzufügen des Gegenstands {i} (Wert: {values[i-1]}, Gewicht: {weights[i-1]}):")
        print_dp_table(dp)
    
    # Maximaler Wert, der im Rucksack mitgegeben werden kann
    return dp[n][capacity]

# Beispielwerte und -gewichte
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

# Aufrufen der Funktion
max_value = knapsack(values, weights, capacity)
print(f"Der maximale Wert, der im Rucksack mitgegeben werden kann, ist: {max_value}")


### Erklärung für die Kontrollstruktur:
Gerne erkläre ich diese Codezeilen im Detail und auf einfache Weise:

### Codezeilen
```python
if weights[i - 1] <= w:
    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
else:
    dp[i][w] = dp[i - 1][w]
```

### Erklärung zur Kontrollstruktur
'''
1. **`if weights[i - 1] <= w:`**
   - Diese Zeile überprüft, ob das Gewicht des aktuellen Gegenstands (`weights[i - 1]`) kleiner oder gleich der aktuellen Kapazität des Rucksacks (`w`) ist.
   - `weights[i - 1]`: Da die Liste `weights` bei 0 beginnt, müssen wir `i - 1` verwenden, um den Index des aktuellen Gegenstands zu erhalten.
   - `w`: Die aktuelle Kapazität des Rucksacks in der DP-Tabelle.

2. **`dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])`**
   - Diese Zeile wird ausgeführt, wenn das Gewicht des aktuellen Gegenstands in den Rucksack passt (`weights[i - 1] <= w`).
   - Hier vergleichen wir zwei Werte:
     - `dp[i - 1][w]`: Der maximale Wert ohne den aktuellen Gegenstand (`i`). Das bedeutet, wir behalten den gleichen Wert wie in der vorherigen Zeile der Tabelle für die gleiche Kapazität.
     - `dp[i - 1][w - weights[i - 1]] + values[i - 1]`: Der maximale Wert, wenn wir den aktuellen Gegenstand hinzufügen. Dazu nehmen wir den Wert für die verbleibende Kapazität (`w - weights[i - 1]`) und addieren den Wert des aktuellen Gegenstands (`values[i - 1]`).
   - `max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])`: Wir nehmen den größeren dieser beiden Werte, weil wir den maximalen Wert im Rucksack haben möchten.

3. **`else:`**
   - Diese Zeile wird ausgeführt, wenn das Gewicht des aktuellen Gegenstands (`weights[i - 1]`) größer ist als die aktuelle Kapazität des Rucksacks (`w`).
   - Das bedeutet, wir können den aktuellen Gegenstand nicht in den Rucksack packen.

4. **`dp[i][w] = dp[i - 1][w]`**
   - Wenn wir den aktuellen Gegenstand nicht in den Rucksack packen können, bleibt der maximale Wert für diese Kapazität gleich wie zuvor, also `dp[i - 1][w]`.

### Zusammengefasst
- Wenn der aktuelle Gegenstand in den Rucksack passt (`weights[i - 1] <= w`), haben wir zwei Möglichkeiten:
  1. Wir nehmen den aktuellen Gegenstand nicht und behalten den Wert von `dp[i - 1][w]`.
  2. Wir nehmen den aktuellen Gegenstand und addieren seinen Wert (`values[i - 1]`) zum maximalen Wert der verbleibenden Kapazität (`dp[i - 1][w - weights[i - 1]]`).
- Wir wählen die Option, die den höheren Wert ergibt.
- Wenn der Gegenstand nicht passt, bleibt der Wert unverändert (`dp[i][w] = dp[i - 1][w]`).


DETAILERKLÄRUNG
Natürlich! Lassen Sie uns diese Zeilen Schritt für Schritt anhand eines konkreten Beispiels aus der obigen Rechnung erklären.

### Gegebene Daten:
- Werte (`values`): [60, 100, 120]
- Gewichte (`weights`): [10, 20, 30]
- Kapazität des Rucksacks (`capacity`): 50

### DP-Tabelle:
Wir starten mit einer leeren DP-Tabelle. Hier ist die Tabelle, nachdem die ersten beiden Gegenstände eingefügt wurden (vereinfacht dargestellt für die wichtigsten Schritte):

#### Anfangszustand (Initiale Tabelle):
```
i\w 0 1 2 ... 10 11 ... 20 21 ... 30 ... 50
0   0 0 0 ...  0  0 ...  0  0 ...  0 ...  0
1   0 0 0 ... 60 60 ... 60 60 ... 60 ... 60
2   0 0 0 ... 60 60 ...160 160...160 ...160
```

### Beispiel: Hinzufügen des 2. Gegenstands (Wert: 100, Gewicht: 20)

#### Aktuelle Kapazität (w = 20):
- `i = 2` (der 2. Gegenstand)
- `weights[i-1] = weights[1] = 20`
- `values[i-1] = values[1] = 100`

### Berechnung für dp[2][20]:

#### Zwei mögliche Werte:
1. **Ohne den 2. Gegenstand (`dp[i-1][w]`):**
   - `dp[1][20] = 60` (Wert mit nur dem ersten Gegenstand und Kapazität 20)

2. **Mit dem 2. Gegenstand (`dp[i-1][w-weights[i-1]] + values[i-1]`):**
   - `dp[i-1][w-weights[i-1]] = dp[1][20-20] = dp[1][0] = 0` (Wert mit dem ersten Gegenstand und verbleibender Kapazität 0)
   - `dp[1][0] + values[1] = 0 + 100 = 100`

#### Maximale Wert:
- `max(dp[1][20], dp[1][0] + values[1]) = max(60, 100) = 100`

#### Ergebnis:
- `dp[2][20] = 100`

### Weitere Berechnung:

#### Aktuelle Kapazität (w = 30):
- `i = 2` (der 2. Gegenstand)
- `weights[i-1] = weights[1] = 20`
- `values[i-1] = values[1] = 100`

### Berechnung für dp[2][30]:

#### Zwei mögliche Werte:
1. **Ohne den 2. Gegenstand (`dp[i-1][w]`):**
   - `dp[1][30] = 60` (Wert mit nur dem ersten Gegenstand und Kapazität 30)

2. **Mit dem 2. Gegenstand (`dp[i-1][w-weights[i-1]] + values[i-1]`):**
   - `dp[i-1][w-weights[i-1]] = dp[1][30-20] = dp[1][10] = 60` (Wert mit dem ersten Gegenstand und verbleibender Kapazität 10)
   - `dp[1][10] + values[1] = 60 + 100 = 160`

#### Maximale Wert:
- `max(dp[1][30], dp[1][10] + values[1]) = max(60, 160) = 160`

#### Ergebnis:
- `dp[2][30] = 160`

### Zusammengefasst:
- Bei jeder Kapazität (`w`) vergleichen wir den Wert ohne den aktuellen Gegenstand (aus der vorherigen Zeile, gleiche Kapazität) mit dem Wert mit dem aktuellen Gegenstand (aus der vorherigen Zeile, reduzierte Kapazität, plus der Wert des aktuellen Gegenstands).
- Wir wählen den höheren Wert, um die Tabelle zu füllen und den maximalen Wert im Rucksack zu erhalten.

Hier ist die vereinfachte Darstellung der wichtigen Schritte zur Veranschaulichung:
```
i\w 0 1 2 ... 10 11 ... 20 21 ... 30 ... 50
0   0 0 0 ...  0  0 ...  0  0 ...  0 ...  0
1   0 0 0 ... 60 60 ... 60 60 ... 60 ... 60
2   0 0 0 ... 60 60 ...100 100...160 ...160
```

Auf diese Weise wird die DP-Tabelle iterativ gefüllt, und am Ende haben wir den maximalen Wert im Rucksack für die gegebene Kapazität.

'''
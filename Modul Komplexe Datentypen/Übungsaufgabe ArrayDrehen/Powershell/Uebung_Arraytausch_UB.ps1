#A3
$zahlenReihen=  New-Object System.Collections.ArrayList

[void]$zahlenReihen.Add(0)
[void]$zahlenReihen.Add(1)
[void]$zahlenReihen.Add(2)
[void]$zahlenReihen.Add(3)
[void]$zahlenReihen.Add(4)
[void]$zahlenReihen.Add(5)
[void]$zahlenReihen.Add(6)
[void]$zahlenReihen.Add(7)
[void]$zahlenReihen.Add(8)
[void]$zahlenReihen.Add(9)

write-host "Zahlenreihe zuvor:"
$zahlenReihen

$zahlenReihen.Reverse()
write-host "Zahlenreihe danach:"
$zahlenReihen

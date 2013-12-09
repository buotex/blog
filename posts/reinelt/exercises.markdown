{
  "title": "Exercises for EA1",
  "date": "2013-12-05",
  "categories": [
  "study",
  "exercises",
  "algorithms"
  ]
}

##[U1]({{urls.media}}/Reinelt/EA1/u1.pdf)
##17
Keine Ahnung?
Ein genereller Acyclic Algorithmus existiert in der Form von Tiefensuche - wenn ein Knoten wieder hinzugefügt wird der
mit der Farbe schwarz markiert wurde, dann haben wir einen Kreis.
Erinnerung: Farben ungefärbt, grau, schwarz
Knoten der in die Nachbarschaftsliste eingetragen wurde, färbe grau
Knoten der aus der Nachbarschaftsliste gepoppt wurde, färbe schwarz -> abgearbeitet.

Angenommen es gibt Kreise mit negativen, 0 und positiven Gewichten:
wie findet man zuerst die mit 0?

Mit Floyd Warshall: Definiere (i,i) = M
wenn shortestPath(i,i,N) = 0, dann gibt es Kreis Länge 0
Halte an, bevor es negativ werden kann.
Laufzeit: laufzeit von Floyd Warshall


##[U2]({{url.media}}/Reinelt/EA1/u2.pdf)
##20

Testen auf Optimallösung:
Duales Programm erstellen
Duale Variablen bestimmen

selbe werte = optimal


##22
Bipartiter Graph G = (V,E), mit Partionen V1, V2.

Matching der Kardinalität |V1| gdw jede Untermenge eine größere Nachbarschaft hat als Mitglieder

Induktion?
TODO

##23
Ordne Gewichte Für V1 und V2
a2 = a1 + b
a4 = a3 + c

a1a3 + a2a4 = 
a1a3 + a1a3 + bc + ca1 + ba3

a1a4 + a2a3 = a1a3 + ca1 + a1a3 + ba3




import tkinter as tk
from tkinter import filedialog

count = 0
lists = []

root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilename() #Auswählen der ASCII-Datei

fobj = open(file)
for line in fobj:
    count += 1
    lists.append(list(line.rstrip()))
fobj.close()

print("Ausgabe der vollständigen Liste: ", lists)
print("Die Koordinaten y = 7 und x = 14 führen zum Zielzustand: ",lists[7][14]) #erste Koordinate ist y, zweite Koordinate ist x


"""Ihr könnte das Ganze gerne noch in Methoden organisieren (gerade bezüglich der Koordinatenauswahl ist das sinnvol), aber ich 
war jetzt einfach zu faul :D Tut mir leid. Ich kenne mich auch nicht 100%ig mit Python aus, falls ich also etwas sehr umständlich
programmiert habe, auch hierfür sorry :)"""

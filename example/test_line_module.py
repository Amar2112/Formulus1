from SunFounder_Line_Follower import Line_Follower
import time

lf = Line_Follower.Line_Follower()
REFERENCES = [50, 50, 50, 50, 50]
lf.references = REFERENCES
mins_values = lf.read_analog()
max_values = lf.read_analog()
valeursTotales = [0,0,0,0,0]
DonneesTotales = 0
while True:
    read_analog_values = lf.read_analog() 
    print("Analog", lf.read_analog())
    compteur = 0
    DonneesTotales +=1
    for values in read_analog_values:
        #DonneesTotales +=1
        valeursTotales[compteur] += values
        if values < mins_values[compteur]:
            mins_values[compteur] = values
        if values > max_values[compteur]:
            max_values[compteur] = values
        compteur +=1
    moyennes = [int(valeurTotale/DonneesTotales) for valeurTotale in valeursTotales]    
    print("Max", max_values)
    print("Min", mins_values)
    print("Moyenne",moyennes)
    print("Digital",lf.read_digital())
    print('')
    time.sleep(0.1)

import time

def afficher_heure(heure):
    heure_format = "{:02d}:{:02d}:{:02d}".format(heure[0], heure[1], heure[2])
    print(heure_format, end='\r')  # '\r' permet de revenir au début de la ligne

def regler_heure():
    heures = int(input("Entrez les heures : "))
    minutes = int(input("Entrez les minutes : "))
    secondes = int(input("Entrez les secondes : "))
    
    return heures, minutes, secondes

def regler_alarme():
    heures = int(input("Réglez l'heure de l'alarme : "))
    minutes = int(input("Réglez les minutes de l'alarme : "))
    secondes = int(input("Réglez les secondes de l'alarme : "))
    
    return heures, minutes, secondes

def verifier_alarme(heure_actuelle, heure_alarme):
    return heure_actuelle == heure_alarme

heure_actuelle = regler_heure()
heure_alarme = regler_alarme()

alarme_declenchee = False

try:
    while True:
        afficher_heure(heure_actuelle)

        # Vérifie si l'alarme doit être déclenchée
        if verifier_alarme(heure_actuelle, heure_alarme) and not alarme_declenchee:
            print("\nAlarme !")
            alarme_declenchee = True  # Marque l'alarme comme déclenchée

        time.sleep(1)

        # Incrémente le temps total en secondes
        total_secondes = heure_actuelle[0] * 3600 + heure_actuelle[1] * 60 + heure_actuelle[2] + 1

        # Calcule les nouvelles heures, minutes et secondes
        heures = total_secondes // 3600 % 24
        minutes = (total_secondes % 3600) // 60
        secondes = total_secondes % 60

        heure_actuelle = (heures, minutes, secondes)

except KeyboardInterrupt:
    print("\nProgramme arrêté.")

import RPi.GPIO as GPIO
#On importe la librarie RPi.GPIO
GPIO.setmode(GPIO.BOARD)
#On definit l utilisation des numeros sur le modele BOARD et non BCM
GPIO.setup(11, GPIO.OUT)
#On definit le port 11 en sortie
GPIO.output(11, GPIO.LOW)
#On mets le port 11 a l etat bas pour eteindre les leds
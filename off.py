import RPi.GPIO as GPIO
#On importe la librarie RPi.GPIO
GPIO.setmode(GPIO.BOARD)
#On définit l'utilisation des numéros sur le modèle BOARD et non BCM
GPIO.setup(11, GPIO.OUT)
#On définit le port 11 en sortie
GPIO.output(11, GPIO.LOW)
#On mets le port 11 à l'état bas pour éteindre les leds

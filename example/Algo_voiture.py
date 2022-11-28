import time
import picar
from picar import front_wheels
from picar import back_wheels
from SunFounder_Ultrasonic_Avoidance import Ultrasonic_Avoidance
from SunFounder_Line_Follower import Line_Follower

picar.setup()

angle = [5, 10, 30, 45]


# Définiton des fonctions utiles au script :
def line_follower_init():
    REFERENCES = [50, 50, 50, 50, 50]
    lf.references = REFERENCES
def start_move() :
    
    print('Démarrage')
      
    fw.turn_straight()
    bw.forward()
    bw.speed = 100
    #time.sleep(5)   # Pour moi : atteint 100% de la vitesse en 5s

def stop_move() :
    
    print('Arrêt')

    bw.stop()
    fw.turn_straight()

def read_line_follower(digital_values):
    theta = 0
    if(digital_values[0] == 1 and digital_values[1] == 1 and digital_values[2] == 1 and digital_values[3] == 1 and digital_values[4] == 1):
        return True, 0
    elif digital_values == [0,0,1,0,0]:
        theta = 0    
    elif digital_values == [0,1,1,0,0]:
        theta = -angle[0]
    elif digital_values == [0,0,1,1,0]:
        theta = angle[0]
    elif digital_values == [0,1,0,0,0]:
        theta = -angle[1]
    elif digital_values == [0,0,0,1,0]:                       
        theta = angle[1]
    elif digital_values == [1,1,0,0,0]:
        theta = -angle[2]
    elif digital_values == [0,0,0,1,1]:
        theta = angle[2]
    elif digital_values == [1,0,0,0,0]:
        theta = -angle[3]
    elif digital_values == [0,0,0,0,1]:
        theta = angle[3]
    return False, theta

# Paramètres utiles au script :

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')
UA = Ultrasonic_Avoidance.Ultrasonic_Avoidance(20)
threshold = 10
distance = UA.get_distance()
status = UA.less_than(threshold)
lf = Line_Follower.Line_Follower()
loop = True

# Script :

line_follower_init()

if __name__ == '__main__' : 
    while loop:   
        try :
            start_move()
            digital_values = lf.read_digital()
            print(digital_values)
            stop_car, theta = read_line_follower(digital_values)
            if(stop_car):
                loop = False
                stop_move()
            else:
                fw.turn(90 + theta)
            time.sleep(1)
#             start_move()
#             if lf == False :    # Il faudra distinguer les cas de non-dérection à gauche ou à droite de la ligne
#                 while lf == False :
#                     fw.turn(theta_1)
#                     bw.forward()
#                     bw.speed = 100
#                     time.sleep(3)
#                     fw.turn(90)
#             elif status == 1 :
#                 bw.stop()       # Décélération à prendre en compte avant
#                 fw.turn(theta_2)
#                 bw.forward()
#                 bw.speed = 50
#                 time.sleep(3)
#                 fw.turn(90)
#                 bw.speed = 0
#                 while status == True :
#                     bw.forward()
#                 fw.turn(-theta_2)
#                 bw.forward()
#                 bw.speed = 50
#                 time.sleep(3)
#                 fw.turn(90)
#                 bw.speed = 100
#                 while lf == False :
#                     bw.forward()    # On vient à redétecter la ligne en sortant du else, mais comment insérer un break pour le suiveur de ligne ?   
        except KeyboardInterrupt :
            stop_move()  
            loop = False
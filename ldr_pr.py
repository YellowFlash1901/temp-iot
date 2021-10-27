import RPi.GPIO as GPIO
import time

def LDR(cpin,lpin):
        GPIO.setmode(GPIO.BOARD)
        cap=0.0000001
        adj=2.130620985
        GPIO.setup(cpin, GPIO.OUT)
        GPIO.setup(lpin, GPIO.OUT)
        GPIO.output(cpin, False)
        GPIO.output(lpin, False)
        time.sleep(0.2)
        GPIO.setup(cpin, GPIO.IN)
        time.sleep(0.2)
        GPIO.output(lpin, True)
        starttime=time.time()
        endtime=time.time()
        while (GPIO.input(cpin) == GPIO.LOW):
            endtime=time.time()
        measureresistance=endtime-starttime
        res=(measureresistance/cap)*adj
        return(res/10)


import RPi.GPIO as GPIO
from ldr_pr import LDR
import I2C_LCD_driver

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_clear()
mylcd.lcd_display_string('Smart Lighting',1,2)
mylcd.lcd_display_string('Mode: ON',2,4)

while True:
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(18,GPIO.OUT)
        p=0
        for i in range(0,5):
            p=p+LDR(11,13)
        p_avg = p/5
        p_diff = 500 - p_avg
        if p_diff >= 0:
            GPIO.output(18, GPIO.HIGH)
            mylcd.lcd_clear()
            mylcd.lcd_display_string('LDR value:',1)
            mylcd.lcd_display_string(str(round(p_avg)),1,10)
            mylcd.lcd_display_string('LED ON',2,4)

        else:
            GPIO.output(18, GPIO.LOW)
            mylcd.lcd_clear()
            mylcd.lcd_display_string('LDR value: ',1)
            mylcd.lcd_display_string(str(round(p_avg)),1,10)
            mylcd.lcd_display_string('LED OFF',2,4)

    except KeyboardInterrupt:
        mylcd.lcd_clear()
        mylcd.lcd_display_string('Smart Lighting',1,2)
        mylcd.lcd_display_string('Mode: OFF',2,4)
        break

GPIO.cleanup()


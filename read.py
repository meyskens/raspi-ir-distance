import cgitb
import spidev
import RPi.GPIO as GPIO
import time
import sys

cgitb.enable()


spi = spidev.SpiDev()  # create spi object
spi.open(0, 0)  # open spi port 0, device (CS) 0, for the MCP8008


def readadc(adcnum):  # read out the ADC
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    r = spi.xfer2([1, (8 + adcnum) << 4, 0])
    adcout = ((r[1] & 3) << 8) + r[2]
    return adcout


while True:
    v = readadc(0) * (3.3 / 1023.0)  # Convert value to voltage

    # Thanks to
    # http://davstott.me.uk/index.php/2013/06/02/raspberry-pi-sharp-infrared/
    distance = (1.0 / (v / 13.15)) - 0.35

    print distance
    time.sleep(1)

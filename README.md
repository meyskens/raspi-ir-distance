Sharp GP2D120 IR distance sensor measurements with the Raspberry PI + MCP3008
===

This Python script allows to read out the distance measured by the Sharp GP2D120. Since the output signal is analog we're using the MCP3008 chip to convert this to a digital value.

## Connection
Connecting the sensor is simple, first wire the MCP3008 (reference voltage 3,3V) to SPI with CE0 and th yellow wire of the GP2D120 to chan 0 of the ADC. The GP2D120 should then be wired to the ground and 5V(!). The sensor needs 5V to operate but won't output more than 3V. 
![Raspberry Pi Zero on a breadboard](https://static.eyskens.me/IMG_2245.jpg)

## Output
The script has a simple output of the measured distance every second.
![Output of the script in the shell](https://static.eyskens.me/Schermafbeelding%202017-04-29%20om%2012.16.58.png)

## Notice
Since we're using IR to measure distance please keep in mind the results depend of the reflectiveness of the surface. So it is a bad idea to see these as absolute distances. 
import serial
port = serial.Serial('/dev/ttyACMO', 9600);

while 1:
	port.readLine()

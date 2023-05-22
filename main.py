import serial
import time

arduino = serial.Serial('COM15', 9600, timeout=1)
time.sleep(2)

while True:
    value = 12312311
    input_1 = str(value)
    arduino.write(input_1.encode())
    data = arduino.readline().decode().strip()
    if data:
        print("Received data:", data)
    time.sleep(1)
arduino.close()
print("done")



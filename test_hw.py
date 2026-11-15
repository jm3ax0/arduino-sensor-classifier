import serial, time

ser = serial.Serial("COM3", 9600)
time.sleep(2)

for c in [b"n", b"o", b"w", b"h"]:
    print("أرسل", c)
    ser.write(c)
    time.sleep(3)

ser.write(b"n")
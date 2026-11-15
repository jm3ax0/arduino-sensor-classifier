import serial, sys, time, os

label = sys.argv[1]
ser = serial.Serial("COM3", 9600, timeout=2)
time.sleep(2)

new_file = not os.path.exists("data.csv")
count = 0
with open("data.csv", "a") as f:
    if new_file:
        f.write("temp,hum,sound,water,lm35,label\n")
    while count < 100:
        line = ser.readline().decode(errors="ignore").strip()
        if len(line.split(",")) == 5 and "nan" not in line:
            f.write(line + "," + label + "\n")
            count += 1
            print(count, line)
print("خلصت")
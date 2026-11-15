import serial, time, joblib
import pandas as pd
from collections import deque, Counter

model = joblib.load("model.pkl")
ser = serial.Serial("COM3", 9600, timeout=2)
time.sleep(2)

codes = {"normal": b"n", "noise": b"o", "water": b"w", "hot": b"h"}
base = None
recent = deque(maxlen=3)

print("شغّال... Ctrl+C للإيقاف")
while True:
    line = ser.readline().decode(errors="ignore").strip()
    parts = line.split(",")
    if len(parts) == 5 and "nan" not in line:
        t, h, s, w = [float(x) for x in parts[:4]]
        if base is None:
            base = t
            print("حرارة الغرفة:", base)

        if t - base >= 2.0:
            state = "hot"
        else:
            X = pd.DataFrame([[s, w]], columns=["sound", "water"])
            state = model.predict(X)[0]
            if state == "water" and w < 20:
                state = "normal"

        recent.append(state)
        final = Counter(recent).most_common(1)[0][0]
        ser.write(codes[final])
        print(final, "|", line)
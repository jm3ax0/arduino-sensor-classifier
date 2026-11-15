import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

data = pd.read_csv("data.csv")
data = data[data["label"] != "hot"]

X = data[["sound", "water"]]
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("الدقة:", round(accuracy_score(y_test, pred) * 100, 1), "%")
print(confusion_matrix(y_test, pred, labels=model.classes_))
print(list(model.classes_))

joblib.dump(model, "model.pkl")
print("انحفظ")
import numpy
print(f"NumPy Version saat Training: {numpy.__version__}")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Baca dataset
dataset = pd.read_csv('student_lifestyle_dataset.csv')

# Persiapan data
X = dataset.drop(columns=['Student_ID', 'Stress_Level'])
y = dataset['Stress_Level']

# Encode target (Stress_Level)
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Melatih model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Simpan model dan encoder
joblib.dump(model, 'model/stress_model.pkl')
joblib.dump(encoder, 'model/label_encoder.pkl')

print("Model dan encoder telah disimpan di folder 'model'.")

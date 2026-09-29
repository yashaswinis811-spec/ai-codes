import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Dataset
data = {
    'Age': [22, 25, 28, 30, 35, 40, 45, 50, 55, 60],
    'Salary': [20000, 25000, 30000, 35000, 40000,
               45000, 50000, 55000, 60000, 65000],
    'Buys': ['No', 'No', 'No', 'Yes', 'Yes',
             'Yes', 'Yes', 'Yes', 'Yes', 'Yes']
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Input and output
X = df[['Age', 'Salary']]
y = df['Buys']

# Split data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Naive Bayes classifier
model = GaussianNB()

# Train the model
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

print("\nActual Output:")
print(y_test.values)

print("\nPredicted Output:")
print(y_pred)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy * 100, "%")

# Predict a new customer
new_customer = [[32, 38000]]

prediction = model.predict(new_customer)

print("\nNew Customer:")
print("Age = 32, Salary = 38000")

print("Prediction:", prediction[0])
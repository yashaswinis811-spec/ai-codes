import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

# Training data
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain',
                'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain',
                'Sunny', 'Overcast', 'Overcast', 'Rain'],

    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool',
                    'Cool', 'Cool', 'Mild', 'Cool', 'Mild',
                    'Mild', 'Mild', 'Hot', 'Mild'],

    'Humidity': ['High', 'High', 'High', 'High', 'Normal',
                 'Normal', 'Normal', 'High', 'Normal', 'Normal',
                 'Normal', 'High', 'Normal', 'High'],

    'Windy': ['False', 'True', 'False', 'False', 'False',
              'True', 'True', 'False', 'False', 'False',
              'True', 'True', 'False', 'True'],

    'Play': ['No', 'No', 'Yes', 'Yes', 'Yes',
             'No', 'Yes', 'No', 'Yes', 'Yes',
             'Yes', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

# Separate input and output
X = df.drop('Play', axis=1)
y = df['Play']

# Convert categorical values into numbers
X_encoded = pd.get_dummies(X)

# Create Decision Tree using ID3
model = DecisionTreeClassifier(
    criterion='entropy',
    random_state=0
)

# Train the model
model.fit(X_encoded, y)

# Display the decision tree
tree_rules = export_text(
    model,
    feature_names=list(X_encoded.columns)
)

print("Decision Tree using ID3 Algorithm")
print("----------------------------------")
print(tree_rules)

# Test a new example
new_data = pd.DataFrame({
    'Outlook': ['Sunny'],
    'Temperature': ['Cool'],
    'Humidity': ['High'],
    'Windy': ['False']
})

new_data_encoded = pd.get_dummies(new_data)

# Make sure test data has same columns as training data
new_data_encoded = new_data_encoded.reindex(
    columns=X_encoded.columns,
    fill_value=0
)

prediction = model.predict(new_data_encoded)

print("New Example:")
print(new_data)

print("\nPrediction:", prediction[0])
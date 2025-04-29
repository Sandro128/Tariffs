import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.compose import ColumnTransformer
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("classified_tariff_data.csv")

# Drop rows with missing values
df = df.dropna()

# Drop rows where mfn_specific_rate is greater than 1000
df = df[df['mfn_specific_rate'] <= 1000]

# Filter columns to use for the model
features = ['mfn_ad_val_rate', 'mfn_other_rate', 'mfn_rate_type_code', 'class']  # Removed 'wto_binding_code'
target = 'mfn_specific_rate'

# Filter rows based on the class
classes = {
    'cotton': ['cotton'],
    'wool': ['wool'],
    'rubber': ['rubber'],
    'steel': ['steel'],
    'fibers': ['fiber', 'fibre', 'fibers', 'fibres'],
    'fabrics': ['fabric', 'fabrics'],
    'metal': ['metal'],
    'textile': ['textile'],
    'cheese': ['cheese'],
    'yarn': ['yarn'],
    'silk': ['silk'],
    'leather': ['leather'],
    'sugar': ['sugar'],
    'salts': ['salt', 'salts'],
    'iron': ['iron'],
    'milk': ['milk']
}

# Filter data for the required classes
class_filter = df['class'].isin([item for sublist in classes.values() for item in sublist])
df = df[class_filter]

# Create a ColumnTransformer to apply OneHotEncoder to categorical columns
preprocessor = ColumnTransformer(
    transformers=[
        ('mfn_rate_type_code', OneHotEncoder(handle_unknown='ignore'), ['mfn_rate_type_code']),
        ('class', OneHotEncoder(handle_unknown='ignore'), ['class'])
    ],
    remainder='passthrough'  # Leave other columns as they are
)

# Prepare features and target
X = df[features]
y = df[target]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Standardize the numeric features (using StandardScaler)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train[['mfn_ad_val_rate', 'mfn_other_rate']])
X_test_scaled = scaler.transform(X_test[['mfn_ad_val_rate', 'mfn_other_rate']])

# Apply OneHotEncoder to categorical features
X_train_encoded = preprocessor.fit_transform(X_train)
X_test_encoded = preprocessor.transform(X_test)

# Combine the scaled numeric features with the encoded categorical features
X_train_final = pd.concat([pd.DataFrame(X_train_scaled), pd.DataFrame(X_train_encoded.toarray())], axis=1)
X_test_final = pd.concat([pd.DataFrame(X_test_scaled), pd.DataFrame(X_test_encoded.toarray())], axis=1)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train_final, y_train)
# Make predictions
y_pred = model.predict(X_test_final)

# Clip negative predictions to 0
y_pred = np.maximum(y_pred, 0)

# Evaluate the model
r2 = r2_score(y_test, y_pred)

# Output the results
print("R-squared:", r2)

# Example of predicting with new data
def predict_tariff(mfn_ad_val_rate, mfn_other_rate, mfn_rate_type_code, class_name):
    # Prepare the input features
    input_data = pd.DataFrame({
        'mfn_ad_val_rate': [mfn_ad_val_rate],
        'mfn_other_rate': [mfn_other_rate],
        'mfn_rate_type_code': [mfn_rate_type_code],
        'class': [class_name]
    })
    
    # Scale the numeric features
    input_data_scaled = scaler.transform(input_data[['mfn_ad_val_rate', 'mfn_other_rate']])
    
    # Apply OneHotEncoder to categorical features
    input_data_encoded = preprocessor.transform(input_data)
    
    # Combine the scaled numeric features with the encoded categorical features
    input_data_final = pd.concat([pd.DataFrame(input_data_scaled), pd.DataFrame(input_data_encoded.toarray())], axis=1)
    
    # Predict the tariff
    predicted_rate = model.predict(input_data_final)
    
    # Clip negative predictions to 0
    predicted_rate = np.maximum(predicted_rate, 0)
    
    return predicted_rate[0]

# Test the prediction function
predicted_rate = predict_tariff(0.15, 0.1, "0", 'cotton')
print(f"Predicted MFN Specific Rate: {predicted_rate}")

# Scatter plot of predicted vs actual values
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted MFN Specific Rate')
plt.savefig('./templates/graph.png')
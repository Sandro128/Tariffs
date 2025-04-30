# Tariff Prediction Software

Tariff Prediction
Description of the Project
The objective of this project is to develop a machine learning-based application that predicts future tariff rates for products based on historical data and associated metadata. The goal is to assist people who might be interested in knowing future tariffs such as business owners.

# Significance of the Project
This project addresses the complex and dynamic nature of international trade by applying machine learning to forecast tariff trends. Predictive tariff modeling is a novel application that can offer strategic value in trade planning and negotiations, especially in response to political or economic shifts. The project's meaningfulness lies in its potential to reduce uncertainty and improve decision-making.

# Instructions for Web Usage
## How to start

1. Unzip the `data.zip` folder inside the root of the project
2. Run `python3 combine_datasets.py` to combine all the datasets
3. Run `python3 preprocess.py` to preprocess the datasets
4. Run the model setup and inference `python3 model.py`

## Flask server

The flask server features a dashboard where you can view all the classes and 
make test inference according to paramter

## Run flask server

```
python3 server.py

```

Go to `localhost:5000`

<img width="517" alt="Screenshot 2025-04-30 at 1 33 41 pm" src="https://github.com/user-attachments/assets/0524af17-b800-41f9-bc4b-e0e9fa87e780" />

# Code Structure
daksh put diagram here

# Functionalities and Test Results
Functionalities
Load and preprocess tariff-related data
Train machine learning models on historical tariff trends
Predict future tariff rates given product metadata and trends
```
predicted_rate = predict_tariff(0.15, 0.1, "0", 'cotton')
```
```
Predicted MFN Specific Rate: 0.01779274700554182
```

##Evaluate model performance on unseen data
![image](https://github.com/user-attachments/assets/9299b43f-9f0b-4fb1-b754-71ac727ae8d3)
## Random Forest R-squared: 0.8218
## Gradient Boosting R-squared: 0.8085


# Data Collection
Data was collected from https://dataweb.usitc.gov/tariff/annual. The model includes each annual tariff report since 1997 and up to 2025. Each record includes fields such as product codes, country, date, tariff rates, and related economic indicators. The dataset contains thousands of entries spanning multiple years, with structured metadata to support forecasting. The final processed and classified file contains 150k entries.

# Data Processing
Data preprocessing included:

Cleaning and handling missing values - Deleting rows with missing values

Encoding categorical variables - Using One-hot encoding for categorical values

Feature engineering - only using the features that direcly affect the tariffs.

This step ensured that the data was in a format suitable for machine learning.

# Model Development
Input and Output
Input: 
mfn_ad_val_rate:
The ad valorem (percentage-based) tariff rate applied to the product.

mfn_other_rate:
Any other associated rate (often a fixed duty or fee).

mfn_rate_type_code:
A categorical code indicating the type of MFN (Most Favored Nation) rate.

class:
The category or type of the product (e.g., cotton, wool, steel, etc.).

Output of the Model:
mfn_specific_rate:
The predicted specific tariff rate for the product. This is usually a fixed monetary value applied per unit of product (e.g., $50 per ton).

Output: Predicted future tariff rate

Algorithms Used:
Random Forest
Gradient Boost

# Discussion and Conclusions
This project demonstrates that machine learning can effectively predict future tariff rates. Key findings include the importance of combining product and economic metadata, and the value of ensemble methods in improving prediction accuracy. Challenges involved aligning external economic indicators with tariff records and managing data sparsity. The project applied course concepts such as preprocessing, regression modeling, and evaluation techniques. Future work may include expanding the dataset and incorporating real-time inputs.

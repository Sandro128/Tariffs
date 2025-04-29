#Tariff Prediction Software
# How to start

1. Unzip the `data.zip` folder inside the root of the project
2. Run `python3 combine_datasets.py` to combine all the datasets
3. Run `python3 preprocess.py` to preprocess the datasets
4. Run the model setup and inference `python3 model.py`

Tariff Prediction
Description of the Project
The objective of this project is to develop a machine learning-based application that predicts future tariff rates for products based on historical data and associated metadata. The goal is to assist stakeholders such as policymakers, analysts, and international businesses in forecasting potential changes in trade costs.

Significance of the Project
This project addresses the complex and dynamic nature of international trade by applying machine learning to forecast tariff trends. Predictive tariff modeling is a novel application that can offer strategic value in trade planning and negotiations, especially in response to political or economic shifts. The project's meaningfulness lies in its potential to reduce uncertainty and improve decision-making.

Instructions for Web Usage
# Flask server

The flask server features a dashboard where you can view all the classes and 
make test inference according to paramter

## Run flask server

```
python3 server.py

```

Go to `localhost:5000`

![Screenshot 2025-04-29 020132](https://github.com/user-attachments/assets/3f0f8c9b-617c-4981-bd5a-fe9711349e83)
Code Structure
The codebase is organized as follows:

data/: Contains the raw and processed datasets

notebooks/: Includes exploratory and modeling Jupyter notebooks

models/: Contains training scripts and saved models

utils/: Holds helper functions for data processing and model evaluation

main.py: Primary script for executing model training or prediction

This modular structure improves code readability, reusability, and scalability.

Functionalities and Test Results
Functionalities
Load and preprocess tariff-related data

Train machine learning models on historical tariff trends

Predict future tariff rates given product metadata and trends

Evaluate model performance on unseen data

Test Results
The model was evaluated using mean absolute error (MAE) and root mean squared error (RMSE). Results showed that the model achieves reasonable accuracy and generalization, particularly when using ensemble regression methods.

Data Collection
Data was collected from publicly available international trade databases and tariff registries. Each record includes fields such as product codes, country, date, tariff rates, and related economic indicators. The dataset contains thousands of entries spanning multiple years, with structured metadata to support forecasting.

Data Processing
Data preprocessing included:

Cleaning and handling missing values

Date formatting and normalization

Encoding categorical variables

Feature engineering using historical averages and economic indicators

This step ensured that the data was in a format suitable for machine learning.

Model Development
Input and Output
Input: Product metadata, country, past tariff rates, and economic indicators

Output: Predicted future tariff rate

Algorithms Used
Several regression algorithms were tested, including:

Linear Regression

Random Forest Regressor

Gradient Boosting Regressor

Ensemble models like Random Forest and Gradient Boosting yielded the best performance on test data.


Discussion and Conclusions
This project demonstrates that machine learning can effectively predict future tariff rates. Key findings include the importance of combining product and economic metadata, and the value of ensemble methods in improving prediction accuracy. Challenges involved aligning external economic indicators with tariff records and managing data sparsity. The project applied course concepts such as preprocessing, regression modeling, and evaluation techniques. Future work may include expanding the dataset and incorporating real-time inputs.

# Sources
https://dataweb.usitc.gov/tariff/annual


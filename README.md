# CustomerConversion-Prediction
In any customer-facing organisation, predicting the behaviour of the customer can drasitcally affect the target and conversion rate while aiming to sell a product. This project aims to leverage multiple Machine Learning models to accurately predict which domain of customers are most likely to get converted. The project also contains Feature Importance which aims to provide insight on which feature is having the maximum effect on the conversion rate of the customer.

## Key Steps involved in the development of the model: 
Data Cleaning: Handle missing values, eliminate duplicates, and removing of outliers.
EDA (Exploratory Data Analysis): Understand variable distributions and their relationships to the target.
Feature Engineering: Categorical encoding and normalization of string values into numeric value.
Modeling: Development of models namely - Logistic Regression, KNN, Decision Tree, XGBoost, and Random Forest (highest accuracy).
Evaluation: Use AUROC and cross-validation scores to assess model performance.

## Tools and Libraries utilized:
Data Processing:	pandas, numpy
Visualization:	matplotlib, seaborn
Preprocessing:	StandardScaler, SMOTEENN from imblearn
Machine Learning:	scikit-learn, xgboost, linear regression, Decision Tree, Random Forest, KNN
Evaluation:	roc_auc_score, cross_val_score
Feature Importance: plot_importance from xgboost

Resulting accuracy / cross-validation score : 0.90 (highest-random forest)


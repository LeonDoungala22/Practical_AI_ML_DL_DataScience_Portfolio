**Table Description: Patient Health Data**

| Column Name            | Type    | Description                                              |
|------------------------|---------|----------------------------------------------------------|
| diabetes_classification | Integer | Classification code indicating diabetes status           |
| patient_number         | Integer | Unique identifier for each patient                        |
| cholesterol            | Integer | Cholesterol levels in the patient's blood (measured unit)|
| glucose                | Integer | Glucose levels in the patient's blood (measured unit)    |
| hdl_chol               | Integer | High-Density Lipoprotein (HDL) cholesterol levels         |
| chol_hdl_ratio         | Decimal | Cholesterol to HDL cholesterol ratio                      |
| age                    | Integer | Age of the patient in years                               |
| gender                 | String  | Gender of the patient (e.g., Male, Female)               |
| height                 | Integer | Height of the patient in a specified unit                 |
| weight                 | Integer | Weight of the patient in a specified unit                 |
| bmi                    | Decimal | Body Mass Index (BMI) calculated from height and weight   |
| systolic_bp            | Integer | Systolic blood pressure                                   |
| diastolic_bp           | Integer | Diastolic blood pressure                                  |
| waist                  | Integer | Waist circumference in a specified unit                   |
| hip                    | Integer | Hip circumference in a specified unit                     |
| waist_hip_ratio        | Decimal | Ratio of waist circumference to hip circumference         |
| diabetes               | String  | Diabetes status (e.g., Yes, No)                           |

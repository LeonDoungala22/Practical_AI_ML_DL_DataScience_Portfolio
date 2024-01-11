In this dataset, various attributes capture crucial information related to heart health. Let's explore the encoding of the selected attributes:
[Heart Disease UCI , Section : Additional Variable Information](https://archive.ics.uci.edu/dataset/45/heart+disease)


1. **Age (`#3`):**
   - *Description:* Age in years.
   - *Type:* Numerical

2. **Sex (`#4`):**
   - *Description:* Gender of the individual.
   - *Encoding:* 
     - 1: Male
     - 0: Female
   - *Type:* Categorical

3. **Chest Pain Type (`#9` - `cp`):**
   - *Description:* 
     - Value 1: Typical angina
     - Value 2: Atypical angina
     - Value 3: Non-anginal pain
     - Value 4: Asymptomatic
   - *Type:* Categorical

4. **Resting Blood Pressure (`#10` - `trestbps`):**
   - *Description:* Resting blood pressure on admission (mm Hg).
   - *Type:* Numerical

5. **Serum Cholesterol (`#12` - `chol`):**
   - *Description:* Serum cholesterol level in mg/dl.
   - *Type:* Numerical

6. **Fasting Blood Sugar (`#16` - `fbs`):**
   - *Description:* Fasting blood sugar level.
   - *Encoding:* 
     - 1: True ( > 120 mg/dl)
     - 0: False ( <= 120 mg/dl)
   - *Type:* Categorical

7. **Resting Electrocardiographic Results (`#19` - `restecg`):**
   - *Description:* 
     - Value 0: Normal
     - Value 1: ST-T wave abnormality
     - Value 2: Left ventricular hypertrophy
   - *Type:* Categorical

8. **Maximum Heart Rate Achieved (`#32` - `thalach`):**
   - *Description:* Maximum heart rate achieved during exercise.
   - *Type:* Numerical

9. **Exercise-Induced Angina (`#38` - `exang`):**
   - *Description:* Presence of exercise-induced angina.
   - *Encoding:* 
     - 1: Yes
     - 0: No
   - *Type:* Categorical

10. **ST Depression Induced by Exercise Relative to Rest (`#40` - `oldpeak`):**
    - *Description:* ST depression induced by exercise relative to rest.
    - *Type:* Numerical

11. **Slope of the Peak Exercise ST Segment (`#41` - `slope`):**
    - *Description:* 
      - Value 1: Upsloping
      - Value 2: Flat
      - Value 3: Downsloping
    - *Type:* Categorical

12. **Number of Major Vessels Colored by Fluoroscopy (`#44` - `ca`):**
    - *Description:* Number of major vessels colored by fluoroscopy (0-3).
    - *Type:* Numerical

13. **Thalassemia (`#51` - `thal`):**
    - *Description:* Thalassemia type.
    - *Encoding:* 
      - Value 3: Normal
      - Value 6: Fixed Defect
      - Value 7: Reversible Defect
    - *Type:* Categorical

14. **Diagnosis of Heart Disease (`#58` - `num`):**
    - *Description:* Diagnosis of heart disease based on angiographic findings.
    - *Encoding:* 
      - Value 0: < 50% diameter narrowing
      - Value 1: > 50% diameter narrowing
    - *Type:* Categorical
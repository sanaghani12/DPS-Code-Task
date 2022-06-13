# DPS-Code-Task

**Task 1 - Historical visualization for number of accidents per category :**
![newplot](https://user-images.githubusercontent.com/91886253/173261490-1be550a3-6e77-494f-8b7a-96ca58f8384e.png)

**Task 2 - Prediction Model (Linear Regression used) - For features that were marked as important in the task:**
![image](https://user-images.githubusercontent.com/91886253/173412930-1870319f-88d8-4b0b-8b59-a422185de4cf.png)

Training features:
'MONATSZAHL', 'AUSPRAEGUNG', 'MONAT','JAHR'

Input Values: [0,0,1,2020]
Regressor score:  0.5466887968970344
predicted value:  [578] Actual Value: [28]

**Prediction Model if we train the model with all the features:**

We see the model has improved significantly.

![image](https://user-images.githubusercontent.com/91886253/173413130-df312293-0ed0-406a-bb89-e1a94b16c934.png)

Training features:
'MONATSZAHL', 'AUSPRAEGUNG', 'MONAT','JAHR','VORJAHRESWERT','VERAEND_VORMONAT_PROZENT','VERAEND_VORJAHRESMONAT_PROZENT','ZWOELF_MONATE_MITTELWERT')

Input Values: [0,0,1,2020,22,-20,27.27,37]
Regressor score:  0.9832669606223889
predicted value:  [17] Actual Value: [28]

**Task 3 - Deployment of the model**

I have used Heroku for the purpose. I have used the first prediction model as in the task we have to give four inputs
Category: 'Alkoholunfälle'
Type: 'insgesamt
Year: '2021'
Month: '01'

Link: https://accidents-prediction.herokuapp.com/

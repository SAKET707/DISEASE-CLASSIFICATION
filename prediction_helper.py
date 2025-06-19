import joblib 
import numpy as np
import pandas as pd

model = joblib.load('model.joblib')
tfidf = joblib.load('tfidf.joblib')

def process(age, sex, symptom1, symptom2, symptom3,symptom4=None, symptom5=None, symptom6=None, symptom7=None, symptom8=None,symptom9=None, symptom10=None, symptom11=None, symptom12=None,symptom13=None, symptom14=None, symptom15=None, symptom16=None, symptom17=None):

    def get_age_group(age):
        if age <= 14:
            return 0
        elif age <= 29:
            return 1
        elif age <= 44:
            return 2
        elif age <= 59:
            return 3
        else:
            return 4
    age_group = get_age_group(age)

    sex = str(sex).strip().lower()
    sex_male = 1 if sex == 'male' else 0
    sex_female = 1 if sex == 'female' else 0

    symptoms = [
        symptom1, symptom2, symptom3, symptom4, symptom5, symptom6, symptom7, symptom8,
        symptom9, symptom10, symptom11, symptom12, symptom13, symptom14, symptom15, symptom16, symptom17
    ]
    cleaned_symptoms = [s.strip().lower() for s in symptoms if s]
    combined_symptoms = ' '.join(cleaned_symptoms)

    symptom_count = len(cleaned_symptoms)

    temp_symptoms_for_checking = combined_symptoms.replace('_', ' ')

    pediatric_fever = int(age_group == 0 and 'fever' in temp_symptoms_for_checking)

    chronic_symptoms = ['fatigue', 'joint pain', 'hypertension']
    elderly_chronic = int(
        age_group == 4 and any(symptom in temp_symptoms_for_checking for symptom in chronic_symptoms)
    )

    age_symptom_count = age_group * symptom_count

    male_elderly = int(sex_male == 1 and age_group == 4)

    age_symptom_means={0: 10.041777777777778, 1: 9.686666666666667, 2: 10.108148148148148, 3: 10.113333333333333, 4: 10.042051282051283}
    symptom_count_vs_age = symptom_count / age_symptom_means[age_group]

    symptoms_age0 = symptom_count if age_group == 0 else 0
    symptoms_age1 = symptom_count if age_group == 1 else 0
    symptoms_age2 = symptom_count if age_group == 2 else 0
    symptoms_age3 = symptom_count if age_group == 3 else 0
    symptoms_age4 = symptom_count if age_group == 4 else 0

    return {
        'age_group': age_group,
        'sex_male': sex_male,
        'sex_female': sex_female,
        'combined_symptoms': combined_symptoms,
        'symptom_count': symptom_count,
        'pediatric_fever': pediatric_fever,
        'elderly_chronic': elderly_chronic,
        'age_symptom_count':age_symptom_count,
        'male_elderly':male_elderly,
        'symptom_count_vs_age':symptom_count_vs_age,
        'symptoms_age0': symptoms_age0,
        'symptoms_age1': symptoms_age1,
        'symptoms_age2': symptoms_age2,
        'symptoms_age3': symptoms_age3,
        'symptoms_age4': symptoms_age4
    }

def predict(age, sex, symptom1, symptom2, symptom3, 
            symptom4=None, symptom5=None, symptom6=None, symptom7=None, symptom8=None,
            symptom9=None, symptom10=None, symptom11=None, symptom12=None, 
            symptom13=None, symptom14=None, symptom15=None, symptom16=None, symptom17=None):

    features = process(age, sex,
        symptom1, symptom2, symptom3,
        symptom4, symptom5, symptom6, symptom7, symptom8,
        symptom9, symptom10, symptom11, symptom12,
        symptom13, symptom14, symptom15, symptom16, symptom17)

    tfidf_vector = tfidf.transform([features['combined_symptoms']])

    ordered_keys = [
        'symptom_count', 'age_group', 'sex_female', 'sex_male', 'symptom_count_vs_age',
        'symptoms_age0', 'symptoms_age1', 'symptoms_age2', 'symptoms_age3', 'symptoms_age4',
        'pediatric_fever', 'elderly_chronic', 'age_symptom_count', 'male_elderly'
    ]

    numerical_features = np.array([[features[k] for k in ordered_keys]])

    from scipy.sparse import hstack
    final_input = hstack([tfidf_vector, numerical_features])

    prediction = model.predict(final_input)[0]
    return prediction

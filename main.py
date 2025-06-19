import streamlit as st
from prediction_helper import predict
import pandas as pd

st.title("DISEASE CLASSIFICATION")

unique_symptoms = sorted([
    'itching', 'skin_rash', 'nodal_eruptions', 'dischromic_patches', 'sneezing',
    'runny_nose', 'itchy_eyes', 'nasal_congestion', 'heartburn', 'acid_reflux',
    'chest_pain', 'dysphagia', 'cough', 'jaundice', 'fatigue', 'dark_urine',
    'abdominal_pain', 'hives', 'swelling', 'wheezing', 'nausea', 'vomiting',
    'loss_of_appetite', 'bloating', 'fever', 'weight_loss', 'night_sweats',
    'swollen_lymph_nodes', 'polyuria', 'polydipsia', 'blurred_vision',
    'diarrhea', 'abdominal_cramps', 'dehydration', 'breathlessness',
    'chest_tightness', 'headache', 'dizziness', 'photophobia', 'phonophobia',
    'visual_aura', 'neck_pain', 'stiffness', 'arm_pain', 'numbness', 'weakness',
    'confusion', 'seizures', 'yellow_skin', 'chills', 'sweating', 'muscle_pain',
    'vesicles', 'joint_pain', 'constipation', 'cold_intolerance', 'dry_skin',
    'weight_gain', 'palpitations', 'tremors', 'hunger', 'reduced_mobility',
    'creaking_joints', 'vertigo', 'balance_loss', 'pimples', 'blackheads',
    'scarring', 'oiliness', 'burning_urination', 'frequent_urination',
    'pelvic_pain', 'cloudy_urine', 'scaling', 'nail_pitting', 'blisters',
    'crusting', 'persistent_cough', 'coughing_blood', 'shortness_of_breath',
    'hoarseness', 'bone_pain', 'breast_lump', 'nipple_discharge',
    'skin_dimpling', 'breast_pain', 'nipple_inversion', 'blood_in_stool',
    'changes_in_bowel_habits', 'iron_deficiency_anemia', 'urinary_difficulty',
    'blood_in_semen', 'erectile_dysfunction', 'indigestion',
    'bloating_after_meals', 'vomiting_blood', 'black_stools', 'early_satiety',
    'heart_palpitations', 'chronic_cough', 'frequent_respiratory_infections',
    'swelling_in_legs', 'changes_in_urination', 'high_blood_pressure',
    'memory_loss', 'mood_swings', 'difficulty_speaking', 'disorientation',
    'sore_throat'
])

col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input('Age', min_value=1, max_value=90, step=1, value=18)
with col2:
    sex = st.selectbox('Sex', ['Male', 'Female'])

cols = st.columns(3)
with cols[0]:
    symptom1 = st.selectbox('Symptom 1 [REQUIRED]', unique_symptoms)
with cols[1]:
    symptom2 = st.selectbox('Symptom 2 [REQUIRED]', [s for s in unique_symptoms if s != symptom1])
with cols[2]:
    symptom3 = st.selectbox('Symptom 3 [REQUIRED]', [s for s in unique_symptoms if s not in [symptom1, symptom2]])

col_4_6 = st.columns(3)
with col_4_6[0]:
    symptom4 = st.selectbox('Symptom 4', ['None'] + [s for s in unique_symptoms if s not in [symptom1, symptom2, symptom3]])
with col_4_6[1]:
    symptom5 = st.selectbox('Symptom 5', ['None'] + [s for s in unique_symptoms if s not in [symptom1, symptom2, symptom3, symptom4]])
with col_4_6[2]:
    symptom6 = st.selectbox('Symptom 6', ['None'] + [s for s in unique_symptoms if s not in [symptom1, symptom2, symptom3, symptom4, symptom5]])

col_7_9 = st.columns(3)
with col_7_9[0]:
    symptom7 = st.selectbox('Symptom 7', ['None'] + [s for s in unique_symptoms if s not in [symptom1, symptom2, symptom3, symptom4, symptom5, symptom6]])
with col_7_9[1]:
    symptom8 = st.selectbox('Symptom 8', ['None'] + [s for s in unique_symptoms if s not in [symptom1, symptom2, symptom3, symptom4, symptom5, symptom6, symptom7]])
with col_7_9[2]:
    symptom9 = st.selectbox('Symptom 9', ['None'] + [s for s in unique_symptoms if s not in [symptom1, symptom2, symptom3, symptom4, symptom5, symptom6, symptom7, symptom8]])

col_10_12 = st.columns(3)
with col_10_12[0]:
    symptom10 = st.selectbox('Symptom 10', ['None'] + [s for s in unique_symptoms if s not in [symptom1, symptom2, symptom3, symptom4, symptom5, symptom6, symptom7, symptom8, symptom9]])
with col_10_12[1]:
    symptom11 = st.selectbox('Symptom 11', ['None'] + [s for s in unique_symptoms if s not in [symptom1, symptom2, symptom3, symptom4, symptom5, symptom6, symptom7, symptom8, symptom9, symptom10]])
with col_10_12[2]:
    symptom12 = st.selectbox('Symptom 12', ['None'] + [s for s in unique_symptoms if s not in [symptom1, symptom2, symptom3, symptom4, symptom5, symptom6, symptom7, symptom8, symptom9, symptom10, symptom11]])

col_13_15 = st.columns(3)
with col_13_15[0]:
    symptom13 = st.selectbox('Symptom 13', ['None'] + [s for s in unique_symptoms if s not in [symptom1, symptom2, symptom3, symptom4, symptom5, symptom6, symptom7, symptom8, symptom9, symptom10, symptom11, symptom12]])
with col_13_15[1]:
    symptom14 = st.selectbox('Symptom 14', ['None'] + [s for s in unique_symptoms if s not in [symptom1, symptom2, symptom3, symptom4, symptom5, symptom6, symptom7, symptom8, symptom9, symptom10, symptom11, symptom12, symptom13]])
with col_13_15[2]:
    symptom15 = st.selectbox('Symptom 15', ['None'] + [s for s in unique_symptoms if s not in [symptom1, symptom2, symptom3, symptom4, symptom5, symptom6, symptom7, symptom8, symptom9, symptom10, symptom11, symptom12, symptom13, symptom14]])

col_16_17 = st.columns(3)
with col_16_17[0]:
    symptom16 = st.selectbox('Symptom 16', ['None'] + [s for s in unique_symptoms if s not in [symptom1, symptom2, symptom3, symptom4, symptom5, symptom6, symptom7, symptom8, symptom9, symptom10, symptom11, symptom12, symptom13, symptom14, symptom15]])
with col_16_17[1]:
    symptom17 = st.selectbox('Symptom 17', ['None'] + [s for s in unique_symptoms if s not in [symptom1, symptom2, symptom3, symptom4, symptom5, symptom6, symptom7, symptom8, symptom9, symptom10, symptom11, symptom12, symptom13, symptom14, symptom15, symptom16]])

disease_advice = {
    'fungal infection': [
        'Keep skin dry and clean',
        'Avoid sharing personal items',
        'Use antifungal treatments',
        'Wear breathable fabrics',
        'Monitor for recurrence'
    ],
    'allergic rhinitis': [
        'Avoid allergens',
        'Use nasal saline rinses',
        'Take antihistamines',
        'Keep indoor air clean',
        'Consult an allergist'
    ],
    'gerd': [
        'Avoid trigger foods',
        'Eat smaller meals',
        'Elevate head during sleep',
        'Maintain healthy weight',
        'Avoid lying down after eating'
    ],
    'chronic cholestasis': [
        'Follow low-fat diet',
        'Take prescribed medications',
        'Avoid alcohol',
        'Monitor for complications',
        'Stay hydrated'
    ],
    'drug allergy': [
        'Know your allergies',
        'Wear medical alert bracelet',
        'Avoid self-medication',
        'Report reactions immediately',
        'Consider allergy testing'
    ],
    'peptic ulcer': [
        'Avoid NSAIDs',
        'Eradicate H. pylori',
        'Reduce stress',
        'Avoid trigger foods',
        'Take medications as prescribed'
    ],
    'hiv/aids': [
        'Adhere to antiretroviral therapy',
        'Practice safe sex',
        'Get regular checkups',
        'Avoid risky behaviors',
        'Stay vaccinated'
    ],
    'type 2 diabetes': [
        'Monitor blood sugar',
        'Follow balanced diet',
        'Exercise regularly',
        'Maintain healthy weight',
        'Take medications as prescribed'
    ],
    'gastroenteritis': [
        'Stay hydrated',
        'Practice hand hygiene',
        'Avoid contaminated food/water',
        'Rest adequately',
        'Seek medical help if severe'
    ],
    'bronchial asthma': [
        'Use inhalers as prescribed',
        'Avoid asthma triggers',
        'Monitor peak flow',
        'Get flu/pneumonia vaccines',
        'Develop an asthma action plan'
    ],
    'hypertension': [
        'Reduce salt intake',
        'Exercise regularly',
        'Monitor blood pressure',
        'Avoid smoking/alcohol',
        'Manage stress'
    ],
    'migraine': [
        'Identify/avoid triggers',
        'Maintain sleep schedule',
        'Stay hydrated',
        'Use prescribed medications',
        'Practice relaxation techniques'
    ],
    'cervical spondylosis': [
        'Maintain good posture',
        'Perform neck exercises',
        'Avoid heavy lifting',
        'Use ergonomic furniture',
        'Seek physiotherapy'
    ],
    'brain hemorrhage': [
        'Control blood pressure',
        'Avoid smoking/alcohol',
        'Wear helmets during activities',
        'Manage stress',
        'Seek immediate medical help for symptoms'
    ],
    'jaundice': [
        'Avoid alcohol',
        'Stay hydrated',
        'Follow low-fat diet',
        'Get vaccinated for hepatitis',
        'Monitor liver function'
    ],
    'malaria': [
        'Use mosquito nets',
        'Apply insect repellent',
        'Take antimalarial prophylaxis',
        'Eliminate standing water',
        'Seek prompt treatment'
    ],
    'chicken pox': [
        'Get vaccinated',
        'Avoid scratching lesions',
        'Practice good hygiene',
        'Isolate to prevent spread',
        'Use soothing lotions'
    ],
    'dengue fever': [
        'Use mosquito repellent',
        'Wear long clothing',
        'Eliminate breeding sites',
        'Stay hydrated',
        'Seek medical care for fever'
    ],
    'typhoid fever': [
        'Get vaccinated',
        'Drink safe water',
        'Wash hands frequently',
        'Avoid raw foods',
        'Complete antibiotic course'
    ],
    'hepatitis a': [
        'Get vaccinated',
        'Practice hand hygiene',
        'Drink safe water',
        'Avoid raw shellfish',
        'Monitor liver health'
    ],
    'hepatitis b': [
        'Get vaccinated',
        'Practice safe sex',
        'Avoid sharing needles',
        'Screen regularly',
        'Follow antiviral therapy'
    ],
    'alcoholic hepatitis': [
        'Stop alcohol consumption',
        'Follow low-fat diet',
        'Take prescribed medications',
        'Monitor liver function',
        'Seek support for alcoholism'
    ],
    'tuberculosis': [
        'Complete antibiotic course',
        'Cover mouth when coughing',
        'Ensure good ventilation',
        'Get screened if exposed',
        'Maintain nutrition'
    ],
    'common cold': [
        'Wash hands frequently',
        'Avoid close contact',
        'Stay hydrated',
        'Rest adequately',
        'Use symptom relief medications'
    ],
    'pneumonia': [
        'Get vaccinated',
        'Avoid smoking',
        'Practice hand hygiene',
        'Seek prompt treatment',
        'Maintain nutrition'
    ],
    'hemorrhoids': [
        'Eat high-fiber diet',
        'Stay hydrated',
        'Avoid straining during bowel movements',
        'Use topical treatments',
        'Exercise regularly'
    ],
    'myocardial infarction': [
        'Control cholesterol',
        'Exercise regularly',
        'Avoid smoking',
        'Monitor blood pressure',
        'Take aspirin if prescribed'
    ],
    'varicose veins': [
        'Exercise regularly',
        'Avoid prolonged standing',
        'Wear compression stockings',
        'Maintain healthy weight',
        'Elevate legs'
    ],
    'hypothyroidism': [
        'Take thyroid medication',
        'Monitor thyroid levels',
        'Eat iodine-rich foods',
        'Avoid goitrogenic foods',
        'Exercise regularly'
    ],
    'hyperthyroidism': [
        'Follow medication regimen',
        'Monitor thyroid function',
        'Avoid excess iodine',
        'Manage stress',
        'Eat balanced diet'
    ],
    'hypoglycemia': [
        'Eat regular meals',
        'Monitor blood sugar',
        'Carry glucose tablets',
        'Avoid excessive alcohol',
        'Exercise with snacks'
    ],
    'osteoarthritis': [
        'Maintain healthy weight',
        'Exercise regularly',
        'Use joint supports',
        'Take pain relievers as prescribed',
        'Seek physiotherapy'
    ],
    'rheumatoid arthritis': [
        'Take prescribed medications',
        'Exercise regularly',
        'Rest during flares',
        'Eat anti-inflammatory diet',
        'Monitor joint health'
    ],
    'benign paroxysmal positional vertigo': [
        'Perform Epley maneuver',
        'Avoid sudden head movements',
        'Stay hydrated',
        'Use caution when standing',
        'Consult a specialist'
    ],
    'acne vulgaris': [
        'Wash face gently',
        'Avoid touching face',
        'Use non-comedogenic products',
        'Follow prescribed treatments',
        'Eat balanced diet'
    ],
    'urinary tract infection': [
        'Drink plenty of water',
        'Urinate frequently',
        'Practice good hygiene',
        'Avoid irritants (e.g., caffeine)',
        'Seek antibiotics if needed'
    ],
    'psoriasis': [
        'Moisturize skin regularly',
        'Avoid triggers (e.g., stress)',
        'Use prescribed treatments',
        'Get moderate sunlight',
        'Monitor for joint pain'
    ],
    'impetigo': [
        'Keep skin clean',
        'Avoid scratching',
        'Use prescribed antibiotics',
        'Wash bedding/towels',
        'Isolate to prevent spread'
    ],
    'lung cancer': [
        'Avoid smoking/secondhand smoke',
        'Get screened if high-risk',
        'Maintain healthy diet',
        'Exercise regularly',
        'Monitor respiratory symptoms'
    ],
    'breast cancer': [
        'Perform regular self-exams',
        'Get mammograms as recommended',
        'Maintain healthy weight',
        'Limit alcohol',
        'Exercise regularly'
    ],
    'colorectal cancer': [
        'Get regular screenings',
        'Eat high-fiber diet',
        'Limit red/processed meats',
        'Exercise regularly',
        'Avoid smoking'
    ],
    'prostate cancer': [
        'Get PSA screenings',
        'Eat healthy diet',
        'Exercise regularly',
        'Limit fatty foods',
        'Monitor urinary symptoms'
    ],
    'stomach cancer': [
        'Eat high-fiber diet',
        'Limit salty/smoked foods',
        'Avoid smoking/alcohol',
        'Get screened if high-risk',
        'Monitor digestive symptoms'
    ],
    'coronary artery disease': [
        'Control cholesterol',
        'Exercise regularly',
        'Avoid smoking',
        'Monitor blood pressure',
        'Eat heart-healthy diet'
    ],
    'copd': [
        'Quit smoking',
        'Use inhalers as prescribed',
        'Get vaccinated',
        'Avoid air pollutants',
        'Perform breathing exercises'
    ],
    'chronic kidney disease': [
        'Control blood pressure',
        'Monitor blood sugar',
        'Follow low-sodium diet',
        'Stay hydrated',
        'Avoid NSAIDs'
    ],
    'alzheimers disease': [
        'Engage in mental exercises',
        'Exercise regularly',
        'Eat Mediterranean diet',
        'Maintain social connections',
        'Monitor memory changes'
    ]
}


disease_map = {
    'lung cancer': (10, True, ['Pembrolizumab', 'Cisplatin', 'Carboplatin', 'Paclitaxel']),  
    'myocardial infarction': (10, True, ['Aspirin', 'Clopidogrel', 'Metoprolol', 'Atorvastatin']), 
    'brain hemorrhage': (10, True, ['Mannitol', 'Nimodipine', 'Phenytoin', 'Levetiracetam']), 
    'breast cancer': (9, True, ['Tamoxifen', 'Trastuzumab', 'Doxorubicin', 'Cyclophosphamide']),  
    'colorectal cancer': (9, True, ['Fluorouracil', 'Oxaliplatin', 'Cetuximab', 'Leucovorin']),  
    'prostate cancer': (9, True, ['Leuprolide', 'Bicalutamide', 'Abiraterone', 'Docetaxel']),  
    'stomach cancer': (9, True, ['Fluorouracil', 'Cisplatin', 'Trastuzumab', 'Capecitabine']), 
    'coronary artery disease': (9, True, ['Atorvastatin', 'Aspirin', 'Metoprolol', 'Nitroglycerin']),  
    'hiv/aids': (8, False, ['Tenofovir', 'Emtricitabine', 'Dolutegravir', 'Efavirenz']),  
    'tuberculosis': (8, False, ['Isoniazid', 'Rifampin', 'Pyrazinamide', 'Ethambutol']),  
    'pneumonia': (8, False, ['Amoxicillin', 'Azithromycin', 'Levofloxacin', 'Doxycycline']),  
    'copd': (8, False, ['Tiotropium', 'Salmeterol', 'Ipratropium', 'Budesonide']),  
    'chronic kidney disease': (8, True, ['Losartan', 'Furosemide', 'Erythropoietin', 'Sevelamer']),  
    'hepatitis b': (7, False, ['Tenofovir', 'Entecavir', 'Lamivudine', 'Peginterferon Alfa']),          
    'alcoholic hepatitis': (7, False, ['Prednisolone', 'Pentoxifylline', 'N-Acetylcysteine', 'N/A']), 
    'malaria': (7, False, ['Artemether-Lumefantrine', 'Chloroquine', 'Quinine', 'Doxycycline']),  
    'dengue fever': (7, False, ['Acetaminophen', 'N/A', 'N/A', 'N/A']),  
    'typhoid fever': (7, False, ['Ceftriaxone', 'Azithromycin', 'Ciprofloxacin', 'N/A']),  
    'alzheimers disease': (7, False, ['Donepezil', 'Memantine', 'Rivastigmine', 'Galantamine']),  
    'type 2 diabetes': (6, False, ['Metformin', 'Sitagliptin', 'Insulin Glargine', 'Empagliflozin']), 
    'hypertension': (6, False, ['Lisinopril', 'Amlodipine', 'Hydrochlorothiazide', 'Losartan']), 
    'bronchial asthma': (6, False, ['Albuterol', 'Budesonide', 'Montelukast', 'Fluticasone']),  
    'rheumatoid arthritis': (6, True, ['Methotrexate', 'Adalimumab', 'Hydroxychloroquine', 'Leflunomide']),  
    'gastroenteritis': (5, False, ['Loperamide', 'Ondansetron', 'Ciprofloxacin', 'N/A']), 
    'peptic ulcer': (5, True, ['Omeprazole', 'Amoxicillin', 'Clarithromycin', 'Ranitidine']),  
    'hepatitis a': (5, False, ['Supportive Care', 'N/A', 'N/A', 'N/A']), 
    'hypoglycemia': (5, False, ['Glucose Tablets', 'Glucagon', 'Dextrose', 'N/A']),
    'chronic cholestasis': (5, True, ['Ursodeoxycholic Acid', 'Cholestyramine', 'Rifampin', 'N/A']),  
    'osteoarthritis': (4, True, ['Acetaminophen', 'Ibuprofen', 'Duloxetine', 'Hyaluronic Acid']), 
    'hypothyroidism': (4, False, ['Levothyroxine', 'Liothyronine', 'N/A', 'N/A']),  
    'hyperthyroidism': (4, True, ['Methimazole', 'Propylthiouracil', 'Carbimazole', 'N/A']),   
    'psoriasis': (4, False, ['Calcipotriene', 'Betamethasone', 'Methotrexate', 'Adalimumab']),  
    'urinary tract infection': (4, False, ['Nitrofurantoin', 'Trimethoprim-Sulfamethoxazole', 'Fosfomycin', 'Ciprofloxacin']),  
    'jaundice': (4, False, ['Ursodeoxycholic Acid', 'Phenobarbital', 'N/A', 'N/A']),  
    'cervical spondylosis': (3, True, ['Ibuprofen', 'Acetaminophen', 'Cyclobenzaprine', 'N/A']),  
    'varicose veins': (3, True, ['Diosmin', 'N/A', 'N/A', 'N/A']),  
    'migraine': (3, False, ['Sumatriptan', 'Propranolol', 'Topiramate', 'Ibuprofen']),  
    'benign paroxysmal positional vertigo': (3, False, ['Meclizine', 'Dimenhydrinate', 'Betahistine', 'N/A']),
    'drug allergy': (3, False, ['Epinephrine', 'Diphenhydramine', 'Prednisone', 'N/A']),
    'gerd': (3, False, ['Omeprazole', 'Ranitidine', 'Antacids', 'Domperidone']),
    'chicken pox': (2, False, ['Acyclovir', 'Calamine', 'Diphenhydramine', 'N/A']),  
    'hemorrhoids': (2, True, ['Hydrocortisone', 'Lidocaine', 'Witch Hazel', 'N/A']), 
    'impetigo': (2, False, ['Mupirocin', 'Fusidic Acid', 'Cephalexin', 'N/A']),  
    'allergic rhinitis': (1, False, ['Loratadine', 'Cetirizine', 'Fluticasone', 'N/A']), 
    'common cold': (1, False, ['Pseudoephedrine', 'Dextromethorphan', 'Guaifenesin', 'N/A']),  
    'acne vulgaris': (1, False, ['Benzoyl Peroxide', 'Clindamycin', 'Tretinoin', 'Adapalene']),  
    'fungal infection': (1, False, ['Clotrimazole', 'Fluconazole', 'Terbinafine', 'N/A'])  
}

from fpdf import FPDF
import base64
from datetime import datetime

def generate_pdf(report_fields, report_values):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Disease Prediction Report", ln=True, align='C')
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt=f"Generated on: {now}", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    for field, value in zip(report_fields, report_values):
        pdf.multi_cell(0, 10, txt=f"{field}: {value}", align='L')

    return pdf.output(dest='S').encode('latin1')


def get_disease_info(disease):
    
    result = {
        'precautions': [],
        'risk_score': None,
        'requires_surgery': None,
        'drugs': []
    }
    
    if disease in disease_advice:
        result['precautions'] = disease_advice[disease]
        
    if disease in disease_map:
        risk_score, requires_surgery, drugs = disease_map[disease]
        result['risk_score'] = risk_score
        result['requires_surgery'] = requires_surgery
        result['drugs'] = drugs
    
    return result

if st.button("Diagnose Disease"):
    predicted_disease = predict(
        age, sex,
        symptom1, symptom2, symptom3,
        symptom4, symptom5, symptom6, symptom7, symptom8,
        symptom9, symptom10, symptom11, symptom12, symptom13,
        symptom14, symptom15, symptom16, symptom17
    )

    st.success(f"Predicted Disease: **{predicted_disease}**")

    symptom_list = [s for s in [symptom1, symptom2, symptom3, symptom4, symptom5, symptom6, symptom7, symptom8,
                                symptom9, symptom10, symptom11, symptom12, symptom13, symptom14, symptom15,
                                symptom16, symptom17] if s and s != 'None']

    disease_info = get_disease_info(predicted_disease)

    report_fields = ["Age", "Sex", "Symptoms", "Prediction"]
    report_values = [age, sex, ", ".join(symptom_list) if symptom_list else "None", predicted_disease]

    if disease_info['risk_score'] is not None:
        report_fields.append("Risk Score")
        report_values.append(disease_info['risk_score'])

    if disease_info['requires_surgery'] is not None:
        report_fields.append("Requires Surgery")
        report_values.append("Yes" if disease_info['requires_surgery'] else "No")

    if disease_info['drugs']:
        report_fields.append("Common Drugs")
        report_values.append(", ".join(disease_info['drugs']))

    if disease_info['precautions']:
        report_fields.append("Precautions")
        report_values.append(", ".join(disease_info['precautions']))

    report_df = pd.DataFrame({
    "Field": report_fields,
    "Value": [str(v) for v in report_values]  
})

    st.subheader("Final Report")
    st.table(report_df)

    pdf_bytes = generate_pdf(report_fields, report_values)
    b64 = base64.b64encode(pdf_bytes).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="report.pdf">📄 Download Report as PDF</a>'
    st.markdown(href, unsafe_allow_html=True)


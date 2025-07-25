import pandas as pd
import joblib
import os
from pathlib import Path
import numpy as np

countries = [
    ("United States of America", "United States of America"),
    ("Philippines", "Philippines"),
    ("United Kingdom of Great Britain and Northern Ireland", "United Kingdom of Great Britain and Northern Ireland"),
    ("Australia", "Australia"),
    ("Netherlands", "Netherlands"),
    ("Germany", "Germany"),
    ("Sweden", "Sweden"),
    ("France", "France"),
    ("Nigeria", "Nigeria"),
    ("Spain", "Spain"),
    ("South Africa", "South Africa"),
    ("Brazil", "Brazil"),
    ("Portugal", "Portugal"),
    ("Italy", "Italy"),
    ("Bangladesh", "Bangladesh"),
    ("Argentina", "Argentina"),
    ("Canada", "Canada"),
    ("Switzerland", "Switzerland"),
    ("Sri Lanka", "Sri Lanka"),
    ("Lithuania", "Lithuania"),
    ("Serbia", "Serbia"),
    ("Cyprus", "Cyprus"),
    ("Latvia", "Latvia"),
    ("Russian Federation", "Russian Federation"),
    ("Greece", "Greece"),
    ("Austria", "Austria"),
    ("Norway", "Norway"),
    ("Singapore", "Singapore"),
    ("Turkey", "Turkey"),
    ("Croatia", "Croatia"),
    ("India", "India"),
    ("Iran, Islamic Republic of...", "Iran, Islamic Republic of..."),
    ("Poland", "Poland"),
    ("Kosovo", "Kosovo"),
    ("Nepal", "Nepal"),
    ("Slovenia", "Slovenia"),
    ("China", "China"),
    ("Belgium", "Belgium"),
    ("Denmark", "Denmark"),
    ("Hungary", "Hungary"),
    ("Republic of Korea", "Republic of Korea"),
    ("Viet Nam", "Viet Nam"),
    ("Israel", "Israel"),
    ("Ukraine", "Ukraine"),
    ("Finland", "Finland"),
    ("Nomadic", "Nomadic"),
    ("Dominican Republic", "Dominican Republic"),
    ("Isle of Man", "Isle of Man"),
    ("Estonia", "Estonia"),
    ("Morocco", "Morocco"),
    ("Egypt", "Egypt"),
    ("The former Yugoslav Republic of Macedonia", "The former Yugoslav Republic of Macedonia"),
    ("Uzbekistan", "Uzbekistan"),
    ("Indonesia", "Indonesia"),
    ("Ireland", "Ireland"),
    ("Georgia", "Georgia"),
    ("Benin", "Benin"),
    ("Japan", "Japan"),
    ("Venezuela, Bolivarian Republic of...", "Venezuela, Bolivarian Republic of..."),
    ("Bahrain", "Bahrain"),
    ("Tajikistan", "Tajikistan"),
    ("Luxembourg", "Luxembourg"),
    ("Czech Republic", "Czech Republic"),
    ("Malta", "Malta"),
    ("Belarus", "Belarus"),
    ("Montenegro", "Montenegro"),
    ("Bosnia and Herzegovina", "Bosnia and Herzegovina"),
    ("Zimbabwe", "Zimbabwe"),
    ("Armenia", "Armenia"),
    ("Romania", "Romania"),
    ("Malaysia", "Malaysia"),
    ("Saudi Arabia", "Saudi Arabia"),
    ("Albania", "Albania"),
    ("Tunisia", "Tunisia"),
    ("Kenya", "Kenya"),
    ("United Arab Emirates", "United Arab Emirates"),
    ("Afghanistan", "Afghanistan"),
    ("Pakistan", "Pakistan"),
    ("Djibouti", "Djibouti"),
    ("Ethiopia", "Ethiopia"),
    ("Paraguay", "Paraguay"),
    ("New Zealand", "New Zealand"),
    ("Panama", "Panama"),
    ("Zambia", "Zambia"),
    ("Nicaragua", "Nicaragua"),
    ("Jordan", "Jordan"),
    ("Slovakia", "Slovakia"),
    ("Bulgaria", "Bulgaria"),
    ("Uruguay", "Uruguay"),
    ("Peru", "Peru"),
    ("Trinidad and Tobago", "Trinidad and Tobago"),
    ("Hong Kong (S.A.R.)", "Hong Kong (S.A.R.)"),
    ("Thailand", "Thailand"),
    ("Ecuador", "Ecuador"),
    ("Mexico", "Mexico"),
    ("Republic of Moldova", "Republic of Moldova"),
    ("Colombia", "Colombia"),
    ("Guatemala", "Guatemala"),
    ("Mongolia", "Mongolia"),
    ("Chile", "Chile"),
    ("Cuba", "Cuba"),
    ("Kazakhstan", "Kazakhstan"),
    ("Azerbaijan", "Azerbaijan"),
    ("Bolivia", "Bolivia"),
    ("Iceland", "Iceland"),
    ("Algeria", "Algeria"),
    ("Syrian Arab Republic", "Syrian Arab Republic"),
    ("Somalia", "Somalia"),
    ("Jamaica", "Jamaica"),
    ("Myanmar", "Myanmar"),
    ("El Salvador", "El Salvador"),
    ("Honduras", "Honduras"),
    ("Yemen", "Yemen"),
    ("Qatar", "Qatar"),
    ("Lebanon", "Lebanon"),
    ("South Korea", "South Korea"),
    ("Ghana", "Ghana"),
    ("Taiwan", "Taiwan"),
    ("Mauritius", "Mauritius"),
    ("Maldives", "Maldives"),
    ("Kuwait", "Kuwait"),
    ("Cambodia", "Cambodia"),
    ("Brunei Darussalam", "Brunei Darussalam"),
    ("Fiji", "Fiji"),
    ("Kyrgyzstan", "Kyrgyzstan"),
    ("Turkmenistan", "Turkmenistan"),
    ("Uganda", "Uganda"),
    ("Oman", "Oman"),
    ("Andorra", "Andorra"),
    ("Palestine", "Palestine"),
    ("Madagascar", "Madagascar"),
    ("United Republic of Tanzania", "United Republic of Tanzania"),
    ("Cameroon", "Cameroon"),
    ("Barbados", "Barbados"),
    ("Gabon", "Gabon"),
    ("Mali", "Mali"),
    ("Palau", "Palau"),
    ("Malawi", "Malawi"),
    ("Belize", "Belize"),
    ("Togo", "Togo"),
    ("Guyana", "Guyana"),
    ("Angola", "Angola"),
    ("Sierra Leone", "Sierra Leone"),
    ("Namibia", "Namibia"),
    ("Botswana", "Botswana"),
    ("Rwanda", "Rwanda"),
    ("Mauritania", "Mauritania"),
    ("Monaco", "Monaco"),
    ("Swaziland", "Swaziland"),
    ("Lesotho", "Lesotho"),
    ("Mozambique", "Mozambique"),
    ("Dominica", "Dominica"),
    ("Liechtenstein", "Liechtenstein"),
    ("Niger", "Niger"),
    ("Saint Kitts and Nevis", "Saint Kitts and Nevis"),
    ("Suriname", "Suriname"),
    ("Senegal", "Senegal"),
    ("Burundi", "Burundi"),
    ("Cape Verde", "Cape Verde"),
    ("Sudan", "Sudan"),
    ("Guinea", "Guinea"),
    ("Libyan Arab Jamahiriya", "Libyan Arab Jamahiriya"),
    ("Burkina Faso", "Burkina Faso"),
    ("Antigua and Barbuda", "Antigua and Barbuda"),
    ("Democratic Republic of the Congo", "Democratic Republic of the Congo"),
    ("Republic of North Macedonia", "Republic of North Macedonia"),
    ("Congo, Republic of the...", "Congo, Republic of the..."),
    ("Samoa", "Samoa"),
    ("Haiti", "Haiti")
]

EdLevel = [
    ("Bachelor’s degree (B.A., B.S., B.Eng., etc.)", "Bachelor’s degree (B.A., B.S., B.Eng., etc.)"),
    ("Master’s degree (M.A., M.S., M.Eng., MBA, etc.)", "Master’s degree (M.A., M.S., M.Eng., MBA, etc.)"),
    ("Some college/university study without earning a degree", "Some college/university study without earning a degree"),
    ("Primary/elementary school", "Primary/elementary school"),
    ("Professional degree (JD, MD, Ph.D, Ed.D, etc.)", "Professional degree (JD, MD, Ph.D, Ed.D, etc.)"),
    ("Associate degree (A.A., A.S., etc.)", "Associate degree (A.A., A.S., etc.)"),
    ("Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)", "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)"),
    ("Something else", "Something else"),
]

OrgSize = [
    "fewer than 10",
    "10 to 19",
    "Small",
    "20 to 99",
    "100 to 499",
    "Medium",
    "500 to 999",
    "1,000 or more",
    "Large",
]

remote_work = [
    ("Hybrid", "Hybrid"),
    ("Remote", "Remote"),
    ("In-person", "In-person")
]

Industry = [
    "Tech",
    "Finance",
    "Manufacturing/Supply Chain",
    "Services",
    "Healthcare",
    "Government",
    "Other",
]
dev_types = [
    ("Senior Executive (C-Suite, VP, etc.)", "Senior Executive (C-Suite, VP, etc.)"),
    ("Developer, back-end", "Developer, back-end"),
    ("Developer, front-end", "Developer, front-end"),
    ("Developer, full-stack", "Developer, full-stack"),
    ("System administrator", "System administrator"),
    ("Developer, desktop or enterprise applications", "Developer, desktop or enterprise applications"),
    ("Developer, QA or test", "Developer, QA or test"),
    ("Designer", "Designer"),
    ("Data scientist or machine learning specialist", "Data scientist or machine learning specialist"),
    ("Data or business analyst", "Data or business analyst"),
    ("Security professional", "Security professional"),
    ("Educator", "Educator"),
    ("Research & Development role", "Research & Development role"),
    ("Other (please specify):", "Other (please specify):"),
    ("Developer, mobile", "Developer, mobile"),
    ("Database administrator", "Database administrator"),
    ("Developer, embedded applications or devices", "Developer, embedded applications or devices"),
    ("Student", "Student"),
    ("Engineer, data", "Engineer, data"),
    ("Hardware Engineer", "Hardware Engineer"),
    ("Product manager", "Product manager"),
    ("Academic researcher", "Academic researcher"),
    ("Developer, game or graphics", "Developer, game or graphics"),
    ("Cloud infrastructure engineer", "Cloud infrastructure engineer"),
    ("Engineering manager", "Engineering manager"),
    ("Developer Experience", "Developer Experience"),
    ("Project manager", "Project manager"),
    ("DevOps specialist", "DevOps specialist"),
    ("Engineer, site reliability", "Engineer, site reliability"),
    ("Blockchain", "Blockchain"),
    ("Developer Advocate", "Developer Advocate"),
    ("Scientist", "Scientist"),
    ("Marketing or sales professional", "Marketing or sales professional"),
    ("Developer, AI", "Developer, AI"),
    ("Data engineer", "Data engineer")
]
employment = [
    ("Employed, full-time", "Employed, full-time"),
    ("Employed, part-time", "Employed, part-time"),
    ("Independent contractor, freelancer, or self-employed", "Independent contractor, freelancer, or self-employed"),
    ("Not employed, but looking for work", "Not employed, but looking for work"),
    ("Not employed, and not looking for work", "Not employed, and not looking for work"),
    ("Student, full-time", "Student, full-time"),
    ("Student, part-time", "Student, part-time"),
    ("Retired", "Retired"),
    ("I prefer not to say", "I prefer not to say")
]
programming_languages = [
    ("Ada", "Ada"),
    ("ALGOL", "ALGOL"),
    ("Assembly", "Assembly"),
    ("AWK", "AWK"),
    ("Bash", "Bash"),
    ("BASIC", "BASIC"),
    ("C", "C"),
    ("C#", "C#"),
    ("C++", "C++"),
    ("Clojure", "Clojure"),
    ("COBOL", "COBOL"),
    ("CoffeeScript", "CoffeeScript"),
    ("Crystal", "Crystal"),
    ("D", "D"),
    ("Dart", "Dart"),
    ("Delphi", "Delphi"),
    ("Elixir", "Elixir"),
    ("Elm", "Elm"),
    ("Erlang", "Erlang"),
    ("F#", "F#"),
    ("Forth", "Forth"),
    ("Fortran", "Fortran"),
    ("Go", "Go"),
    ("Groovy", "Groovy"),
    ("Haskell", "Haskell"),
    ("HTML/CSS", "HTML/CSS"),
    ("Java", "Java"),
    ("JavaScript", "JavaScript"),
    ("Julia", "Julia"),
    ("Kotlin", "Kotlin"),
    ("Lisp", "Lisp"),
    ("Lua", "Lua"),
    ("MATLAB", "MATLAB"),
    ("Nim", "Nim"),
    ("Objective-C", "Objective-C"),
    ("OCaml", "OCaml"),
    ("Pascal", "Pascal"),
    ("Perl", "Perl"),
    ("PHP", "PHP"),
    ("PowerShell", "PowerShell"),
    ("Prolog", "Prolog"),
    ("Python", "Python"),
    ("R", "R"),
    ("Ruby", "Ruby"),
    ("Rust", "Rust"),
    ("Scala", "Scala"),
    ("Scheme", "Scheme"),
    ("Scratch", "Scratch"),
    ("Shell", "Shell"),
    ("Smalltalk", "Smalltalk"),
    ("SQL", "SQL"),
    ("Swift", "Swift"),
    ("Tcl", "Tcl"),
    ("TypeScript", "TypeScript"),
    ("VB.NET", "VB.NET"),
    ("VBA", "VBA"),
    ("Verilog", "Verilog"),
    ("VHDL", "VHDL"),
    ("Visual Basic", "Visual Basic"),
    ("Zig", "Zig")
]


# Define paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
MODEL_PATH = BASE_DIR / 'models' / 'LinearRegression_salary_predictor.pkl'
FEATURES_PATH = BASE_DIR / 'models'/'LinearRegression_feature_names.pkl'

# Load the trained model
model = joblib.load(MODEL_PATH)

# List of expected features (based on your training data)
# FEATURES = [
    # 'YearsCode', 'YearsCodePro',
    # 'Country_United States', 'Country_India', 'Country_Other',  # Example one-hot encoded countries
    # 'DevType_Full-stack developer', 'DevType_Back-end developer',  # Example roles
    # 'EdLevel_Bachelor’s degree', 'EdLevel_Master’s degree',
    # 'RemoteWork_Remote', 'RemoteWork_Hybrid',
    # 'LanguageHaveWorkedWith_Python', 'LanguageHaveWorkedWith_JavaScript',  # Example languages
# ]
#
FEATURES = joblib.load(FEATURES_PATH)
breakpoint()  # Debugging breakpoint

def preprocess_input(data, feature_names):
    """Preprocess user input to match model features."""
    # Initialize DataFrame with zeros for all expected features
    input_df = pd.DataFrame(0, index=[0], columns=feature_names)

    # Numerical features
    input_df['num__YearsCode'] = float(data.get('years_code_pro', 0))  # Assume YearsCode = YearsCodePro
    input_df['num__YearsCodePro'] = float(data.get('years_code_pro', 0))
    input_df['num__NumLanguages'] = len(data.get('languages', [])) if data.get('languages') else 0
    input_df['num__NumTools'] = 1 if data.get('ai_select', '') in ['Yes', 'No, but I plan to soon'] else 0
    input_df['num__NumPlatforms'] = len(data.get('platforms', [])) if data.get('platforms') else 0

    # Language features
    for lang in data.get('languages', []):
        col = f'num__Language_{lang}'
        if col in feature_names:
            input_df[col] = 1

    # Database features
    for db in data.get('databases', []):
        col = f'num__Database_{db}'
        if col in feature_names:
            input_df[col] = 1

    # Platform features
    for plat in data.get('platforms', []):
        col = f'num__Platform_{plat}'
        if col in feature_names:
            input_df[col] = 1

    # Categorical features
    country = data.get('country', 'Other')
    if country and f'cat__Country_{country}' in feature_names:
        input_df[f'cat__Country_{country}'] = 1
    else:
        input_df['cat__Country_Other'] = 1

    dev_type = data.get('dev_type', 'Other')
    if dev_type and f'cat__DevType_{dev_type}' in feature_names:
        input_df[f'cat__DevType_{dev_type}'] = 1

    ed_level = data.get('ed_level', 'Other')
    if ed_level and f'cat__EdLevel_{ed_level}' in feature_names:
        input_df[f'cat__EdLevel_{ed_level}'] = 1

    remote_work = data.get('remote_work', 'In-person')
    if remote_work and f'cat__RemoteWork_{remote_work}' in feature_names:
        input_df[f'cat__RemoteWork_{remote_work}'] = 1

    org_size = data.get('org_size', '10,000 or more employees')
    if org_size and f'cat__OrgSize_{org_size}' in feature_names:
        input_df[f'cat__OrgSize_{org_size}'] = 1

    return input_df

def predict_salary(data, ):
    """Predict salary from user input."""
    input_df = preprocess_input(data, FEATURES)
    breakpoint()
    print(f"Input DataFrame for prediction:\n{input_df}")
    log_salary = model.predict(input_df)[0]
    salary = round(np.expm1(log_salary), 2)  # Reverse log-transform
    return salary

import pandas as pd
import joblib
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

platforms = [
    ('Amazon Web Services (AWS)', 'Amazon Web Services (AWS)'),
    ('Cloudflare','Cloudflare'),
    ('Colocation', 'Colocation'),
    ('Digital Ocean', 'Digital Ocean'),
    ('Firebase', 'Firebase'),
    ('Fly.io', 'Fly.io'),
    ('Google Cloud', 'Google Cloud'),
    ('Heroku', 'Heroku'),
    ('Hetzner', 'Hetzner'),
    ('IBM Cloud Or Watson', 'IBM Cloud Or Watson'),
    ('Linode, now Akamai', 'Linode, now Akamai'),
    ('Managed Hosting', 'Managed Hosting'),
    ('Microsoft Azure', 'Microsoft Azure'),
    ('Netlify', 'Netlify'),
    ('OpenShift', 'OpenShift'),
    ('OpenStack', 'OpenStack'),
    ('Oracle Cloud Infrastructure (OCI)', 'Oracle Cloud Infrastructure (OCI)'),
    ('OVH', 'OVH'),
    ('Render', 'Render'),
    ('Scaleway', 'Scaleway'),
    ('Vercel', 'Vercel'),
    ('VMware', 'VMware'),
    ('Vultr', 'Vultr')
]
industries = [
    ("Tech", "Tech"),
    ("Finance", "Finance"),
    ("Manufacturing/Supply Chain", "Manufacturing/Supply Chain"),
    ("Services", "Services"),
    ("Healthcare", "Healthcare"),
    ("Government", "Government"),
    ("Other", "Other"),
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

def get_region(country):
    if country in  [
    'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cape Verde', 'Cameroon',
    'Central African Republic', 'Chad', 'Comoros', 'Democratic Republic of the Congo', 'Congo', 'Congo, Republic of the...',
    'Côte d’Ivoire', "Côte d'Ivoire", 'Djibouti', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia',
    'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia',
    'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Mozambique', 'Namibia',
    'Niger', 'Nigeria', 'Rwanda', 'São Tomé and Príncipe', 'Senegal', 'Seychelles',
    'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Swaziland', 'Tanzania',
    'Togo', 'Uganda', 'United Republic of Tanzania', 'Zambia', 'Zimbabwe'
]:
        return 'Sub Saharan Africa'
    elif country in ['United States of America', 'Canada']:
        return 'North America'
    elif country in ['United Kingdom of Great Britain and Northern Ireland', 'Germany', 'France', 'Italy', 'Netherlands', 'Sweden', 'Switzerland',
                     'Austria', 'Belgium', 'Portugal', 'Spain', 'Greece', 'Norway', 'Iceland', 'Denmark', 'Finland', 'Ireland', 'Estonia',
                     'Lithuania', 'Latvia', 'Luxembourg', 'Monaco']:
        return 'Western & Northern Europe'
    elif country in ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Dominican Republic', 'Ecuador',
                    'El Salvador', 'Guatemala', 'Honduras', 'Mexico', 'Nicaragua', 'Panama', 'Paraguay', 'Peru', 'Uruguay', 'Venezuela', 'Venezuela, Bolivarian Republic of...']:
        return 'Latin America'
    elif country in ['India', 'Pakistan', 'Bangladesh', 'Sri Lanka', 'Indonesia', 'Nepal', 'Viet Nam', 'Philippines', 'Malaysia', 'Thailand',
                     'Bhutan', 'Maldives', 'Brunei', 'Cambodia', 'Laos', 'Myanmar']:
        return 'South & Southeast Asia'
    elif country in ['China', 'Japan', 'South Korea', 'Taiwan', 'Hong Kong', 'Hong Kong (S.A.R.)', 'Singapore', 'Macau', 'Mongolia', 'North Korea', 'Republic of Korea', "Democratic People's Republic of Korea"]:
        return 'East Asia'
    elif country in ['Armenia', 'Albenia','Armenia', 'Montenegro', 'Poland', 'Ukraine', 'Romania', 'Russian Federation', 'Serbia', 'Czech Republic', 'Slovakia', 'Hungary', 'Moldova', 'Republic of Moldova', 'Belarus', 'Bulgaria', 'Kosovo', 'Slovenia',
                    'Croatia', 'Bosnia and Herzegovina', 'Kazakhstan', 'Uzbekistan', 'Albania', 'Azerbaijan', 'Kyrgyzstan', 'Afghanistan', 'Georgia']:
        return 'Eastern Europe & Central Asia'
    elif country in ['Australia', 'New Zealand', 'Fiji']:
        return 'Oceania'
    elif country in ['Antigua and Barbuda', 'Bahamas', 'Barbados', 'Dominica', 'Grenada', 'Haiti', 'Jamaica', 'Saint Kitts and Nevis',
                     'Saint Lucia', 'Saint Vincent', 'The Grenadines', 'Trinidad and Tobago', 'Anguilla', 'Aruba', 'British Virgin Islands',
                     'Cayman Islands', 'Puerto Rico']:
        return 'Caribbean'
    elif country in ['Algeria', 'Egypt', 'Libya', 'Morocco', 'Tunisia', 'Mauritania',
                 'Bahrain', 'Iran, Islamic Republic of...', 'Iraq', 'Israel', 'Jordan', 'Kuwait', 'Lebanon', 'Oman', 'Cyprus',
                 'Turkey', 'Georgia', 'Malta', 'Palestine', 'Qatar', 'Saudi Arabia', 'Syria', 'Syrian Arab Republic', 'United Arab Emirates', 'Yemen']:
        return 'MENA'
    else:
        return 'Other'


# Define paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
MODEL_PATH_LGBM = BASE_DIR / 'models' / 'lightgbm_model.pkl'
FEATURES_PATH_LGBM = BASE_DIR / 'models'/'lightgbm_params.pkl'


# Load the trained model
lgbm_model = joblib.load(MODEL_PATH_LGBM)

LGBM_FEATURES = joblib.load(FEATURES_PATH_LGBM)


feature_info = joblib.load('models/feature_info.pkl')
preprocessor = joblib.load('models/lightgbm_preprocessor.pkl')

def preprocess_input(data):
    """Preprocess user input to match model features."""

    # Initialize output dictionary with default values
    input_df = {col: 0 for col in feature_info['numerical_features']}
    input_df.update({col: None for col in feature_info['onehot_features'] + feature_info['target_encoded_features']})

    # Numerical features
    input_df['YearsCode'] = float(data.get('years_code_pro', 0))  # Assume YearsCode = YearsCodePro
    input_df['YearsCodePro'] = float(data.get('years_code_pro', 0))
    input_df['NumLanguages'] = len(data.get('programming_languages', []))
    input_df['NumTools'] = 1 if data.get('ai_select', '') in ['Yes', 'No, but I plan to soon'] else 0
    input_df['NumPlatforms'] = len(data.get('platforms', []))

    # Language features
    #Dynamic Lang_* features
    for lang in data.get('programming_languages', []):
        lang_col = f"Lang_{lang}"
        if lang_col in feature_info['numerical_features']:
            input_df[lang_col] = 1

    # Dynamic Platform_* features
    for platform in data.get('platforms', []):
        platform_col = f"Platform_{platform}"
        if platform_col in feature_info['numerical_features']:
            input_df[platform_col] = 1

    ed_level_mapping = {
        'Bachelor’s degree (B.A., B.S., B.Eng., etc.)': 3,
        'Master’s degree (M.A., M.S., M.Eng., MBA, etc.)': 4,
        "Some college/university study without earning a degree": 3,
        "Associate degree (A.A., A.S., etc.)": 3,
        "Primary/elementary school": 0,
        "Professional degree (JD, MD, Ph.D, Ed.D, etc.)": 5,
        "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)": 1,
        "Something else": 0
    }
    input_df['EdLevel_Encoded'] = ed_level_mapping.get(data.get('ed_level', ''), 0)

    years_coding = float(data.get('years_of_coding', 0))
    if years_coding <= 5:
        input_df['ExperienceLevel'] = 'Junior'
    elif years_coding <= 10:
        input_df['ExperienceLevel'] = 'Mid'
    else:
        input_df['ExperienceLevel'] = 'Senior'

    # Categorical features
    country = data.get('countries', '')
    if country:
        input_df['Region'] = get_region(country)

    remote_work = data.get('remote_work', 'Unknown')
    if remote_work:
        input_df['RemoteWork_Simplified'] = remote_work

    dev_type = data.get('dev_type', 'Other')
    if dev_type:
        input_df['DevType'] = dev_type

    all_features = (feature_info['numerical_features'] +
                    feature_info['onehot_features'] +
                    feature_info['target_encoded_features'])

    input_df = pd.DataFrame([input_df], columns=all_features)
    return input_df

def predict_salary(data, ):
    """Predict salary from user input."""
    input_df = preprocess_input(data)
    print(f"Input DataFrame for prediction:\n{input_df}")
    log_salary = lgbm_model.predict(input_df)[0]
    salary = round(np.expm1(log_salary), 2)  # Reverse log-transform
    return salary

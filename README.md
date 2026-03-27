# PhishNet

PhishNet is a simple AI-powered Command Line Interface (CLI) application built to detect college-specific phishing, "fake internship" scams, and urgent "account suspension" spam. It uses Natural Language Processing (TF-IDF) and Naive Bayes Classification to read emails and determine if they are safe or dangerous.

## Why PhishNet? (Project Motivation)
Over the past semester, our college's Placement Office has sent out repeated, urgent warnings regarding sophisticated fake internship emails targeting students. These scams bypass standard Gmail/Outlook filters because they mimic legitimate university communications, often preying on students’ financial insecurities with subject lines like:
- *"URGENT: Paid Research Assistant Position Available within your Department"* or 
- *"NASSCOM Job Bridge Drive: Immediate Action Required"*
- *"We are announcing a unique 3-month Job Driven Program offered by UNLOX, in collaboration with leading MNCs"*

Once the student clicks the link or replies, scammers ask for SSNs or charge a fake "onboarding fee." PhishNet was built specifically to solve this problem by training an isolated Machine Learning model exclusively on the linguistic patterns of these very targeted campus scams.

## Features
- **Machine Learning Integration**: Built from scratch using `scikit-learn` and `pandas`.
- **Custom Campus Dataset**: Trained on a dataset specifically tailored to college environments
- **Interactive CLI Menu**: An intuitive text-based interface built with pure Python.
- **Model Persistence**: Uses `pickle` to save and load models without needing to retrain them every time.

## Project Structure
```text
PhishNet/
├── data/
│   └── dataset.csv                 <- Training dataset (auto-generated on first run)
├── models/                         <- Saved AI components
│   ├── model.pkl                   <- Trained Naive Bayes classifier
│   └── vectorizer.pkl              <- Trained TF-IDF vectorizer
├── app.py                          <- Main CLI App (Run this!)
└── train_model.py                  <- Training script (Run this once first!)
```

## Complete Setup Instructions

### Step 1: Clone or Download this repository
Download the `ZIP` file from GitHub and extract it, or open your terminal/command prompt and run:
```bash
git clone <your-repository-link>
cd PhishNet
```

### Step 2: Create a Virtual Environment
This ensures the Python libraries you install don't interfere with the rest of your computer.
```bash
# Create the environment
python -m venv venv
# Activate it (Windows)
venv\Scripts\activate
# Activate it (Mac/Linux)
source venv/bin/activate
```

### Step 3: Install Dependencies
The application relies on Pandas (for reading data) and Scikit-Learn (for AI processing). Ensure your virtual environment is activated, then run:
```bash
pip install pandas scikit-learn
```

## How to Use the Application

### 1. Training the Model
Before you can analyze emails, the AI needs to build its "brains." You must run the training script first. This will automatically generate a starter `dataset.csv` in the `data/` folder, train the AI, and save its serialized weight matrices into the `models/` folder.
```bash
python train_model.py
```
<img width="721" height="185" alt="image" src="https://github.com/user-attachments/assets/374bca08-52a5-461f-92c9-9a883632080a" />

### 2. Running the Application
Once trained, launch the main interactive terminal app.
```bash
python app.py
```
<img width="557" height="247" alt="image-1" src="https://github.com/user-attachments/assets/a524fbdb-56cb-4a73-9d0f-33d6d7b95526" />


## Adding Your Own Data 
To make the AI smarter (such as adding the exact emails your Placement Office warned you about):
1. Open the auto-generated `data/dataset.csv` file in Notepad or Excel.
2. Add a new row. Paste the spam message entirely in the first column, and place a `1` in the label column. Let `0` represent normal, safe emails.
3. Save the file and simply run `python train_model.py` again! The model will instantly update itself and learn from your new examples.

## Screenshots
<img width="1896" height="659" alt="image-2" src="https://github.com/user-attachments/assets/a1a83ea5-c872-4cf1-b9d7-883582ca81fa" />

<img width="864" height="436" alt="image-3" src="https://github.com/user-attachments/assets/e9893af8-3e0f-40e8-859c-af671b146971" />

<img width="796" height="365" alt="image-4" src="https://github.com/user-attachments/assets/dd64420c-ad6e-4bbf-91f9-d1a02016e4e5" />

<img width="712" height="208" alt="image-5" src="https://github.com/user-attachments/assets/1e66385f-88ee-4288-923a-ed17c4ad0de3" />




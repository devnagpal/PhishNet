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
![alt text](image.png)

### 2. Running the Application
Once trained, launch the main interactive terminal app.
```bash
python app.py
```

## Adding Your Own Data 
To make the AI smarter (such as adding the exact emails your Placement Office warned you about):
1. Open the auto-generated `data/dataset.csv` file in Notepad or Excel.
2. Add a new row. Paste the spam message entirely in the first column, and place a `1` in the label column. Let `0` represent normal, safe emails.
3. Save the file and simply run `python train_model.py` again! The model will instantly update itself and learn from your new examples.
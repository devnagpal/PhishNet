import pickle
import os

class CampusMailCLI:
    def __init__(self):
        self.model_dir="models"
        self.model=None
        self.vectorizer=None

    def get_multi_line_input(self):
        print("\nEnter the email text line by line. Press Enter twice (an empty line) to analyze.")
        print("-"*82)
        lines=[]
        while True:
            try:
                line=input("> ")
            except EOFError:
                break
            if line.strip()=="":
                if not lines:
                    print("Please enter at least one line of text.")
                    continue
                else:
                    break
            lines.append(line)
        return " ".join(lines)

    def view_stats(self):
        stats_path=os.path.join(self.model_dir,"stats.txt")
        print("="*15,"Model Statistics","="*15)
        try:
            with open(stats_path,"r") as f:
                print(f.read().strip())
        except FileNotFoundError:
            print("No testing data found. Did you run the training script?")
        print("="*41)

    def view_help(self):
        print("="*15,"Help / About","="*15)
        print("PhishNet is an AI-powered Text Classifier.")
        print("It uses Natural Language Processing (TF-IDF) and Naive Bayes")
        print("to detect targeted campus scams, such as:")
        print("- Fake 'Paid Internships'")
        print("- Fake scholarship offers")
        print("- Urgent 'Account Suspension' phishing")
        print("="*41)

    def run(self):
        print("\n"+"="*41)
        print(" "*10,"Welcome to PhishNet!")
        print("="*41)
        if not self.load_model():
            return
        while True:
            print("-"*15,"Main Menu","-"*15)
            print("1. Analyze an Email")
            print("2. View Model Stats")
            print("3. Help / About")
            print("4. Exit")
            print("-"*41)
            choice=input("Enter Your Choice (1-4): ")
            if choice=="1":
                self.analyze_email()
            elif choice=="2":
                self.view_stats()
            elif choice=="3":
                self.view_help()
            elif choice=="4":
                print("Exiting PhishNet. Stay safe out there!")
                break
            else:
                print("Invalid input! Please enter a number between 1 and 4.")

if __name__=="__main__":
    app=CampusMailCLI()
    app.run()
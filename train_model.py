import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import os

class SpamDetectorTrainer:
    def __init__(self):
        self.data_dir="data"
        self.model_dir="models"
        self.data_path=os.path.join(self.data_dir,"dataset.csv")

    def create_dummy_data(self):
        """Creates a simple mock dataset if none exists."""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        if not os.path.exists(self.data_path):
            print("Creating dummy dataset...")
            # 1=Scam,0=Safe
            data=[
                ("Hey, are we still meeting tomorrow for the group project?", 0),
                ("URGENT: Campus Placement Drive. Send SSN and $50 fee for registration.", 1),
                ("Your university library books are overdue. Please return them.", 0),
                ("PAID INTERNSHIP! Click here to apply now.", 1),
                ("Professor Smith's AI class is canceled today.", 0),
                ("Important: Verify your student email to avoid account suspension.", 1),
                ("Campus event: Free pizza at the quad at 12 PM. See you there!", 0),
                ("Congratulations! You won the college scholarship. Claim here!!", 1),
                ("Can you send me the notes from the last machine learning lecture?", 0),
                ("WORK FROM DORM! Part time position available. Contact this strange email.", 1)
            ]
            df=pd.DataFrame(data, columns=["text","label"])
            df.to_csv(self.data_path, index=False)
            print(f"Dataset saved to {self.data_path}")

    def load_data(self):
        print("Loading data...")
        df=pd.read_csv(self.data_path)
        df=df.dropna()
        return df["text"],df["label"]

    def train_and_save(self):
        self.create_dummy_data()
        X,y=self.load_data()
        
        print("Splitting data into training and testing sets...")
        X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

        print("Converting text to numbers (TF-IDF)...")
        vectorizer=TfidfVectorizer(stop_words='english')
        X_train_vec=vectorizer.fit_transform(X_train)
        X_test_vec=vectorizer.transform(X_test)

        print("Training Naive Bayes model...")
        model=MultinomialNB(alpha=0.1)
        model.fit(X_train_vec,y_train)

        predictions=model.predict(X_test_vec)
        accuracy=accuracy_score(y_test,predictions)
        print(f"Model trained! Testing Accuracy: {accuracy * 100:.2f}%")

        if not os.path.exists(self.model_dir):
            os.makedirs(self.model_dir)
        print("Saving model and vectorizer to models/ directory...")
        with open(os.path.join(self.model_dir,"model.pkl"),"wb") as f:
            pickle.dump(model,f)
        with open(os.path.join(self.model_dir,"vectorizer.pkl"),"wb") as f:
            pickle.dump(vectorizer,f)
        with open(os.path.join(self.model_dir,"stats.txt"),"w") as f:
            f.write(f"Testing Accuracy: {accuracy*100:.2f}%\n")
            f.write(f"Total Emails Trained On: {len(X)}\n")
        print("Training complete! You can now run the CLI app.")

if __name__=="__main__":
    print("="*15,"Model Training Phase","="*15)
    trainer=SpamDetectorTrainer()
    trainer.train_and_save()
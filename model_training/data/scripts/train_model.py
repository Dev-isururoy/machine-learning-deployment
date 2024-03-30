import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

def train_model(input_file, output_model):
    # Load the dataset
    df = pd.read_csv(input_file)

    # Split the dataset into features and target variable
    X = df.drop(columns=['loan_approval'])
    y = df['loan_approval']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Feature scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Initialize and train the model
    model = LogisticRegression()
    model.fit(X_train_scaled, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test_scaled)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    conf_matrix = confusion_matrix(y_test, y_pred)
    print("\nConfusion Matrix:")
    print(conf_matrix)

    report = classification_report(y_test, y_pred)
    print("\nClassification Report:")
    print(report)

    # Save the trained model
    joblib.dump(model, output_model)
    print("\nModel training completed. Trained model saved to", output_model)

if __name__ == "__main__":
    input_file = 'path/to/your/train.csv'  # Update with input file path
    output_model = 'path/to/your/trained_model.pkl'  # Update with  output model path
    train_model(input_file, output_model)

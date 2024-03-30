import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(input_file, output_file):
    # Load the dataset
    df = pd.read_csv(input_file)

    # Perform data preprocessing steps
    # Example: Handling missing values by imputing with mean or median
    # df['age'].fillna(df['age'].median(), inplace=True)

    # Example: Feature scaling
    scaler = StandardScaler()
    numerical_features = df.select_dtypes(include=['int64', 'float64']).columns
    df[numerical_features] = scaler.fit_transform(df[numerical_features])

    # Save the preprocessed data to a new file
    df.to_csv(output_file, index=False)
    print("Data preprocessing completed. Preprocessed data saved to", output_file)

if __name__ == "__main__":
    input_file = 'path/to/your/input.csv'  # Update with input file path
    output_file = 'path/to/your/output.csv'  # Update with  output file path
    preprocess_data(input_file, output_file)

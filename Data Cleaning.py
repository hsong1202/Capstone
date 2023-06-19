#standardizing the dataset
import pandas as pd
import os

# Directory containing your Excel files
xlsx_folder = 'C:/Users/habum/Code/SavvyCoders/Capstone/Dataset'
csv_folder = 'C:/Users/habum/Code/SavvyCoders/Capstone/Dataset/CSV/'

# Iterate over each file in the directory
for filename in os.listdir(xlsx_folder):
    if filename.endswith('.xlsx'):
        # Construct the file path
        file_path = os.path.join(xlsx_folder, filename)
        csv_path = os.path.join(csv_folder, os.path.splitext(filename)[0] + '.csv')
        
        # Read the Excel file and skip the first row
        data = pd.read_excel(file_path, skiprows=1)
        
        # Write the modified DataFrame back to a CSV file
        data.to_csv(csv_folder, index=False)

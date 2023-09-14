# Flask App for Data Processing and Exploratory Data Analysis

**Author**: Sachin Lodhi
**Repository**: [GitHub Repository](https://github.com/sachinlodhi/RA_assignment)

## Overview

This Flask application is designed to perform four main tasks on a dataset provided in CSV or XLS format:

1. **Upload**: Allows users to upload a CSV or XLS file.
2. **Extract**: Extracts serial numbers from a specified column.
3. **Map**: Maps serial numbers to a 5-digit unique ID.
4. **Remove**: Removes personal information such as email, name, etc., from the original dataset.
5. **EDA**: Performs Exploratory Data Analysis (EDA) on the dataset and generates graphs for visualizing relationships, dependencies, and correlations between attributes.



## Usage

1.clone the repository to your local machine: 
```bash
git clone https://github.com/sachinlodhi/RA_assignment
```
2. Navigate to the project directory using the following command:
```bash
cd RA_assignment
```
## Requirements

3.Before running the application, ensure you have the necessary dependencies installed. You can install them using `pip` with the following command:

```bash
pip install -r requirements.txt
```
## Run app
4.Run the app using following command:
```python
python3 app.py
```
and if that throws any error then use following command:
```python
python app.py
```
## Access the application
Open your web browser and access the app at http://localhost:5000.

Follow the on-screen instructions to perform the tasks on your dataset.

Input Data
Make sure your dataset is in CSV or XLS format. When uploading the file, specify the column containing serial numbers.

Output
The app will generate a processed dataset with personal information removed and EDA graphs in the output directory.


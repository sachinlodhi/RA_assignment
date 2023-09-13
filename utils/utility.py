import pandas as pd
import re
import  os
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OrdinalEncoder
import warnings
import math
import shutil
import glob

warnings.filterwarnings('ignore')

read_func ={
    ".csv" : pd.read_csv,
    ".xls" : pd.read_excel
}

# attributes exteractor
def load_file(filename):
    global read_func
    df = read_func[filename[-4:]](filename)
    return df.columns.tolist()


# This filters out the attrs automatically(predefined)
def filter_personal(attributes):
    words_to_filter = ["email", "name", "cwid"]

    # Create a regex pattern that matches any of the words in a case-insensitive manner
    pattern = re.compile(r"|".join(re.escape(word) for word in words_to_filter), re.IGNORECASE)

    # Filter the list to get elements that match the pattern
    filtered_list = [word for word in l if pattern.search(word)]

    # Print the filtered list
    print(filtered_list)


# this function removes the columns baesd on the user selection
def filter_cols(all_cols, selected_cols):
    return [i for i in all_cols if i not in selected_cols]

# assigning the serial number and creating another file to save record
def mapping(filename):
    df = read_func[filename[-4:]](filename)

    # Assigning Serial Nos to all the recs
    df["Sr. No."] = pd.Series(range(1, len(df)+1))
    main_df_len = len(df)

    # creating 5 digits unique numbers

    unique_digits = set()
    while True:
        unique_digits.add(random.randint(10000, 99999))
        if len(unique_digits) == main_df_len:
            break

    map_df = pd.DataFrame()
    map_df["Sr. No."] = df["Sr. No."]
    map_df["uid"] = list(unique_digits)
    _, file_extension = os.path.splitext(filename)
    map_df.to_csv(_ +"_mapping.csv",index=False)
    print("Success Mapping")



# plotting the graphs
def graphs(file_path):
    try:
        os.makedirs("static/graphs/"+"frequency_graphs")
        os.makedirs("static/graphs/" + "scatter_graphs")
    except:
        pass
    save_dir = "static/graphs"
    '''Plotting frequency graph for the dataframe and dsiplaying image'''
    df = read_func[file_path[-4:]](file_path)
    attributes_to_plot = list(df.columns.values)
    print(len(attributes_to_plot))
    num_rows = math.ceil(len(attributes_to_plot) / 5)
    num_cols = 5

    # Frequency graphs
    for i in attributes_to_plot:
        frequency_counts = df[i].value_counts().sort_index()
        plt.figure(figsize=(10, 6))  # Set the figure size
        frequency_counts.plot(kind='bar', color='skyblue')
        plt.xlabel('Unique Values')  # X-axis label
        plt.ylabel('Frequency')  # Y-axis label
        plt.title(f'Frequency Distribution of {i}')
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        # plt.show()  # Show the plot
        plt.savefig(save_dir+'/frequency_graphs/' +i+".png")
    print("Freq distr saved")
    freq_lis = glob.glob(save_dir+"/frequency_graphs/" + "*.png")

    # # scatter plot
    # Create a list to store the scatter plots
    scatter_plots = []

    # Loop through each attribute and create scatter plots
    for i, attribute in enumerate(attributes_to_plot):
        row = i // num_cols
        col = i % num_cols
        plt.figure(figsize=(10, 8))  # Set the figure size
        sns.scatterplot(x=attribute, y='Grade', data=df)
        plt.xlabel(attribute)
        plt.ylabel('Grade')
        plt.title(f'{attribute} vs. Grade')
        plt.xticks(rotation=45)  # Rotate x-axis labels if needed
        # Append the current plot to the list of scatter plots
        scatter_plots.append(plt)
        plt.savefig(save_dir + '/scatter_graphs/' + attribute + ".png")

    scatter_lis = glob.glob(save_dir + "/scatter_graph/" + "*.png")

    return [freq_lis, scatter_lis]







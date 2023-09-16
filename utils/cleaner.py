import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OrdinalEncoder
import warnings
import random
import researchpy as rp
import re

'''
receives the dataframe as the parameter and removes the columns
'''
def clean(rec):
    # removing the personal info columns : (Implemented in web with user input to choose the columns to remove)

    words_to_filter = ["email", "name", "cwid"]

    # Create a regex pattern that matches any of the words in a case-insensitive manner
    pattern = re.compile(r"|".join(re.escape(word) for word in words_to_filter), re.IGNORECASE)

    # Filter the list to get elements that match the pattern
    filtered_list = [word for word in words_to_filter if pattern.search(word)]

    # Print the filtered list
    # print(filtered_list)

    del_columns = ["Person Name", "Cwid", "Email"]
    rec.drop(columns=del_columns, inplace=True)

    # Checking and dropping the unique values cols as they are not helpful to find the relation
    # between them and grade
    single_val_cols = rec.columns[rec.nunique() == 1]
    # print(single_val_cols)
    # DRopping additional columns manually by checking them
    del_li = ["Expected Grad Term", "Major (Latest)", "EOP"]
    rec.drop(columns=del_li, inplace=True)
    rec.drop(columns=single_val_cols, inplace=True)
    # print("Columns Dropped")

    return rec




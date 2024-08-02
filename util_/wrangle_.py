# This utility file should alway go where the env file is.

# For funtion annotations
from binascii import a2b_qp
from typing import Union
from typing import Tuple

# Python libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Mac libraries
import os

# data visualization
import matplotlib.pyplot as plt
import seaborn as sns

# data separation/transformation
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# system manipulation
import os
import sys

# other
# import env
import warnings
warnings.filterwarnings("ignore")

################### LOADING FILES ##############################################
def save_original_data(df:pd.DataFrame, folder:str = "data", file_name:str = "original_data") -> str:
    """
    df: dataframe to save
    folder: folder name to save to
    file_name: file name to be assigned to the data
    """
    if not os.path.exists(f"./{folder}"):
        os.makedirs(folder)
        df.to_csv(f"./{folder}/00_{file_name}.csv", mode="w")
        return f"File {file_name} saved"
    else:
        df.to_csv(f"./{folder}/00_{file_name}.csv", mode="w")
        return f"File {file_name} saved"
    
# -----------------------------------------------------------------

# Remove encoding while loading csv data to python
def catch_encoding_errors_(fileName:str) -> pd.DataFrame:
    
    """
    parameters:
        fileName: csv file name. Should look like (file.csv)
    return:
        file dataframe with no encoding errors
    """
    
    # list of encodings to check for
    encodings = ['utf-8', 'latin-1', 'cp1252', 'utf-16']
    
    # check encodings and return dataframe
    for encoding in encodings:
        try:
            df = pd.read_csv(fileName, encoding=encoding, index_col=0)
            break
        except UnicodeDecodeError:
            print(f"Failed to decode with {encoding} encoding.")
    return df


################### PREP DATA ##############################################
# Save visuals
def save_visuals_(fig: plt.figure ,viz_name:str= "unamed_viz", folder_name:int= 0, ) -> str:
    """
    Goal: Save a single visual into the project visual folder
    parameters:
        fig: seaborn visual figure to be saved
        viz_name: name of the visual to save
        folder_name: interger (0-7)represanting the section you are on in the pipeline
            0: all other (defealt)
            1: univariate stats
            2: bivariate stats
            3: multivariate stats
            4: stats test
            5: modeling
            6: final report
            7: presantation
    return:
        message to user on save status
    """
    project_visuals = "./00_project_visuals"
    folder_selection = {
        0: "00_non_specific_viz",
        1: "01_univariate_stats_viz",
        2: "02_bivariate_stats_viz",
        3: "03_multivariate_stats_viz",
        4: "04_stats_test_viz",
        5: "05_modeling_viz",
        6: "06_final_report_viz",
        7: "07_presantation"
    }

    # return error if user input for folder selection is not found
    if folder_name not in list(folder_selection.keys()):
        return f"{folder_name} is not a valid option for a folder name."
    # when folder location is found in selections
    else:
        # Specify the path to the directory where you want to save the figure
        folder_name = folder_selection[folder_name]
        directory_path = f'{project_visuals}/{folder_name}/'

        # Create the full file path by combining the directory path and the desired file name
        file_path = os.path.join(directory_path, f'{viz_name}.png')

        if os.path.exists(project_visuals): # check if the main viz folder exists
            if not os.path.exists(directory_path): # check if the folder name already exists
                os.makedirs(directory_path)
                # Save the figure to the specified file path
                fig.canvas.print_figure(file_path)

            else:
                # Save the figure to the specified file path
                fig.canvas.print_figure(file_path)
        else:
            # create both the project vis folder and the specific section folder
            os.makedirs(project_visuals)
            os.makedirs(directory_path)

            # Save the figure to the specified file path
            fig.canvas.print_figure(file_path)
    
    return f"Visual successfully saved in folder: {folder_name}"

# -----------------------------------------------------------------
# Save the splited data into separate csv files
def save_split_data_(original_df:pd.DataFrame,encoded_scaled_df: pd.DataFrame, train:pd.DataFrame, validate:pd.DataFrame, test:pd.DataFrame, folder_path: str = "./00_project_data",
                     test_size:float = 0.2,stratify_col:str=None, random_state: int=95 ) -> str:
    """
    parameters:
        encoded_df: full project dataframe that contains the (encoded columns or scalling)
        train: training data set that has been split from the original
        validate: validation data set that has been split from the original
        test: testing data set that has been split from the original
        folder_path: folder path where to save the data sets

        Only apply to spliting the original_df in inside this function
            --> test_size:float = 0.2,stratify_col:str=None, random_state: int=95
    return:
        string to show succes of saving the data
    """
    # split original clearn no dumies data frame
    org_train_df, org_val_df, org_test_df = split_data_(df=original_df, test_size=test_size, stratify_col=stratify_col, random_state=random_state)


    # create new folder if folder don't aready exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        # save the dataframe with dummies in a csv for easy access
        original_df.to_csv(f"./{folder_path}/00_original_clean_no_dummies.csv", mode="w")

        # save the dataframe with dummies in a csv for easy access
        org_train_df.to_csv(f"./{folder_path}/01_original_clean_no_dummies_train.csv", mode="w")

        # save the dataframe with dummies in a csv for easy access
        encoded_scaled_df.to_csv(f"./{folder_path}/1-0_encoded_data.csv", mode="w")

        # save training data
        train.to_csv(f"./{folder_path}/1-1_training_data.csv", mode="w")

        # save validate
        validate.to_csv(f"./{folder_path}/1-2_validation_data.csv", mode="w")

        # Save test
        test.to_csv(f"./{folder_path}/1-3_testing_data.csv", mode="w")

    else:
        # save the dataframe with dummies in a csv for easy access
        original_df.to_csv(f"./{folder_path}/00_original_clean_no_dummies.csv", mode="w")

        # save the dataframe with dummies in a csv for easy access
        org_train_df.to_csv(f"./{folder_path}/01_original_clean_no_dummies_train.csv", mode="w")

        # save the dataframe with dummies in a csv for easy access
        encoded_scaled_df.to_csv(f"./{folder_path}/1-0_encoded_data.csv", mode="w")

        # save training data
        train.to_csv(f"./{folder_path}/1-1_training_data.csv", mode="w")

        # save validate
        validate.to_csv(f"./{folder_path}/1-2_validation_data.csv", mode="w")

        # Save test
        test.to_csv(f"./{folder_path}/1-3_testing_data.csv", mode="w")

    return "SIX data sets saved as .csv"


# -----------------------------------------------------------------
# Split the data into train, validate and train
def split_data_(df: pd.DataFrame, test_size: float =.2, validate_size: float =.2, stratify_col: str =None, random_state: int=95) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    '''
    parameters:
        df: pandas dataframe you wish to split
        test_size: size of your test dataset
        validate_size: size of your validation dataset
        stratify_col: the column to do the stratification on
        random_state: random seed for the data

    return:
        train, validate, test DataFrames
    '''
    # no stratification
    if stratify_col == None:
        # split test data
        train_validate, test = train_test_split(df, 
                                                test_size=test_size, 
                                                random_state=random_state)
        # split validate data
        train, validate = train_test_split(train_validate, 
                                           test_size=validate_size/(1-test_size),
                                            random_state=random_state)
    # stratify split
    else:
        # split test data
        train_validate, test = train_test_split(df,
                                                test_size=test_size,
                                                random_state=random_state, 
                                                stratify=df[stratify_col])
        # split validate data
        train, validate = train_test_split(train_validate, 
                                           test_size=validate_size/(1-test_size),
                                           random_state=random_state, 
                                           stratify=train_validate[stratify_col])
    return train, validate, test
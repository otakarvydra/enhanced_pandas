#This script includes the definition of enhanced Pandas DataFrame

#Imports
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class EnhancedPandas():

    def viewna_all(df):
        frame_missing = df.isna().sum().reset_index()
        frame_missing = frame_missing.rename(columns = {'index': 'column', 0 : 'missing count'})
        frame_missing['percentage missing'] = 100 * frame_missing['missing count'] / len(df)
        return frame_missing

    def viewna_column(df, column, *args):
        num = 0
        for arg in args:
            grouped_frame = df.groupby(str(arg))[str(column)].apply(lambda x: x.isnull().sum()).reset_index()
            grouped_renamed_frame = grouped_frame.rename(columns = {str(column) : str(column) + ' missing values'})
            print('\n')
            print(grouped_renamed_frame)

            #Plotting
            x = np.arange(len(args))
            plt.bar(x, grouped_renamed_frame[str(arg)], grouped_renamed_frame[str(column) + ' missing values'], label = ('group ' + str(num)))
            plt.xlabel('column values')
            plt.ylabel('missing values count')
            plt.title('missing values correlation investigation')
            plt.legend()
            plt.xticks(x, args)
            plt.show()         

    def check_missing_time_records(df, column, format):
        record_list = df[column].to_list()
        delta = datetime.strptime(record_list[1], format) - datetime.strptime(record_list[0], format)

        missing_values = []
        for i in (range(len(record_list))-1):
            value_1 = datetime.strptime(record_list[i], format)
            value_2 = datetime.strptime(record_list[i+1], format)
            if value_2 - value_1 != delta:
                missing_values.extend([record_list[i], record_list[i+1]])

        return df[df[column] in missing_values]
        
    def normalize(df, p_key, *args):
        new_frame = pd.DataFrame()
        new_frame[str(p_key)] = df[str(p_key)]
        for arg in args:
            new_frame[str(arg)] = df[str(arg)]
            df = df.drop(str(arg), axis = 1)
        new_frame = new_frame.drop_duplicates()
        if new_frame[str(p_key)].duplicated().sum() == 0:
            print('Normalization succesfull')
        else:
            print('Error, multiple values exist for the primary key')
        return new_frame
    
    def get_bool(df, column):
        bool_list = []
        lst = df[column].to_list()
        for element in lst:
            try:
                element = bool(element)
                bool_list.append(element)
            except:
                pass
        return bool_list
    
    def get_numeric(df, column):
        numeric_list = []
        lst = df[column].to_list()
        for element in lst:
            try:
                element = float(element)
                numeric_list.append(element)
            except:
                pass
        return numeric_list

    def check_empty_values(df, column):

        frame_unique = df.drop_duplicates(subset=column).reset_index()
        frame_sorted = frame_unique.sort_values(by=column).reset_index()
        frame_sorted[column] = frame_sorted[column].str.lower()
        column_list = frame_sorted[column].to_list()

        strings_check = ['empty', 'na', 'nan', 'none', 'unknown', 'not applicable']

        for string in strings_check:
            print('checking for string ' + string + ':')
        if string in column_list:
            print('Warning, the string ' + string + ' is present in the column ' + str(column))
        else:
            print(string + ' not present in the column')

    def sort_check(df, column):
        frame_unique = df.drop_duplicates(subset=column)
        frame_sorted = frame_unique.sort_values(by=column)
        print(frame_sorted.head(5))
        print(frame_sorted.tail(5))
        return frame_sorted
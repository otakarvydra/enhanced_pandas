#This script includes the definition of enhanced Pandas DataFrame

#Imports

from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

class EnhancedPandas():

    def viewna_all(df):
        frame_missing = df.isna().sum().reset_index()
        frame_missing = frame_missing.rename(columns = {'index': 'column', 0 : 'missing count'})
        frame_missing['percentage missing'] = 100 * frame_missing['missing count'] / len(df)

        return frame_missing

    def viewna_column(df, column, column_2):
        grouped_frame = df.groupby(str(column_2))[str(column)].apply(lambda x: x.isnull().sum()).reset_index()
        grouped_renamed_frame = grouped_frame.rename(columns = {str(column) : str(column) + ' missing values'})

        #Plotting
        plt.bar(grouped_renamed_frame[str(column_2)], grouped_renamed_frame[str(column) + ' missing values'])
        plt.xlabel('column values')
        plt.ylabel('missing values count')
        plt.title('missing values correlation investigation')
        plt.legend()

        return grouped_renamed_frame, plt          

    def check_missing_time_records(df, column, format):
        record_list = df[column].to_list()
        delta = datetime.strptime(record_list[1], format) - datetime.strptime(record_list[0], format)

        missing_values = []
        for i in (range(len(record_list)-1)):
            value_1 = datetime.strptime(record_list[i], format)
            value_2 = datetime.strptime(record_list[i+1], format)
            if value_2 - value_1 != delta:
                missing_values.extend([record_list[i], record_list[i+1]])

        return missing_values

    def normalize(df, p_key, *args):
        new_frame = pd.DataFrame()
        new_frame[p_key] = df[p_key]
        for arg in args:
            new_frame[arg] = df[arg]
        new_frame = new_frame.drop_duplicates()
        if new_frame[p_key].duplicated().sum() == 0:
            print('Normalization succesfull')
            for arg in args:
                df = df.drop(arg, axis = 1)
            return new_frame
        else:
            print('Error, multiple values exist for the primary key')
            return []
        
    def get_bool(df, column):
        bool_list = []
        lst = df[column].to_list()
        for element in lst:
            if element.lower() == 'true' or element.lower() == 'false':
                bool_list.append(element)
        
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
        frame_unique[column] = frame_unique[column].str.lower()
        column_list = frame_unique[column].to_list()

        strings_check = ['empty', 'na', 'nan', 'none', 'unknown', 'not applicable']
        strings_present = []
        for string in strings_check:
            if string in column_list:
                print('Warning, the string ' + string + ' is present in the column ' + str(column))
                strings_present.append(string)
        if strings_present == []:
            print('No empty strings present in the column')

    def sort_check(df, column):
        df = df[column]
        frame_unique = df.drop_duplicates()
        frame_sorted = frame_unique.sort_values()
        print('Head:')
        print(frame_sorted.head(5))
        print('Tail:')
        print(frame_sorted.tail(5))
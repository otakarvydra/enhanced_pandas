#This script includes the definition of enhanced Pandas DataFrame
import pandas as pd
import matplotlib.pyplot as plt

class EnhancedDataFrame():
    def __init__(self, orig_frame):
        self.frame = orig_frame

    def viewna(self):
        frame_missing = self.frame.isna().sum().reset_index()
        frame_missing = frame_missing.rename(columns = {'index': 'column', 0 : 'missing count'})
        frame_missing['percentage missing'] = 100 * frame_missing['missing count'] / len(self.frame)
        print(frame_missing)

    def viewna_column(self, column, *args):
        for arg in args:
            grouped_frame =self.frame.groupby(str(arg))[str(column)].apply(lambda x: x.isnull().sum()).reset_index()
            grouped_renamed_frame = grouped_frame.rename(columns = {str(column) : str(column) + ' missing values'})
            print('\n')
            print(grouped_renamed_frame)
            plt.bar(grouped_renamed_frame[str(arg)], grouped_renamed_frame[str(column) + ' missing values'])
            plt.xlabel('column values')
            plt.ylabel('missing values count')
            plt.title('missing values correlation investigation')
            plt.show()         

    def viewna_time(self, column, time_column):
        pass

    def normalize(self, p_key, *args):
        new_frame = pd.DataFrame()
        new_frame[str(p_key)] = self.frame[str(p_key)]
        for arg in args:
            new_frame[str(arg)] = self.frame[str(arg)]
            self.frame = self.frame.drop(str(arg), axis = 1)
        new_frame = new_frame.drop_duplicates()
        if new_frame[str(p_key)].duplicated().sum() == 0:
            print('Normalization succesfull')
        else:
            print('Error, multiple values exist for the primary key')
        return new_frame
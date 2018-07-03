#!venv/bin/python

import pandas as pd
import sys

pd.set_option('display.expand_frame_repr', False)

def trimAllColumns(df):
    trimStrings = lambda x: x.strip() if type(x) is str else x
    return df.applymap(trimStrings)


def main(args):
    if len(args) < 3:
        print('Invalid command, check READme file')
    else:
        try:
            file_path = args[2]
            # Reads data from csv file
            df = pd.read_csv(file_path, index_col=False, header=None)
        except FileNotFoundError as e:
            print('File does not exist')
        else:
            # Drops first column from data
            df.drop([df.columns[0]], inplace=True, axis=1)

            # Trims white space from the data fields
            df = trimAllColumns(df)

            # Sorts the data frame by last column
            sorted_df = df.sort_values(df.columns[2])

            # Resets row indices
            sorted_df.reset_index(drop=True, inplace=True)

            # Writes sorted data frame to file data0.csv
            sorted_df.to_csv('data0.csv', header=None, index=False)

            # Prints sorted data frame to console
            print(sorted_df)


main(sys.argv)

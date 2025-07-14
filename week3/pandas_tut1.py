import pandas as pd

def read_excel():
    file_path = "D:\Learning\SIC_June2025\week3\dataset\student-scores.xlsx"

    df = pd.read_excel(file_path)

    print(df.count())
    print(df.head())
    print(df.tail())

    # for _, row in df.iterrows():
    #     print(row[0], '  ', row[1])

    # for row in df.iterrows():
    #     print(row[1][0], row[1][1])

read_excel()
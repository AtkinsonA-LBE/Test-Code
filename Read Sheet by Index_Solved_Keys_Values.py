import pandas as pd
xlsx_url = r'c:\Users\charl\OneDrive\Documents\Python Projects\Finances\Demo Excel.xlsx'
worksheet = pd.ExcelFile(xlsx_url)
worksheets = worksheet.sheet_names

# Make column index while reading xlsx
for sheet_name in worksheets:    
    df = pd.read_excel(worksheet, sheet_name=[0, 1, 2], header=1)
    
    print(df.keys())
    print(df.values())
    
    break
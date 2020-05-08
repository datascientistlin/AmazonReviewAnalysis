# We can put the data clearning and manipulating functions in here.


import pandas as pd


def GetXLSSheetToDF(sheetname):
    return pd.read_excel('data\Google Trend.xlsx', sheet_name=sheetname, parse_dates=False)
	
def GetGoogleTrendsDF():
    sheets_in_xls = ['Momentum True Wireless 2','WH-1000XM3','AirPds Pro',' Noise Cancelling Headphones 70',
                    'Elite 75t','Soundcore Liberty Air 2','WF-1000XM3','Free','Soundcore Life Q20','Soundcore Liberty 2 Pro']
    
    df= GetXLSSheetToDF(sheets_in_xls[0])
    df.rename(columns={df.columns[1]: df.columns[1].replace(': (United States)','')}, inplace=True) 
    
    for sheetname in sheets_in_xls[1:]:
        next_df = GetXLSSheetToDF(sheetname)
        next_df.rename(columns={next_df.columns[1]: next_df.columns[1].replace(': (United States)','')}, inplace=True)
        df = pd.merge(df, next_df, how='outer',on='Week')
    df['Week'] = pd.to_datetime(df['Week'], format='%Y-%m-%d')
    # TODO: it might not be bad to set na values to 0, but isn't necessary for this data...
    return df
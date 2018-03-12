import os
import pandas as pd
import matplotlib.pyplot as plt


def symbol_to_path(symbol):
    # Return CSV file path given ticker symbol
    return os.path.join("Dataset/{}.csv".format(str(symbol)))



def get_data(symbols, dates):
    df = pd.DataFrame(index = dates)
    if 'SPY' not in symbols: # add SPY for reference, if absent
        symbols.insert(0,'SPY') 
    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date', parse_dates = True, usecols = ['Date', 'Adj Close'], na_values = ['nan'])
        df_temp = df_temp.rename(columns = {'Adj Close': symbol})
        df = df.join(df_temp)

        # Drop dates SPY did not trade
        if symbol == 'SPY':
            df = df.dropna(subset=['SPY'])
    return df



def plot_data(df, title = 'Stock Price'):
    
    # Plot stock prices
    ax = df.plot(title=title, fontsize=10,figsize = [18,14])
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    plt.show()
    
def plot_selected(df, columns, start_index, end_index):
    '''Plot the desire columns over desire dates'''
#     df = normalize_data(df)
    plot_data(df.loc[start_index:end_index, columns], title= 'Selected XX Stocks')
    df = df.loc[start_index:end_index, columns]

    
    
def normalize_data(df):
    return df/df.iloc[0,:]



def plot_selected_normalize(df, columns, start_index, end_index):
    
    # Normalize stock prices
    df = normalize_data(df)
    plot_data(df.loc[start_index:end_index,columns], title="Selected Data after Normalized")
    df = df.loc[start_index: end_index, columns]
    

    
def test_run():
    
    # Define a date range
    dates = pd.date_range('2009-01-05', '2018-02-14')
    
    # Choose stock symbol to read
    symbols = ['SPY','GOOG', 'DIS','AMZN','NKE', 'BRK-A','WFC','COST','MSFT']
    
    error_symbols = ['AAPL', 'NFLX','NVDA', 'SBUX']
    incomplete_symbols = ['FB','TSLA']


    # Get stock data
    df = get_data(symbols, dates)
    
    # error_symbols = ['AAPL']
    # if symbol == 'AAPL':
    #     df1 = pd.read_csv(symbol_to_path, index_col='Date', parse_dates = True, usecols = ['Date', 'Adj Close'], na_values = ['nan'])
    #     df1 = df1.rename(columns = {'Adj Close': symbol})
    #     cols = df1.columns
    #     for col in cols:
    #         if col == 'Volume':
    #             df1[col] = df[col].astype('int32')
    #         else:
    #             df[col] = df[col].astype(float)
    # return df1
    
            
    
    # Plot them out
    plot_selected_normalize(df, symbols, dates[0], dates[-1])

if __name__=='__main__':
    test_run()
    
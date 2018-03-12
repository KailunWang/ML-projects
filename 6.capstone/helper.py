import os
import pandas as pd
import matplotlib.pyplot as plt



# def plot_selected(df, columns, start_index, end_index):
#     '''Plot the desire columns over index values in the given range.'''
#     plot_data(df.loc[start_index:end_index, columns], title = 'Selected Data')
    

def plot_selected(df, columns, start_index, end_index):
    '''Plot the desire columns over desire dates'''
#     df = normalize_data(df)
    plot_data(df.loc[start_index:end_index, columns], title= 'Selected Stocks')
    df = df.loc[start_index:end_index, columns]
   


def symbol_to_path(symbol, base_dir = 'Dataset'):
    
    # Return CSV file path given ticker symbol
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))



def get_data(symbols, dates):
    
    # Read stock data(adjusted close) for given symbols from CSV files
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
        # THIS!!! It took me 4 days to figure out.
        df[symbol] = pd.to_numeric(df[symbol])

    return df



def plot_data(df, title = 'Stock Prices'):

    # Plot stock prices
    ax = df.plot(title =title, fontsize=12, figsize = (15, 8))
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()




def compute_daily_returns(df):
    
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:]/df[:-1].values) - 1
    
    # Set daily returns for row 0 to 0 
    daily_returns.iloc[0,:] = 0
    return daily_returns

    
    

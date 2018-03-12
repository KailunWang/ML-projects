
def compute_daily_returns(df):
    
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:]/df[:-1].values) - 1
    
    # Set daily returns for row 0 to 0 
    daily_returns.iloc[0,:] = 0
    return daily_returns

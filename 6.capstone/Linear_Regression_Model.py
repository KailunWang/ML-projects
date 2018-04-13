import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline 


from sklearn.cross_validation import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from helper import symbol_to_path


def Linear_Regression_Model():
    
    df = pd.read_csv(symbol_to_path('SPY'), index_col='Date', parse_dates=True, usecols=['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'])


    total = df['Adj Close'].count()
    
    # Starts from 2500, because data from too previous possibly cause overfitting
    X_train = df.iloc[2500:total-600, :-2].join(df.iloc[2500:total -600, -1]) # Add feature 'Volume' to training features
    #print df.iloc[0:1, :-2].join(df.iloc[0:1, -1])
    y_train = df.iloc[2500:total-600, -2]
    #print df.iloc[0:1, -2]
    
    # I can't test only on one day. Not only it gives me only one dot on a graph, but also not accurate
    X_test = df.iloc[total-599:, :-2].join(df.iloc[total-599:, -1])
    y_test = df.iloc[total-599:, -2]

    # Create linear regression object
    regr = linear_model.LinearRegression()
    
    # Train the model using the training sets
    regr.fit(X_train, y_train)
    
    # Query
    regr.predict(X_test)
    
    # Plot outputs
    print "\n"
    plt.figure(figsize=(8,6))
    plt.title("Actual Prices vs Predicted Prices")
    plt.xlabel("Prediction")
    plt.ylabel("Real prices")
    plt.scatter(regr.predict(X_test), y_test, color='blue')
    plt.show()
    
    
    # Score
    print "Score on training data"
    print "regr.score(X_train, y_train): ", regr.score(X_train, y_train), "\n"
    print "Score on testing data"
    print('regr.score(X_test, y_test): %.2f' % regr.score(X_test, y_test))
    print "Mean squared error: ", mean_squared_error(y_test, regr.predict(X_test)), "\n"


if __name__ == "__main__":
    Linear_Regression_Model()

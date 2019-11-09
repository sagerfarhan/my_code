import os
import pandas as pd


def symbol_to_path(symbol, base_dir="data"):
    return os.path.join(base_dir, '{}.csv'.format(str(symbol)))


def get_data(symbols, dates):
    # Read stock data (adjusted close) for given symbols from CSV files.
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                              parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':
            df = df.dropna(subset=['SPY'])

    return df


def test_run():
    dates = pd.date_range('2018-01-01', '2019-11-08')
    symbols = ['GOOG', 'IBM', 'GLD']

    df = get_data(symbols, dates)
    #print(df)
    # slice by row for 1 month
    print(df.ix['2019-01-01':'2019-01-31'])
    # slice by columnS symbols
    print(df[['GOOG', 'GLD']])

    # slice by row AND COLUMN
    print(df.ix['2019-01-01':'2019-01-15', ['SPY', 'IBM']])


if __name__ == "__main__":
    test_run()

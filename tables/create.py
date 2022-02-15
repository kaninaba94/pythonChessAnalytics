'''
TODO:
recreate the games DataFrame from games.json
columns:
    'Event', 'Site', 'Date', 'datetime', 'White', 'Black',
       'Result', 'UTCDate', 'UTCTime', 'WhiteElo', 'BlackElo',
       'WhiteRatingDiff', 'BlackRatingDiff', 'Variant', 'TimeControl', 'ECO',
       'Opening', 'Termination', 'moves', 'MyColor', 'OppColor', 'MyElo', 'OppElo',
       'MyRatingDiff'
'''

def create_mean_rating_diff_df():
    import pandas as pd
    import numpy as np
    df = pd.read_csv('C:\\Users\\knaraghi\\pycharm\\node_chess_analytics\\data\\time_series_df.csv')
    di = {}
    for num_games in sorted(df['Games'].unique()):
        di[num_games] = df[df['Games'] == num_games]['RatingDiff'].mean()

    mrddf = pd.DataFrame(data=np.array([list(di.keys()), list(di.values())]).T, columns=['Games', 'MeanRatingDiff'])
    mrddf['MeanRatingDiffByGames'] = mrddf['MeanRatingDiff'] / mrddf['Games']
    return mrddf

'''
create time series data frame with information such as
"Open", "Close", "Min", "Max", "RatingDiff", "RatingSpread", "Games"
'''

from common import create_time_series_structure
from tables.load import load_blitz_games

def create_time_series():
    # create empty time series
    columns = ['Open', 'Close', 'Min', 'Max', 'RatingDiff', 'RatingSpread']
    games = load_blitz_games()
    df = create_time_series_structure(games, columns)

    # populate df with elos
    for (i, day) in enumerate(df.index):
        day_games = games[games['Date'] == str(day)].sort_values(by='datetime')
        df.loc[day, 'Games'] = len(day_games)
        if len(day_games) > 0:
            df.loc[day, 'Open'] = day_games.iloc[0]['My Elo']
            df.loc[day, 'Close'] = day_games.iloc[-1]['My Elo'] + day_games.iloc[-1][f"{day_games.iloc[-1]['My Color']}RatingDiff"]
            df.loc[day, 'Min'] = day_games['My Elo'].min()
            df.loc[day, 'Max'] = day_games['My Elo'].max()
        else:
            df.loc[day, 'Open'] = df.loc[day, 'Close'] = df.loc[day, 'Min'] = df.loc[day, 'Max'] = df.iloc[i - 1]['Close']
        df.loc[day, 'RatingDiff'] = df.loc[day, 'Open'] - df.loc[day, 'Close']
        df.loc[day, 'RatingSpread'] = df.loc[day, 'Max'] - df.loc[day, 'Min']
    # df.reset_index(inplace=True)
    # df.columns.rename({'index': 'Period'})
    return df

if __name__=='__main__':
    mrddf = create_mean_rating_diff_df()
    mrddf.to_csv('C:\\Users\\knaraghi\\pycharm\\node_chess_analytics\\data\\mean_rating_diff_df.csv', index=False)
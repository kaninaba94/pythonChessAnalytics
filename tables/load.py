def load_blitz_games():
    import os
    import pandas as pd

    data_path = 'C:\\Users\\knaraghi\\pycharm\\node_chess_analytics\\data'
    with open(os.path.join(data_path, 'games.json')) as json_file:
        games = pd.read_csv(data_path + '\\games.csv')

    # only include Rated Blitz Games
    return games[games['Event'] == 'Rated Blitz game'].reset_index(drop=True)

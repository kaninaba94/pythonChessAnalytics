import matplotlib.pyplot as plt

from tables.load import load_blitz_games

games = load_blitz_games()


# TODO: find out about the slight ELO deviations before games 699, 1360, 1361, 1412, 1797, 1798, 1821, 2223, 2319, and 2320

def plot_games_and_elo(roll=15, elo_type='Max'):
    elo_types_allowed = ['Min', 'Max', 'Open', 'Close', 'RatingDiff', 'RatingSpread']
    if elo_type not in elo_types_allowed:
        raise ValueError(f"elo_type has to be one of {elo_types_allowed}")
    roll_param = roll

    # plot
    # plt.style.use('seaborn')
    fig, ax1 = plt.subplots()
    ax1.plot_date(df.index[roll_param - 1:], df[elo_type].rolling(roll_param).mean().dropna(), linestyle='solid', markersize=0, color='blue', linewidth=0.4)
    plt.gcf().autofmt_xdate()
    plt.xlabel('Day')
    ax1.set_ylabel(f"{elo_type}")
    ax2 = ax1.twinx()
    ax2.plot_date(df.index[roll_param - 1:], df.Games.rolling(roll_param).mean().dropna(), linestyle='solid', markersize=0, color='green', linewidth=0.4)
    ax2.set_ylabel('Games')
    ax1.set_title(f"rolling param = {roll_param}")
    # ax1.grid(linewidth=0.1)
    plt.tight_layout()
    # plt.savefig('C:\\Users\\knaraghi\\pycharm\\node_chess_analytics\\data\\games&max_elo.pdf', format='pdf')
    plt.show()


if __name__ == '__main__':
    df = plot_games_and_elo(roll=30, elo_type='Close')
    # plot_mean_rating_diff_over_games(df)

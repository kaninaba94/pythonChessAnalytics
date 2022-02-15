from tables.load import load_blitz_games

games = load_blitz_games()

vs_white = games[games['Opp Color'] == 'White']
vs_black = games[games['Opp Color'] == 'Black']

wins_vs_white = vs_white[vs_white['Result'] == '0-1']
wins_vs_black = vs_black[vs_black['Result'] == '1-0']

win_perc_vs_white = len(wins_vs_white) / len(vs_white)
win_perc_vs_black = len(wins_vs_black) / len(vs_black)

overall_win_perc = (win_perc_vs_black * len(vs_black) + win_perc_vs_white * len(vs_white)) / (len(games))


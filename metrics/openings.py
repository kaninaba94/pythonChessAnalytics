from tables.load import load_blitz_games
from pieces import win_perc_vs_white

games = load_blitz_games()

vs_white = games[games['Opp Color'] == 'White']
vs_black = games[games['Opp Color'] == 'Black']

vs_white_openings = vs_white.Opening.value_counts()
vs_black_openings = vs_black.Opening.value_counts()

win_perc_by_opening = {}
for opening in vs_white_openings.keys()[:5]:
    win_perc_by_opening[opening] = (len(vs_white[(vs_white.Opening == opening) & (vs_white['My Color'] == 'Black') & (vs_white['Result'] == '0-1')]) + \
                                   len(vs_white[(vs_white.Opening == opening) & (vs_white['My Color'] == 'White') & (vs_white['Result'] == '1-0')])) /\
                                   len(vs_white[vs_white.Opening == opening])



from tables.load import load_blitz_games
from common import user_name

games = load_blitz_games()

vs_stronger = games[((games['White'] == user_name) & (games['BlackElo'] > games['WhiteElo'])) | ((games['Black'] == user_name) & (games['WhiteElo'] > games['BlackElo']))]
vs_weaker = games[((games['White'] == user_name) & (games['BlackElo'] < games['WhiteElo'])) | ((games['Black'] == user_name) & (games['WhiteElo'] < games['BlackElo']))]
vs_equal = games[((games['White'] == user_name) & (games['BlackElo'] == games['WhiteElo'])) | ((games['Black'] == user_name) & (games['WhiteElo'] == games['BlackElo']))]

elo_gained_vs_stronger = vs_stronger[(vs_stronger['My Color'] == 'White')]['WhiteRatingDiff'].sum() + vs_stronger[(vs_stronger['My Color'] == 'Black')]['BlackRatingDiff'].sum()
elo_gained_vs_weaker = vs_weaker[(vs_weaker['My Color'] == 'White')]['WhiteRatingDiff'].sum() + vs_weaker[(vs_weaker['My Color'] == 'Black')]['BlackRatingDiff'].sum()
elo_gained_vs_equal = vs_equal[(vs_equal['My Color'] == 'White')]['WhiteRatingDiff'].sum() + vs_equal[(vs_equal['My Color'] == 'Black')]['BlackRatingDiff'].sum()

wins_vs_stronger = vs_stronger[((vs_stronger['My Color'] == 'White') & (vs_stronger['Result'] == '1-0')) | ((vs_stronger['My Color'] == 'Black') & (vs_stronger['Result'] == '0-1'))]
draws_vs_stronger = vs_stronger[vs_stronger['Result'] == '1/2-1/2']
losses_vs_stronger = vs_stronger[((vs_stronger['My Color'] == 'White') & (vs_stronger['Result'] == '0-1')) | ((vs_stronger['My Color'] == 'Black') & (vs_stronger['Result'] == '1-0'))]

# wins_vs_equal =
# draws_vs_equal =
# losses_vs_equal =

# wins_vs_weaker =
# draws_vs_weaker =
losses_vs_weaker = vs_weaker[((vs_weaker['My Color'] == 'White') & (vs_weaker['Result'] == '1-0')) | ((vs_weaker['My Color'] == 'Black') & (vs_weaker['Result'] == '0-1'))]

win_perc_vs_stronger = len(wins_vs_stronger) / len(vs_stronger)
draw_perc_vs_stronger = len(draws_vs_stronger) / len(vs_stronger)
loss_perc_vs_stronger = len(losses_vs_stronger) / len(vs_stronger)

# win_perc_vs_equal =
# draw_perc_vs_equal =
# loss_perc_vs_equal =

# win_perc_vs_weaker =
# draw_perc_vs_weaker =
loss_perc_vs_weaker = len(losses_vs_weaker) / len(vs_weaker)
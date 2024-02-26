import numpy
import simulation_method

def build_key():
    return {
    'Start': 0,
    'Home Team Scores 7 and Waits': 1,
    'Home Team Scores 3 and Waits': 2,
    'Home Team Scores 0 and Waits': 3,
    'Home Team Scores 7 and Wins': 4,
    'Home Team Scores 3 and Wins': 5,
    'Away Team Scores 7 and Ties': 6,
    'Away Team Scores 3 and Ties': 7,
    'Away Team Scores 0 and Ties': 8,
    'Away Team Scores 3 and Loses': 9,
    'Away Team Scores 0 and Loses': 10,
    'Away Team Scores 7 and Wins': 11,
    'Away Team Scores 3 and Wins': 12
}

def initialize_stochastic_matrix(size):
    results = [[0 for _1 in range(0,size)] for _2 in range(0,size)]
    for i in range(0,size):
        results[i][i] = 1
    return results

def initialize_state_matrix(size):
    results = [[0 for _ in range(0,size)]]
    results[0][0] = 1
    return results

def build_stochastic_matrix_for_1st_round_home_team_plays_it_safe(initialized_matrix):
    results = [[i for i in j] for j in initialized_matrix]
    key = build_key()
    results[key['Start']][key['Start']] = 0
    results[key['Start']][key['Home Team Scores 7 and Waits']] = 1/3
    results[key['Start']][key['Home Team Scores 3 and Waits']] = 1/3
    results[key['Start']][key['Home Team Scores 0 and Waits']] = 1/3
    return results

def build_stochastic_matrix_for_1st_round_away_team_plays_it_safe(initialized_matrix):
    results = [[i for i in j] for j in initialized_matrix]
    key = build_key()
    results[key['Home Team Scores 7 and Waits']][key['Home Team Scores 7 and Waits']] = 0
    results[key['Home Team Scores 7 and Waits']][key['Away Team Scores 7 and Ties']] = 1/3
    results[key['Home Team Scores 7 and Waits']][key['Away Team Scores 3 and Loses']] = 1/3
    results[key['Home Team Scores 7 and Waits']][key['Away Team Scores 0 and Loses']] = 1/3
    results[key['Home Team Scores 3 and Waits']][key['Home Team Scores 3 and Waits']] = 0
    results[key['Home Team Scores 3 and Waits']][key['Away Team Scores 7 and Wins']] = 1/3
    results[key['Home Team Scores 3 and Waits']][key['Away Team Scores 3 and Ties']] = 1/3
    results[key['Home Team Scores 3 and Waits']][key['Away Team Scores 0 and Loses']] = 1/3
    results[key['Home Team Scores 0 and Waits']][key['Home Team Scores 0 and Waits']] = 0
    results[key['Home Team Scores 0 and Waits']][key['Away Team Scores 7 and Wins']] = 1/3
    results[key['Home Team Scores 0 and Waits']][key['Away Team Scores 3 and Wins']] = 1/3
    results[key['Home Team Scores 0 and Waits']][key['Away Team Scores 0 and Ties']] = 1/3
    return results

def build_stochastic_matrix_for_other_rounds_home_team_plays_it_safe(initialized_matrix):
    results = [[i for i in j] for j in initialized_matrix]
    key = build_key()
    results[key['Away Team Scores 7 and Ties']][key['Away Team Scores 7 and Ties']] = 0
    results[key['Away Team Scores 7 and Ties']][key['Home Team Scores 7 and Wins']] = 1/3
    results[key['Away Team Scores 7 and Ties']][key['Home Team Scores 3 and Wins']] = 1/3
    results[key['Away Team Scores 7 and Ties']][key['Home Team Scores 0 and Waits']] = 1/3
    results[key['Away Team Scores 3 and Ties']][key['Away Team Scores 3 and Ties']] = 0
    results[key['Away Team Scores 3 and Ties']][key['Home Team Scores 7 and Wins']] = 1/3
    results[key['Away Team Scores 3 and Ties']][key['Home Team Scores 3 and Wins']] = 1/3
    results[key['Away Team Scores 3 and Ties']][key['Home Team Scores 0 and Waits']] = 1/3
    results[key['Away Team Scores 0 and Ties']][key['Away Team Scores 0 and Ties']] = 0
    results[key['Away Team Scores 0 and Ties']][key['Home Team Scores 7 and Wins']] = 1/3
    results[key['Away Team Scores 0 and Ties']][key['Home Team Scores 3 and Wins']] = 1/3
    results[key['Away Team Scores 0 and Ties']][key['Home Team Scores 0 and Waits']] = 1/3
    return results

def build_stochastic_matrix_for_other_rounds_away_team_plays_it_safe(initialized_matrix):
    results = [[i for i in j] for j in initialized_matrix]
    key = build_key()
    results[key['Home Team Scores 0 and Waits']][key['Home Team Scores 0 and Waits']] = 0
    results[key['Home Team Scores 0 and Waits']][key['Away Team Scores 7 and Wins']] = 1/3
    results[key['Home Team Scores 0 and Waits']][key['Away Team Scores 3 and Wins']] = 1/3
    results[key['Home Team Scores 0 and Waits']][key['Away Team Scores 0 and Ties']] = 1/3
    return results

def build_stochastic_matrix_for_1st_round_home_team_plays_aggressively(initialized_matrix):
    results = [[i for i in j] for j in initialized_matrix]
    key = build_key()
    results[key['Start']][key['Start']] = 0
    results[key['Start']][key['Home Team Scores 7 and Waits']] = 1/2
    results[key['Start']][key['Home Team Scores 3 and Waits']] = 0
    results[key['Start']][key['Home Team Scores 0 and Waits']] = 1/2
    return results

def build_stochastic_matrix_for_1st_round_away_team_plays_aggressively(initialized_matrix):
    results = [[i for i in j] for j in initialized_matrix]
    key = build_key()
    results[key['Home Team Scores 7 and Waits']][key['Home Team Scores 7 and Waits']] = 0
    results[key['Home Team Scores 7 and Waits']][key['Away Team Scores 7 and Ties']] = 1/2
    results[key['Home Team Scores 7 and Waits']][key['Away Team Scores 3 and Loses']] = 0
    results[key['Home Team Scores 7 and Waits']][key['Away Team Scores 0 and Loses']] = 1/2
    results[key['Home Team Scores 3 and Waits']][key['Home Team Scores 3 and Waits']] = 0
    results[key['Home Team Scores 3 and Waits']][key['Away Team Scores 7 and Wins']] = 1/2
    results[key['Home Team Scores 3 and Waits']][key['Away Team Scores 3 and Ties']] = 0
    results[key['Home Team Scores 3 and Waits']][key['Away Team Scores 0 and Loses']] = 1/2
    results[key['Home Team Scores 0 and Waits']][key['Home Team Scores 0 and Waits']] = 0
    results[key['Home Team Scores 0 and Waits']][key['Away Team Scores 7 and Wins']] = 1/2
    results[key['Home Team Scores 0 and Waits']][key['Away Team Scores 3 and Wins']] = 0
    results[key['Home Team Scores 0 and Waits']][key['Away Team Scores 0 and Ties']] = 1/2
    return results

def build_stochastic_matrix_for_other_rounds_home_team_plays_aggressively(initialized_matrix):
    results = [[i for i in j] for j in initialized_matrix]
    key = build_key()
    results[key['Away Team Scores 7 and Ties']][key['Away Team Scores 7 and Ties']] = 0
    results[key['Away Team Scores 7 and Ties']][key['Home Team Scores 7 and Wins']] = 1/2
    results[key['Away Team Scores 7 and Ties']][key['Home Team Scores 3 and Wins']] = 0
    results[key['Away Team Scores 7 and Ties']][key['Home Team Scores 0 and Waits']] = 1/2
    results[key['Away Team Scores 3 and Ties']][key['Away Team Scores 3 and Ties']] = 0
    results[key['Away Team Scores 3 and Ties']][key['Home Team Scores 7 and Wins']] = 1/2
    results[key['Away Team Scores 3 and Ties']][key['Home Team Scores 3 and Wins']] = 0
    results[key['Away Team Scores 3 and Ties']][key['Home Team Scores 0 and Waits']] = 1/2
    results[key['Away Team Scores 0 and Ties']][key['Away Team Scores 0 and Ties']] = 0
    results[key['Away Team Scores 0 and Ties']][key['Home Team Scores 7 and Wins']] = 1/2
    results[key['Away Team Scores 0 and Ties']][key['Home Team Scores 3 and Wins']] = 0
    results[key['Away Team Scores 0 and Ties']][key['Home Team Scores 0 and Waits']] = 1/2
    return results

def build_stochastic_matrix_for_other_rounds_away_team_plays_aggressively(initialized_matrix):
    results = [[i for i in j] for j in initialized_matrix]
    key = build_key()
    results[key['Home Team Scores 0 and Waits']][key['Home Team Scores 0 and Waits']] = 0
    results[key['Home Team Scores 0 and Waits']][key['Away Team Scores 7 and Wins']] = 1/2
    results[key['Home Team Scores 0 and Waits']][key['Away Team Scores 3 and Wins']] = 0
    results[key['Home Team Scores 0 and Waits']][key['Away Team Scores 0 and Ties']] = 1/2
    return results

def build_stochastic_matrix_for_1st_round_away_team_plays_adaptively_safe(initialized_matrix):
    results = [[i for i in j] for j in initialized_matrix]
    key = build_key()
    results[key['Home Team Scores 7 and Waits']][key['Home Team Scores 7 and Waits']] = 0
    results[key['Home Team Scores 7 and Waits']][key['Away Team Scores 7 and Ties']] = 1/2
    results[key['Home Team Scores 7 and Waits']][key['Away Team Scores 3 and Loses']] = 0
    results[key['Home Team Scores 7 and Waits']][key['Away Team Scores 0 and Loses']] = 1/2
    results[key['Home Team Scores 3 and Waits']][key['Home Team Scores 3 and Waits']] = 0
    results[key['Home Team Scores 3 and Waits']][key['Away Team Scores 7 and Wins']] = 1/3
    results[key['Home Team Scores 3 and Waits']][key['Away Team Scores 3 and Ties']] = 1/3
    results[key['Home Team Scores 3 and Waits']][key['Away Team Scores 0 and Loses']] = 1/3
    results[key['Home Team Scores 0 and Waits']][key['Home Team Scores 0 and Waits']] = 0
    results[key['Home Team Scores 0 and Waits']][key['Away Team Scores 7 and Wins']] = 1/3
    results[key['Home Team Scores 0 and Waits']][key['Away Team Scores 3 and Wins']] = 1/3
    results[key['Home Team Scores 0 and Waits']][key['Away Team Scores 0 and Ties']] = 1/3
    return results

def build_stochastic_matrix_for_1st_round_away_team_plays_adaptively_aggressive(initialized_matrix):
    results = [[i for i in j] for j in initialized_matrix]
    key = build_key()
    results[key['Home Team Scores 7 and Waits']][key['Home Team Scores 7 and Waits']] = 0
    results[key['Home Team Scores 7 and Waits']][key['Away Team Scores 7 and Ties']] = 1/2
    results[key['Home Team Scores 7 and Waits']][key['Away Team Scores 3 and Loses']] = 0
    results[key['Home Team Scores 7 and Waits']][key['Away Team Scores 0 and Loses']] = 1/2
    results[key['Home Team Scores 3 and Waits']][key['Home Team Scores 3 and Waits']] = 0
    results[key['Home Team Scores 3 and Waits']][key['Away Team Scores 7 and Wins']] = 1/2
    results[key['Home Team Scores 3 and Waits']][key['Away Team Scores 3 and Ties']] = 0
    results[key['Home Team Scores 3 and Waits']][key['Away Team Scores 0 and Loses']] = 1/2
    results[key['Home Team Scores 0 and Waits']][key['Home Team Scores 0 and Waits']] = 0
    results[key['Home Team Scores 0 and Waits']][key['Away Team Scores 7 and Wins']] = 1/3
    results[key['Home Team Scores 0 and Waits']][key['Away Team Scores 3 and Wins']] = 1/3
    results[key['Home Team Scores 0 and Waits']][key['Away Team Scores 0 and Ties']] = 1/3
    return results

def home_team_wins(state_matrix):
    key = build_key()
    results = state_matrix[0][key['Home Team Scores 7 and Wins']]
    results += state_matrix[0][key['Home Team Scores 3 and Wins']]
    results += state_matrix[0][key['Away Team Scores 3 and Loses']]
    results += state_matrix[0][key['Away Team Scores 0 and Loses']]
    return results

def away_team_wins(state_matrix):
    key = build_key()
    results = state_matrix[0][key['Away Team Scores 7 and Wins']]
    results += state_matrix[0][key['Away Team Scores 3 and Wins']]
    return results

def both_teams_play_it_safe():
    size = len(build_key())
    sto_mat = initialize_stochastic_matrix(size)
    sto_mat_1st_round_home_team = build_stochastic_matrix_for_1st_round_home_team_plays_it_safe(sto_mat)
    sto_mat_1st_round_away_team = build_stochastic_matrix_for_1st_round_away_team_plays_it_safe(sto_mat)
    sto_mat_oth_round_home_team = build_stochastic_matrix_for_other_rounds_home_team_plays_it_safe(sto_mat)
    sto_mat_oth_round_away_team = build_stochastic_matrix_for_other_rounds_away_team_plays_it_safe(sto_mat)
    strategy_statement = 'When both teams play it safe, i.e. "go for a 3 or 7"'
    course_of_play_template(sto_mat_1st_round_home_team, sto_mat_1st_round_away_team, sto_mat_oth_round_home_team, sto_mat_oth_round_away_team, strategy_statement)

def both_teams_play_aggressively():
    size = len(build_key())
    sto_mat = initialize_stochastic_matrix(size)
    sto_mat_1st_round_home_team = build_stochastic_matrix_for_1st_round_home_team_plays_aggressively(sto_mat)
    sto_mat_1st_round_away_team = build_stochastic_matrix_for_1st_round_away_team_plays_aggressively(sto_mat)
    sto_mat_oth_round_home_team = build_stochastic_matrix_for_other_rounds_home_team_plays_aggressively(sto_mat)
    sto_mat_oth_round_away_team = build_stochastic_matrix_for_other_rounds_away_team_plays_aggressively(sto_mat)
    strategy_statement = 'When both teams play aggressively, i.e. "always go for 7"'
    course_of_play_template(sto_mat_1st_round_home_team, sto_mat_1st_round_away_team, sto_mat_oth_round_home_team, sto_mat_oth_round_away_team, strategy_statement)

def home_team_plays_it_safe_away_team_plays_aggressively():
    size = len(build_key())
    sto_mat = initialize_stochastic_matrix(size)
    sto_mat_1st_round_home_team = build_stochastic_matrix_for_1st_round_home_team_plays_it_safe(sto_mat)
    sto_mat_1st_round_away_team = build_stochastic_matrix_for_1st_round_away_team_plays_aggressively(sto_mat)
    sto_mat_oth_round_home_team = build_stochastic_matrix_for_other_rounds_home_team_plays_it_safe(sto_mat)
    sto_mat_oth_round_away_team = build_stochastic_matrix_for_other_rounds_away_team_plays_it_safe(sto_mat)
    strategy_statement = 'When Home plays it safe but Away plays it aggressively'
    course_of_play_template(sto_mat_1st_round_home_team, sto_mat_1st_round_away_team, sto_mat_oth_round_home_team, sto_mat_oth_round_away_team, strategy_statement)

def home_team_plays_it_safe_away_team_plays_adaptively_safe():
    size = len(build_key())
    sto_mat = initialize_stochastic_matrix(size)
    sto_mat_1st_round_home_team = build_stochastic_matrix_for_1st_round_home_team_plays_it_safe(sto_mat)
    sto_mat_1st_round_away_team = build_stochastic_matrix_for_1st_round_away_team_plays_adaptively_safe(sto_mat)
    sto_mat_oth_round_home_team = build_stochastic_matrix_for_other_rounds_home_team_plays_it_safe(sto_mat)
    sto_mat_oth_round_away_team = build_stochastic_matrix_for_other_rounds_away_team_plays_it_safe(sto_mat)
    strategy_statement = 'When Home plays it safe but Away plays an adaptive but safe game, i.e. "go for a tie if down by 3 or 7"'
    course_of_play_template(sto_mat_1st_round_home_team, sto_mat_1st_round_away_team, sto_mat_oth_round_home_team, sto_mat_oth_round_away_team, strategy_statement)

def home_team_plays_it_safe_away_team_plays_adaptively_aggressive():
    size = len(build_key())
    sto_mat = initialize_stochastic_matrix(size)
    sto_mat_1st_round_home_team = build_stochastic_matrix_for_1st_round_home_team_plays_it_safe(sto_mat)
    sto_mat_1st_round_away_team = build_stochastic_matrix_for_1st_round_away_team_plays_adaptively_aggressive(sto_mat)
    sto_mat_oth_round_home_team = build_stochastic_matrix_for_other_rounds_home_team_plays_it_safe(sto_mat)
    sto_mat_oth_round_away_team = build_stochastic_matrix_for_other_rounds_away_team_plays_it_safe(sto_mat)
    strategy_statement = 'When Home plays it safe but Away plays an adaptive yet aggressive game, i.e. "go for a win if down by 3 or a tie if down by 7"'
    course_of_play_template(sto_mat_1st_round_home_team, sto_mat_1st_round_away_team, sto_mat_oth_round_home_team, sto_mat_oth_round_away_team, strategy_statement)

def both_teams_play_adaptively_aggressive():
    size = len(build_key())
    sto_mat = initialize_stochastic_matrix(size)
    sto_mat_1st_round_home_team = build_stochastic_matrix_for_1st_round_home_team_plays_aggressively(sto_mat)
    sto_mat_1st_round_away_team = build_stochastic_matrix_for_1st_round_away_team_plays_adaptively_aggressive(sto_mat)
    sto_mat_oth_round_home_team = build_stochastic_matrix_for_other_rounds_home_team_plays_it_safe(sto_mat)
    sto_mat_oth_round_away_team = build_stochastic_matrix_for_other_rounds_away_team_plays_it_safe(sto_mat)
    strategy_statement = 'When both teams play an adaptive yet aggressive game, i.e. "Home goes for 7 initially, while Away goes for a win if down by 3 or a tie if down by 7"'
    course_of_play_template(sto_mat_1st_round_home_team, sto_mat_1st_round_away_team, sto_mat_oth_round_home_team, sto_mat_oth_round_away_team, strategy_statement)

def home_team_plays_aggressively_away_team_plays_it_safe():
    size = len(build_key())
    sto_mat = initialize_stochastic_matrix(size)
    sto_mat_1st_round_home_team = build_stochastic_matrix_for_1st_round_home_team_plays_aggressively(sto_mat)
    sto_mat_1st_round_away_team = build_stochastic_matrix_for_1st_round_away_team_plays_it_safe(sto_mat)
    sto_mat_oth_round_home_team = build_stochastic_matrix_for_other_rounds_home_team_plays_it_safe(sto_mat)
    sto_mat_oth_round_away_team = build_stochastic_matrix_for_other_rounds_away_team_plays_it_safe(sto_mat)
    strategy_statement = 'When Home plays it safe but Away plays it aggressively'
    course_of_play_template(sto_mat_1st_round_home_team, sto_mat_1st_round_away_team, sto_mat_oth_round_home_team, sto_mat_oth_round_away_team, strategy_statement)

def course_of_play_template(sto_mat_1st_round_home_team, sto_mat_1st_round_away_team, sto_mat_oth_round_home_team, sto_mat_oth_round_away_team, strategy_statement):
    size = len(build_key())
    sta_mat = initialize_state_matrix(size)
    sta_mat = numpy.matmul(sta_mat, sto_mat_1st_round_home_team)
    sta_mat = numpy.matmul(sta_mat, sto_mat_1st_round_away_team)
    sta_mat = numpy.matmul(sta_mat, sto_mat_oth_round_home_team)
    sta_mat = numpy.matmul(sta_mat, sto_mat_oth_round_away_team)
    sta_mat = numpy.matmul(sta_mat, sto_mat_oth_round_home_team)
    sta_mat = numpy.matmul(sta_mat, sto_mat_oth_round_away_team)
    sta_mat = numpy.matmul(sta_mat, sto_mat_oth_round_home_team)
    sta_mat = numpy.matmul(sta_mat, sto_mat_oth_round_away_team)
    sta_mat = numpy.matmul(sta_mat, sto_mat_oth_round_home_team)
    sta_mat = numpy.matmul(sta_mat, sto_mat_oth_round_away_team)
    sta_mat = numpy.matmul(sta_mat, sto_mat_oth_round_home_team)
    sta_mat = numpy.matmul(sta_mat, sto_mat_oth_round_away_team)
    sta_mat = numpy.matmul(sta_mat, sto_mat_oth_round_home_team)
    sta_mat = numpy.matmul(sta_mat, sto_mat_oth_round_away_team)
    sta_mat = numpy.matmul(sta_mat, sto_mat_oth_round_home_team)
    sta_mat = numpy.matmul(sta_mat, sto_mat_oth_round_away_team)
    sta_mat = numpy.matmul(sta_mat, sto_mat_oth_round_home_team)
    sta_mat = numpy.matmul(sta_mat, sto_mat_oth_round_away_team)
    sta_mat = numpy.matmul(sta_mat, sto_mat_oth_round_home_team)
    sta_mat = numpy.matmul(sta_mat, sto_mat_oth_round_away_team)
    sta_mat = numpy.matmul(sta_mat, sto_mat_oth_round_home_team)
    sta_mat = numpy.matmul(sta_mat, sto_mat_oth_round_away_team)
    sta_mat = numpy.matmul(sta_mat, sto_mat_oth_round_home_team)
    sta_mat = numpy.matmul(sta_mat, sto_mat_oth_round_away_team)
    home_team_pct = '{:.2f}%'.format(home_team_wins(sta_mat) * 100)
    away_team_pct = '{:.2f}%'.format(away_team_wins(sta_mat) * 100)
    print(f'{strategy_statement}, Home wins {home_team_pct} of the time, and Away wins {away_team_pct}.')

def go_markov_chains():
    print("Calculating the exact probabilities using Markov Chains:")
    both_teams_play_it_safe()
    both_teams_play_aggressively()
    home_team_plays_it_safe_away_team_plays_aggressively()
    home_team_plays_aggressively_away_team_plays_it_safe()
    home_team_plays_it_safe_away_team_plays_adaptively_safe()
    home_team_plays_it_safe_away_team_plays_adaptively_aggressive()
    both_teams_play_adaptively_aggressive()

go_markov_chains()
print()
simulation_method.go_simulations()
import random
import math
import pprint

def run_game_simulation(home_team_strategy, away_team_strategy):
    round = 1
    home_team_has_possession = True
    game_over = False
    home_team_wins = False
    away_team_wins = False
    home_team_score = 0
    away_team_score = 0
    while not game_over:
        if round == 1:
            if home_team_has_possession:
                home_team_score = random.choice(home_team_strategy['equity_round'])
                home_team_has_possession = False
            else:
                if home_team_score == 7:
                    away_team_score = random.choice(away_team_strategy['down_by_7'])
                elif home_team_score == 3:
                    away_team_score = random.choice(away_team_strategy['down_by_3'])
                else:
                    away_team_score = random.choice(away_team_strategy['score_tied'])
                if away_team_score > home_team_score:
                    away_team_wins = True
                    home_team_wins = False
                    game_over = True
                    break
                elif home_team_score > away_team_score:
                    home_team_wins = True
                    away_team_wins = False
                    game_over = True
                    break
                round +=1
                home_team_has_possession = True
        else:
            if home_team_has_possession:
                home_team_score = random.choice(home_team_strategy['sudden_death_round'])
                if home_team_score > 0:
                    home_team_wins = True
                    away_team_wins = False
                    game_over = True
                    break
                home_team_has_possession = False
            else:
                away_team_score = random.choice(away_team_strategy['score_tied'])
                if away_team_score > 0:
                    away_team_wins = True
                    home_team_wins = False
                    game_over = True
                    break
                round += 1
                home_team_has_possession = True
    return {'home_team_wins': home_team_wins, 'away_team_wins': away_team_wins, 'round': round}

def run_game_simulations(number_of_simulations, home_team_strategy, away_team_strategy, strategy_statement):
    results = {'home_team_wins': 0, 'away_team_wins': 0, 'max_rounds': 0}
    for i in range(0, number_of_simulations):
        game_results = run_game_simulation(home_team_strategy, away_team_strategy)
        winner = 'No'
        if game_results['home_team_wins']:
            winner = 'Home'
            results['home_team_wins'] = results['home_team_wins'] + 1
        if game_results['away_team_wins']:
            winner = 'Away'
            results['away_team_wins'] = results['away_team_wins'] + 1
        results['max_rounds'] = max([results['max_rounds'], game_results['round']])
        game_rounds = game_results['round']
        #print(f'The {winner} team won in {game_rounds}.')
        home_team_pct = '{:.2f}%'.format(results['home_team_wins'] / number_of_simulations * 100)
        away_team_pct = '{:.2f}%'.format(results['away_team_wins'] / number_of_simulations * 100)
    print(f'{strategy_statement}, the home team wins approx. {home_team_pct} of the time, and the away team wins approx. {away_team_pct}.')
    #pprint.pprint(results)

def go_simulations():
    print('Calculating the estimated probabilities using game simulations:')
    home_team_safe_strategy = {
        'equity_round': [0, 3, 7],
        'sudden_death_round': [0, 3, 7]
    }

    home_team_aggressive_strategy = {
        'equity_round': [0, 7],
        'sudden_death_round': [0, 7]
    }

    home_team_adaptive_aggressive_strategy = {
        'equity_round': [0, 7],
        'sudden_death_round': [0, 3, 7]
    }

    away_team_safe_strategy = {
        'down_by_7': [0, 3, 7],
        'down_by_3': [0, 3, 7],
        'score_tied': [0, 3, 7]
    }

    away_team_aggressive_strategy = {
        'down_by_7': [0, 7],
        'down_by_3': [0, 7],
        'score_tied': [0, 7]
    }

    away_team_adaptive_safe_strategy = {
        'down_by_7': [0, 7],
        'down_by_3': [0, 3, 7],
        'score_tied': [0, 3, 7]
    }

    away_team_adaptive_aggressive_strategy = {
        'down_by_7': [0, 7],
        'down_by_3': [0, 7],
        'score_tied': [0, 3, 7]
    }

    strategy_statement = 'When both teams play it safe, i.e. "go for a 3 or 7"'
    run_game_simulations(100000000, home_team_safe_strategy, away_team_safe_strategy, strategy_statement)

    strategy_statement = 'When both teams play aggressively, i.e. "always go for 7"'
    run_game_simulations(10000000, home_team_aggressive_strategy, away_team_aggressive_strategy, strategy_statement)
    
    strategy_statement = 'When Home plays it safe but Away plays aggressively'
    run_game_simulations(1000000, home_team_safe_strategy, away_team_aggressive_strategy, strategy_statement)

    strategy_statement = 'When Home plays aggressively but Away plays it safe'
    run_game_simulations(1000000, home_team_aggressive_strategy, away_team_safe_strategy, strategy_statement)

    strategy_statement = 'When Home plays it safe but Away plays an adaptive but safe game, i.e. "go for a tie if down by 3 or 7"'
    run_game_simulations(1000000, home_team_safe_strategy, away_team_adaptive_safe_strategy, strategy_statement)

    strategy_statement = 'When Home plays it safe but Away plays an adaptive yet aggressive game, i.e. "go for a win if down by 3 or a tie if down by 7"'
    run_game_simulations(1000000, home_team_safe_strategy, away_team_adaptive_aggressive_strategy, strategy_statement)

    strategy_statement = 'When both teams play an adaptive yet aggressive game, i.e. "Home goes for 7 initially, while Away goes for a win if down by 3 or a tie if down by 7"'
    run_game_simulations(1000000, home_team_adaptive_aggressive_strategy, away_team_adaptive_aggressive_strategy, strategy_statement)

import random
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Simulate a trading strategy.")
parser.add_argument('--position_size', type=float, default=0.1, help='Position size as a fraction of total money.')
parser.add_argument('--win_prob', type=float, default=0.50, help='Probability of winning a trade.')
parser.add_argument('--return_on_win', type=float, default=2, help='Return multiplier on a winning trade.')

args = parser.parse_args()

# Initialize constants with command line arguments or defaults
position_size = args.position_size
win_prob = args.win_prob
return_on_win = args.return_on_win
trades = 100
initial_money = 1000
num_simulations = 1000

# List to store the results of each simulation
results = []

# Run the simulation multiple times
for _ in range(num_simulations):
    money_left = initial_money
    for _ in range(trades):
        money_in_trade = money_left * position_size
        money_left -= money_in_trade
        
        if random.random() < win_prob:
            money_left += money_in_trade * return_on_win
    
    results.append(money_left)

# Calculate summary statistics
average_money_left = sum(results) / num_simulations
max_money_left = max(results)
min_money_left = min(results)

# Print summary statistics
print(f"Average money left after simulations: ${average_money_left:.2f}")
print(f"Maximum money left after simulations: ${max_money_left:.2f}")
print(f"Minimum money left after simulations: ${min_money_left:.2f}")
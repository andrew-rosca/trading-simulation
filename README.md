### Trading Strategy Simulation

This Python script simulates a trading strategy over multiple iterations to analyze the potential outcomes based on certain parameters. 

It's a fun experiment to show the impact position size (risk) can have in different situations.

For example, allocating all your capital to a series of "sure thing" trades which have a 90% chance of doubling your money can have disatrous outcomes.

| Position Size | Win Probability | Return on Win | Average Return |
|---------------|-----------------|---------------|----------------|
| 100%          | 90%             | 200%          | 0%             |

On the other hand, taking many asymmetric bets (small bets / small risk but each having the potential to pay off huge) can be very lucrative.

| Position Size | Win Probability | Return on Win | Average Return |
|---------------|-----------------|---------------|--------------------|
| 2%            | 10%             | 3000%         | 4300%              |

### Usage

#### Command-Line Usage

Example usage:

```sh
python simulate.py --position_size 0.15 --win_prob 0.55 --return_on_win 2.5
```

#### Key Parameters
1. **Position Size (`--position_size`)**:
   - The fraction of the total money that is used in each trade.
   - Default value: `0.1` (10% of the total money).

2. **Win Probability (`--win_prob`)**:
   - The probability of winning a trade.
   - Default value: `0.50` (50% chance of winning).

3. **Return on Win (`--return_on_win`)**:
   - The return multiplier applied to the gains when a trade is won.
   - Default value: `2` (200% return on a winning trade).

Additional parameters, such as the nubmer of simulations to run and the number of trades per simulation, can me changed by modifying the constants in the beginning of the script.

The defaults are:
* initial capital: 1000
* number of simulations: 1000
* number of trades per simulation: 100
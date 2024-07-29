"""How many different ways can £2 be made using any number of coins?"""

target = 200

# Coin denominations in pence
coins = [1, 2, 5, 10, 20, 50, 100, 200]

# Initialize a list with zeros, with indices representing amounts from 0 to target
ways = [0] * (target + 1)

# There is one way to make 0 amount (use no coins)
ways[0] = 1

# For each coin, update the ways to make each amount up to the target
for coin in coins:
    for amount in range(coin, target + 1):
        ways[amount] += ways[amount - coin]

# The answer is the number of ways to make the target amount
print(ways[target])
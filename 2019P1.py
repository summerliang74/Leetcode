n = int(input())
pebble_1 = 1
pebble_2 = 2
pebble_3 = 3
score1 = 0
score2 = 0
score3 = 0
for i in range(n):
    swaps = input().split()
    guess = swaps[2]
    swaps = swaps[:2]
    if pebble_1 == int(swaps[0]):
        pebble_1 = int(swaps[1])
    elif pebble_1 == int(swaps[1]):
        pebble_1 = int(swaps[0])
    if guess == str(pebble_1):
        score1 += 1

    if pebble_2 == int(swaps[0]):
        pebble_2 = int(swaps[1])
    elif pebble_2 == int(swaps[1]):
        pebble_2 = int(swaps[0])
    if guess == str(pebble_2):
        score2 += 1

    if pebble_3 == int(swaps[0]):
        pebble_3 = int(swaps[1])
    elif pebble_3 == int(swaps[1]):
        pebble_3 = int(swaps[0])
    if guess == str(pebble_3):
        score3 += 1
print(max(score1, score2, score3))
#!/usr/bin/python3
"This module contains a function named make change to count fewest number of coins needed to meet total"


def makeChange(coins, total):
    "This function determines the fewest number of coins needed to meet amount total"
    # if total is 0 or less than 0, return 0

    count = 0
    if total > 0:
        i = 0
        coins.sort(reverse=True)
        len_1 = len(coins)
        if len_1 == 0:
            count = -1
        while(i < len_1):
            div = (total // coins[i])
            rest = (total % coins[i])
            count = count + div
            total = rest
            if rest != 0 and i == (len_1 - 1):
                count = -1
            if rest != 0:
                i += 1
            else:
                break
    else:
        count = 0
    return (count)

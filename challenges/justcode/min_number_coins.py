# https://www.hackerrank.com/contests/justcode/challenges/minimum-number-of-coins-for-possible-sum

import unittest


def getMinNumberCoinsRecursive(total, coins, index_coins, result, index, results):
    if total < 0:
        return
    if total == 0:
        results.append(list(result[:index]))
        return
    i = index_coins
    while i < len(coins):
        coin = coins[i]
        result[index] = coin
        getMinNumberCoinsRecursive(
            total - coin, coins, i, result, index + 1, results)
        i += 1
    return


def getMinNumberCoins(total, coins):
    my_coins = sorted(coins, reverse=True)
    result = [0] * (total + 1)
    results = []
    getMinNumberCoinsRecursive(total, my_coins, 0, result, 0, results)
    min_coins = total
    for r in results:
        len_list_result = len(r)
        if len_list_result < min_coins:
            min_coins = len_list_result
    return min_coins


def getMinNumberCoinsTabular(total, coins):
    tab = [0] * (total + 1)
    i = 1
    while i <= total:
        previous_results = [
            tab[i - coin] + 1 for coin in coins if i - coin >= 0]
        if previous_results:
            tab[i] = min(previous_results)
        i += 1
    return tab[total]


class Testing(unittest.TestCase):

    def test_0(self):
        min_coins = getMinNumberCoinsTabular(
            11, list(map(int, '1 3 5'.split(' '))))
        min_coins_rec = getMinNumberCoins(
            11, list(map(int, '1 3 5'.split(' '))))
        self.assertEqual(min_coins, 3)
        self.assertEqual(min_coins, min_coins_rec)

    def test_1(self):
        min_coins = getMinNumberCoinsTabular(
            25, list(map(int, '4 5 2 1 9'.split(' '))))
        min_coins_rec = getMinNumberCoins(
            25, list(map(int, '4 5 2 1 9'.split(' '))))
        self.assertEqual(min_coins, 4)
        self.assertEqual(min_coins, min_coins_rec)

    def test_2(self):
        min_coins = getMinNumberCoinsTabular(
            5, list(map(int, '1 3 5'.split(' '))))
        min_coins_rec = getMinNumberCoins(
            5, list(map(int, '1 3 5'.split(' '))))
        self.assertEqual(min_coins, 1)
        self.assertEqual(min_coins, min_coins_rec)

    def test_3(self):
        min_coins = getMinNumberCoinsTabular(
            18, list(map(int, '1 2 5 10'.split(' '))))
        min_coins_rec = getMinNumberCoins(
            18, list(map(int, '1 2 5 10'.split(' '))))
        self.assertEqual(min_coins, 4)
        self.assertEqual(min_coins, min_coins_rec)

    def test_4(self):
        min_coins = getMinNumberCoinsTabular(
            256324, list(map(int, '1 2 5 10 20 50'.split(' '))))
        self.assertEqual(min_coins, 5129)

    def test_5(self):
        min_coins = getMinNumberCoinsTabular(
            564, list(map(int, '1 2 5 10 20 50 100 500'.split(' '))))
        self.assertEqual(min_coins, 5)


if __name__ == '__main__':
    unittest.main()

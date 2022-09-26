#!/usr/bin/env python3
# uses async/await syntax introduced in py 3.5+ - and prints the numbers 1-100 in a convoluted way

from asyncio import run, sleep, wait
import random

def get_numbers_btwn_range(s, e, i):
   return list(range(s, e, i))

async def sleep_sort(n):
    await sleep(n)
    print(n)

if __name__ == '__main__':
    # make an ordered list
    start, end, intval = 1, 101, 1
    ordered_list = get_numbers_btwn_range(start, end, intval)

    # shuffle it for no good reason, twice
    random.shuffle(ordered_list)
    shuffled_list = random.sample(ordered_list, len(ordered_list))
    # print("shuffled lis")
    # print(shuffled_list)

    # iterate over the list to print each number after awaiting its value in elapsed time, so it becomes an ordered list again
    run(wait(map(sleep_sort, map(int, shuffled_list))))

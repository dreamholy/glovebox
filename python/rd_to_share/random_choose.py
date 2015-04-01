#!/usr/bin/env python
# -*- coding: utf8 -*-
# =========================================================
#
# Copyright (c) 2014 Dreamholy. All Rights Reserved
#
# =========================================================
"""
随机产生重构分享人
Authors: 'dreamholy'
Date:    '2014/12/23 10:10'
"""
import random
import time

rd_chosen_count_file = 'D://rd_chosen_count.txt'
rd_chosen_count_dict = {}


def init_rd_chosen_dict():
    count_file = open(rd_chosen_count_file, 'r')
    content = count_file.readlines()
    count_file.close()
    for line in content:
        line_block = line.split("=")
        if len(line_block) < 2:
            continue
        rd_chosen_count_dict[str(line_block[0])] = int(line_block[1])


def update_rd_chosen_count(chosen_rds):
    for rd_name in chosen_rds:
        rd_chosen_count_dict[rd_name] += 1
    count_file = open(rd_chosen_count_file, 'w')
    for rd_name, chosen_count in rd_chosen_count_dict.items():
        count_file.write(rd_name + "=" + str(chosen_count) + "\n")
    count_file.flush()
    count_file.close()


def get_chosen_sequence():
    chosen_seq = []
    total_chosen_count = 0
    for count in rd_chosen_count_dict.values():
        total_chosen_count += count
    for rd_name, count in rd_chosen_count_dict.items():
        loop_count = 1 + total_chosen_count - count
        for i in range(0, loop_count):
            chosen_seq.append(rd_name)
    return chosen_seq


def random_rd(chosen_seq):
    time_seed = long(time.time() * 256)  # 默认的seed
    random_instance = random.Random()
    random_instance.seed(time_seed)
    random_instance.shuffle(chosen_seq)
    selected_rd = random_instance.choice(chosen_seq)
    print "selected rd is :" + selected_rd + "; seed is :" + str(time_seed)
    return selected_rd


def main():
    init_rd_chosen_dict()

    chosen_sequence = get_chosen_sequence()

    first_rd = random_rd(chosen_sequence)
    time.sleep(1)
    second_rd = random_rd(chosen_sequence)
    while second_rd == first_rd:
        time.sleep(1)
        second_rd = random_rd(chosen_sequence)
    print "随机结果：" + first_rd + " 和 " + second_rd

    update_rd_chosen_count([first_rd, second_rd])


if __name__ == '__main__':
    main()
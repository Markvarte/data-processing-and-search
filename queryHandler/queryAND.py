import itertools
import math


def query_and(selected_postings_dict):
    term_count = len(selected_postings_dict)
    if term_count < 2:
        return ['term count less that 2, can\'t do AND query']
    else:
        result_posting_list = []
        for key, val in selected_postings_dict.items():
            result_posting_list.append(val)
        while len(result_posting_list) != 1:
            # insert at the beginning of list to make shorter lists process first: that reduce doc id needed to check
            result_posting_list.insert(0, intercept_with_skips(result_posting_list[0], result_posting_list[1]))
            # need to delete 2 items from list because we already found intercept between them and put it on 0 index
            del result_posting_list[1], result_posting_list[1]
        # merging list in list to one list
        result_intercept_list = list(itertools.chain.from_iterable(result_posting_list))
        if result_intercept_list:
            return result_intercept_list
        else:
            return ['empty']


def intercept_with_skips(p1, p2):
    if not p1 or not p2:
        return ['empty']
    p1_with_skips = add_skips(p1)
    p2_with_skips = add_skips(p2)
    intercept = []
    p1_index = 0
    p2_index = 0
    while p1_index < len(p1) and p2_index < len(p2):
        if p1[p1_index] == p2[p2_index]:
            intercept.append(p1[p1_index])
            p1_index += 1
            p2_index += 1
        elif p1[p1_index] < p2[p2_index]:
            next_skip_pos_p1 = next_skip(p1_index + 1, p1_with_skips)
            if next_skip_pos_p1 and (p1[next_skip_pos_p1] <= p2[p2_index]):
                p1_index = next_skip_pos_p1
            else:
                p1_index += 1
        elif p2[p2_index] < p1[p1_index]:
            next_skip_pos_p2 = next_skip(p2_index + 1, p2_with_skips)
            if next_skip_pos_p2 and (p2[next_skip_pos_p2] <= p1[p1_index]):
                p2_index = next_skip_pos_p2
            else:
                p2_index += 1
    return intercept


def add_skips(posting_list):
    post_list_with_skips = []
    skip_count = math.floor(math.sqrt(len(posting_list)))
    pos_index = 0
    skip_period = math.floor(len(posting_list) / skip_count)
    skip_index = 0
    while pos_index < len(posting_list):
        if pos_index == skip_index:
            post_list_with_skips.append([posting_list[pos_index], 1])
            skip_index += skip_period
        else:
            post_list_with_skips.append([posting_list[pos_index], 0])
        pos_index += 1
    return post_list_with_skips


def next_skip(start_index, posting_list):
    while start_index < len(posting_list):
        if posting_list[start_index][1]:
            return start_index
        start_index += 1
    else:
        return False

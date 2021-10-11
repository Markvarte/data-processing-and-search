import filesHandler
import postingsHandler
import math


def process_query(postings_dict, query_file_name='query.txt', result_file_name='result.txt'):
    all_queries_list = filesHandler.split_query(query_file_name)
    for query in all_queries_list:
        selected_postings_dict = postingsHandler.get_all_postings_by_query(postings_dict, query)
        # query_and(selected_postings_dict)
        # queryOr
        filesHandler.write_selected_postings(selected_postings_dict, result_file_name)


# def query_and(selected_postings_dict: dict):
#     and_ids = []
#     term_count = len(selected_postings_dict)
#     if term_count < 2:
#         return selected_postings_dict.values()
#     if term_count == 2:
#         # !!!
#         return intercept_with_skips(selected_postings_dict.values(), selected_postings_dict[1])
#     elif term_count > 2:
#         # kak to loop

    each_posting_count = []
    postings_list = []
    # for key, val in selected_postings_dict.items():
    #     each_posting_count.append(len(val))
    #     postings_list.append([val])
    # print("each_posting_count",each_posting_count)
    # smallest_posting_index = 0
    # posting_num = 0
    # while smallest_posting_index < min(each_posting_count):
    #     while posting_num < term_count:
    #         if
    #         posting_num += 1


def intercept_with_skips(p1, p2):
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


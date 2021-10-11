import filesHandler
import postingsHandler


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
#     print("term_count", term_count)
#     each_posting_count = []
#     postings_list = []
#     for key, val in selected_postings_dict.items():
#         each_posting_count.append(len(val))
#         postings_list.append([val])
#     print("each_posting_count",each_posting_count)
#     smallest_posting_index = 0
#     posting_num = 0
#     while smallest_posting_index < min(each_posting_count):
#         while posting_num < term_count:
#             if
#             posting_num += 1





from IOfilesHandler import inputHandler, outputHandler
from invertedIndex import postingsHandler
from TFIDF import scoreCounter
from queryHandler import queryOR, queryAND


def process_query(postings_dict, query_file_name='query.txt', result_file_name='result.txt'):
    all_queries_list = inputHandler.split_query(query_file_name)
    for query in all_queries_list:
        selected_postings_dict = postingsHandler.get_all_postings_by_query(postings_dict, query)
        intercept_with_skips_list = queryAND.query_and(selected_postings_dict)
        join_postings_list = queryOR.query_or(selected_postings_dict)
        outputHandler.write_selected_postings(selected_postings_dict, result_file_name)
        outputHandler.write_query(query, intercept_with_skips_list, result_file_name)  # write and query
        outputHandler.write_query(query, join_postings_list, result_file_name, is_and=False)  # write or query
        scoreCounter.find_score(selected_postings_dict, join_postings_list)

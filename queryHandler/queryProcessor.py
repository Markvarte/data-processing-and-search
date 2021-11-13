from IOfilesHandler import inputHandler, outputHandler
from invertedIndex import postingsHandler
from TFIDF import scoreCounter, termCounter
from queryHandler import queryOR, queryAND


def process_query(postings_dict, main_file_name='simple-sample.txt', query_file_name='simple-query.txt', result_file_name='result.txt'):
    all_queries_list = inputHandler.split_query(query_file_name)
    [docs_for_TFIDF_dict, term_counts_in_docs_dict] = TFIDF_preparation(main_file_name)
    for query in all_queries_list:
        selected_postings_dict = postingsHandler.get_all_postings_by_query(postings_dict, query)
        intercept_with_skips_list = queryAND.query_and(selected_postings_dict)
        join_postings_list = queryOR.query_or(selected_postings_dict)
        outputHandler.write_selected_postings(selected_postings_dict, result_file_name)
        outputHandler.write_query(query, intercept_with_skips_list, result_file_name)  # write and query
        outputHandler.write_query(query, join_postings_list, result_file_name, is_and=False)  # write or query
        scoreCounter.find_score(docs_for_TFIDF_dict, term_counts_in_docs_dict, selected_postings_dict, join_postings_list)


def TFIDF_preparation(main_file_name):
    # docs_for_TFIDF_dict = { docid : ['word1', 'word2', 'word3', ... ] }
    docs_for_TFIDF_dict = inputHandler.create_docs_terms_dict(main_file_name)
    # Example: {'1000': Counter({'Thi': 1, 'Jane': 1, 'Austen': 1}), '1001': Counter({'is': 2, 'This': 1, 's': 1}), ...}
    term_counts_in_docs_dict = termCounter.each_term_count_in_doc(docs_for_TFIDF_dict)
    return docs_for_TFIDF_dict, term_counts_in_docs_dict

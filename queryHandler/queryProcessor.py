from IOfilesHandler import inputHandler, outputHandler
from invertedIndex import postingsHandler
from TFIDF import scoreCounter, termCounter
from queryHandler import queryOR, queryAND
from permutationIndex import RotationsCreator, permutationIndexCreator


def process_query(postings_dict, main_file_name='sample.txt', query_file_name='query.txt', result_file_name='result.txt'):
    all_queries_list = inputHandler.split_query(query_file_name)
    [docs_for_TFIDF_dict, term_counts_in_docs_dict] = TFIDF_preparation(main_file_name)
    for query in all_queries_list:
        selected_postings_dict = postingsHandler.get_all_postings_by_query(postings_dict, query)
        intercept_with_skips_list = queryAND.query_and(selected_postings_dict)
        join_postings_list = queryOR.query_or(selected_postings_dict)
        ranked_intercept_postings_list = scoreCounter.create_ranked_posting_list(docs_for_TFIDF_dict, term_counts_in_docs_dict, selected_postings_dict, intercept_with_skips_list)
        ranked_joining_postings_list = scoreCounter.create_ranked_posting_list(docs_for_TFIDF_dict, term_counts_in_docs_dict, selected_postings_dict, join_postings_list)
        outputHandler.write_selected_postings(selected_postings_dict, result_file_name)
        outputHandler.write_query(query, intercept_with_skips_list, result_file_name, 'QueryAnd')  # write and query
        outputHandler.write_query(query, ranked_intercept_postings_list, result_file_name, 'TF-IDF')  # write TF-IDF ranked list
        outputHandler.write_query(query, join_postings_list, result_file_name, 'QueryOr')  # write or query
        outputHandler.write_query(query, ranked_joining_postings_list, result_file_name, 'TF-IDF')  # write TF-IDF ranked list


def TFIDF_preparation(main_file_name):
    # docs_for_TFIDF_dict = { docid : ['word1', 'word2', 'word3', ... ] }
    docs_for_TFIDF_dict = inputHandler.create_docs_terms_dict(main_file_name)
    # Example: {'1000': Counter({'Thi': 1, 'Jane': 1, 'Austen': 1}), '1001': Counter({'is': 2, 'This': 1, 's': 1}), ...}
    term_counts_in_docs_dict = termCounter.each_term_count_in_doc(docs_for_TFIDF_dict)
    return docs_for_TFIDF_dict, term_counts_in_docs_dict


def process_substitute_query(postings_dict, template_file_name='template.txt', result_file_name='result.txt'):
    all_template_list = inputHandler.split_query(template_file_name)
    rotations_dict = RotationsCreator.create_rotations(postings_dict.keys())
    for template_list in all_template_list:
        for template in template_list:
            result_postings = permutationIndexCreator.get_postings_by_template(postings_dict, rotations_dict, template)
            outputHandler.write_wild_card(template, result_postings, result_file_name)

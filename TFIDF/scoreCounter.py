from TFIDF import TFIDFCounter


def find_score(all_docs: dict, term_counts_in_docs_dict: dict, selected_postings_dict: dict, join_postings_list: list):
    # not for query term: term_counts_in_docs_dict - all { doc_id: Counter({'Thi': 1, 'Jane': 1, 'Austen': 1, ...}), doc_id2 ... } dictionary
    # for one query terms: selected_postings_dict - dictionary, keys = terms, vals = postings
    # for one query terms: join_postings_list - all distinct postings
    [all_query_terms_freq, doc_amount_per_term] = get_terms_freq_per_doc(term_counts_in_docs_dict, selected_postings_dict)
    each_selected_doc_size = get_each_selected_doc_size(all_docs, join_postings_list)

    tf = TFIDFCounter.count_TF(all_query_terms_freq, each_selected_doc_size)
    idf = TFIDFCounter.count_IDF(len(term_counts_in_docs_dict), doc_amount_per_term)
    print("all:", len(term_counts_in_docs_dict), "doc_amount_per_term:", doc_amount_per_term, "idf:", idf)
    return ['empty']


def get_terms_freq_per_doc(term_counts_in_docs_dict: dict, selected_postings_dict: dict):
    all_query_terms_freq = {}
    doc_amount_per_term = {}
    for term, posting_list in selected_postings_dict.items():
        doc_term_appear_count = get_doc_freq_per_term(term_counts_in_docs_dict, term)
        # all_terms_freq = { term : {id : freq, id2 : freq, id3 : freq, ...}, term2 : { ...}, ... }
        all_query_terms_freq[term] = doc_term_appear_count
        # doc_amount_per_term = { term : doc_amount, term2 : doc_amount, ... }
        doc_amount_per_term[term] = len(doc_term_appear_count)
    return all_query_terms_freq, doc_amount_per_term


def get_doc_freq_per_term(term_counts_in_docs_dict: dict, term: str):
    doc_term_appear_count = {}
    # Example: term_counts_in_docs_dict = {'1000': Counter({'Thi': 1, 'Jane': 1, 'Austen': 1}), '1001': Counter({'is': 2, 'This': 1, 's': 1}), ...}
    for doc_id, terms_freq_dict in term_counts_in_docs_dict.items():
        for term_key, freq in terms_freq_dict.items():
            if term_key == term:
                doc_term_appear_count[doc_id] = freq
                break
    # doc_term_appear_count = {id : freq, id2 : freq, id3 : freq, ...}
    return doc_term_appear_count


def get_each_selected_doc_size(all_docs: dict, join_postings_list: list):
    each_doc_size = {}
    for selected_doc_id in join_postings_list:
        for doc_id, terms_list in all_docs.items():
            if doc_id == selected_doc_id:
                each_doc_size[doc_id] = len(terms_list)
    return each_doc_size

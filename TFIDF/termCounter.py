from collections import Counter


# not related to query
def each_term_count_in_doc(docs_dict):
    counts_dict = {}
    for doc_id, term_list in docs_dict.items():
        counts = Counter(term_list)  # Example: Counter({'Thi': 1, 'Jane': 1, 'Austen': 1})
        counts_dict[doc_id] = counts  # Example: {'1000': Counter({'Thi': 1, 'Jane': 1, 'Austen': 1}), '1001': Counter({'is': 2, 'This': 1, 's': 1}), ...}
    return counts_dict

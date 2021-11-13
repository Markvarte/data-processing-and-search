def count_TF(all_query_terms_freq: dict, each_selected_doc_size: dict):
    tf = {}
    for term, term_freq in all_query_terms_freq.items():
        for doc_id, freq in term_freq.items():
            for doc_id_for_size, doc_size in each_selected_doc_size.items():
                if doc_id == doc_id_for_size:
                    tf[f'{doc_id}{term}'] = freq / doc_size
    return tf


def count_IDF(all_doc_amount: int, doc_amount_per_term: dict):
    idf = {}
    for term, doc_amount in doc_amount_per_term.items():
        idf[term] = all_doc_amount / doc_amount
    return idf


def count_TFIDF(tf: dict, idf: dict, join_postings_list: list):
    tf_idf_score = {}
    for doc_id in join_postings_list:
        tf_idf = 0
        # key = '{docId}{term}'
        for key, tf_score in tf.items():
            if key[:4] != doc_id:
                continue
            if key[4:] not in idf:
                idf[key[4:]] = 0
            tf_idf = tf_idf + (tf_score * idf[key[4:]])
        tf_idf_score[doc_id] = tf_idf
    return tf_idf_score

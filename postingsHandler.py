def create_postings(unique_terms_with_id):
    postings_dict = {}
    inc_list_index = 1
    doc_ids_list = []
    for term, doc_id in unique_terms_with_id:
        # in list ...[0] = term, ..[1] = docId
        # if current term equal to next term
        # then add docId to docIds for each term list
        if term == unique_terms_with_id[inc_list_index][0]:
            doc_ids_list.append(doc_id)
        # if current term not equal to next term
        # then add term, docIds list and set docIds list to empty
        elif term != unique_terms_with_id[inc_list_index][0]:
            doc_ids_list.append(doc_id)
            postings_dict[term] = doc_ids_list  # adding new posting to posting dict
            doc_ids_list = []
        # check only current term with next term because list is sorted
        # check if it is last pair and if yes
        # add last term and current docId to list and break the loop
        # otherwise increase the next list index
        if inc_list_index == (len(unique_terms_with_id) - 1):
            # {keyTerm : [docId1, docId2, ... ] }
            postings_dict[unique_terms_with_id[inc_list_index][0]] = [unique_terms_with_id[inc_list_index][1]]
            break
        else:
            inc_list_index += 1
    return postings_dict


def get_all_postings_by_query(postings, query):
    selected_postings_dict = {}
    for term in query:
        selected_postings_dict[term] = get_posting(postings, term)
    return selected_postings_dict


def get_posting(postings_dict, term):
    for key, val in postings_dict.items():
        if term == key:
            return val
    return []

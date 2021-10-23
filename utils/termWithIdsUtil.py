# Creates inverted index
def remove_duplicates_in_term_ids_list(terms_with_id):
    inc_list_index = 1  # included in termsWithId list index
    unique_terms_with_id = []
    for term, doc_id in terms_with_id:
        if not (term == terms_with_id[inc_list_index][0] and doc_id == terms_with_id[inc_list_index][1]):
            unique_list = [term, doc_id]
            unique_terms_with_id.append(unique_list)
        if inc_list_index == (len(terms_with_id) - 1):
            unique_list = terms_with_id[inc_list_index]
            unique_terms_with_id.append(unique_list)
            break
        else:
            inc_list_index += 1
    return unique_terms_with_id

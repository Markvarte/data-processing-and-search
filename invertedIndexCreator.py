import filesHandler
import termWithIdsUtil
import postingsHandler


def create_inverted_index(file_name='sample.txt'):
    terms_with_ids_list = filesHandler.create_terms_with_id_list(file_name)
    create_dictionary(terms_with_ids_list)
    unique_terms_with_id_list = termWithIdsUtil.remove_duplicates_in_term_ids_list(terms_with_ids_list)
    return postingsHandler.create_postings(unique_terms_with_id_list)


# Creates term frequency matrix
def create_dictionary(terms_with_id):
    dictionary = []
    inc_list_index = 1  # included in termsWithId list index
    term_freq = 1

    for term, doc_id in terms_with_id:
        # in list ...[0] = term, ..[1] = docId
        # if current term equal to next term and docId are different
        # then increase frequency
        if term == terms_with_id[inc_list_index][0] and doc_id != terms_with_id[inc_list_index][1]:
            term_freq += 1
        # if current term not equal to next term
        # then add term, frequency pairs to dictionary and set frequency to 1
        elif term != terms_with_id[inc_list_index][0]:
            dic = {term: term_freq}
            dictionary.append(dic)
            term_freq = 1
        # not check for equal terms and frequency both because frequency already set to 1
        # check only current term with next term because list is sorted
        # check if it is last pair and if yes
        # add last term and current frequency to dictionary list and break the loop
        # otherwise increase the next list index
        if inc_list_index == (len(terms_with_id) - 1):
            dic = {terms_with_id[inc_list_index][0]: term_freq}
            dictionary.append(dic)
            break
        else:
            inc_list_index += 1
    return dictionary

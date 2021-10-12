# Creates terms with document ids list
def create_terms_with_id_list(file_name='sample.txt'):
    terms_with_id = []
    with open(file_name, 'r') as f:
        for line in f:
            cur_identifier = line[:4]  # first 4 chars - number
            line = line[5:]  # from text to end
            for term in line.split():
                included_list = [term, cur_identifier]  # every time new list
                terms_with_id.append(included_list)  # [ [term, id], [term2, id2], .. ]
    # Sort list, first by term, second by id.
    terms_with_id.sort()
    return terms_with_id


def write_selected_postings(postings_dict, result_file):
    with open(result_file, 'a') as fw:
        fw.write('GetPostings\n')
        for key, val in postings_dict.items():
            fw.write(key + '\nPostings: ')
            for item in val:
                fw.write(item + " ")
            fw.write("\n")
        fw.write("\n")


def write_query(query, postings_list, result_file, is_and=True):
    with open(result_file, 'a') as fw:
        if is_and:
            fw.write('QueryAnd\n')
        else:
            fw.write('QueryOr\n')
        for term in query:
            fw.write(term + " ")
        fw.write("\nResults: ")
        for doc_id in postings_list:
            fw.write(doc_id + " ")
        fw.write("\n\n")


def split_query(query_file):
    query_list = []
    all_queries_list = []
    with open(query_file, 'r') as f:
        for line in f:
            for term in line.split():
                query_list.append(term)
            all_queries_list.append(query_list)
            query_list = []
    return all_queries_list

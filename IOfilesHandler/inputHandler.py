# Creates terms with document ids list
def create_terms_with_id_list(file_name):
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


def create_docs_terms_dict(file_name):
    docs = {}
    with open(file_name, 'r') as f:
        for line in f:
            # first 4 chars = doc id, other doc content
            # { docid : ['word1', 'word2', 'word3', ... ] }
            docs[line[:4]] = line[5:].split()
    return docs


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

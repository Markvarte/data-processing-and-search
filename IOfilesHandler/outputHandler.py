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

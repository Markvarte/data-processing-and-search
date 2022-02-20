def write_selected_postings(postings_dict, result_file, wildCardmode = False):
    with open(result_file, 'a') as fw:
        fw.write('GetPostings\n')
        for key, val in postings_dict.items():
            fw.write(key + '\nPostings: ')
            for item in val:
                fw.write(item + " ")
            fw.write("\n")
        fw.write("\n")


def write_query(query, postings_list, result_file, query_title):
    with open(result_file, 'a') as fw:
        fw.write(f'{query_title}\n')
        for term in query:
            fw.write(term + " ")
        fw.write("\nResults: ")
        for doc_id in postings_list:
            fw.write(doc_id + " ")
        fw.write("\n\n")


def write_wild_card(template, postings_dict, result_file):
    with open(result_file, 'a') as fw:
        fw.write(f'WildCard\n{template}\nResults:\n')
        for key, val in postings_dict.items():
            fw.write(key + '\nPostings: ')
            for item in val:
                fw.write(item + " ")
            fw.write("\n")
        fw.write("\n")

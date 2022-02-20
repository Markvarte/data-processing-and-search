from invertedIndex import invertedIndexCreator
from queryHandler import queryProcessor

file_name = input("Ievadiet tekstā faila vārdu, kas satur dokumentu identifikatorus un teikumus (dokumentus).. ")
postings_dict = invertedIndexCreator.create_inverted_index(file_name)

query_file_name = input("Ievadiet tekstā faila vārdu, kurā glabājās vaicājums.. ")
result_file_name = input("Ievadiet tekstā faila vārdu, kurā ierakstīt vaicājuma atbildi.. ")
template_file_name = input("Ievadiet teksta faila vardu, kas satur sablonu..")
queryProcessor.process_query(postings_dict, file_name, query_file_name, result_file_name)
queryProcessor.process_substitute_query(postings_dict, template_file_name, result_file_name)

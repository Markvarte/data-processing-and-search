from invertedIndex import invertedIndexCreator
from queryHandler import queryProcessor

# DOTO: uncomment this !
# DOTO: add file_name
# file_name = input("Ievadiet tekstā faila vārdu, kas satur dokumentu identifikatorus un teikumus (dokumentus).. ")
postings_dict = invertedIndexCreator.create_inverted_index()

# DOTO: uncomment this !
# DOTO: add file_name, query_file_name, result_file_name
# result_file_name = input("Ievadiet tekstā faila vārdu, kurā ierakstīt vaicājuma atbildi.. ")
# query_file_name = input("Ievadiet tekstā faila vārdu, kurā glabājās vaicājums.. ")
queryProcessor.process_query(postings_dict)

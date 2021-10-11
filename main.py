import invertedIndexCreator
import queryProcessor


# file_name = input("Ievadiet tekstā faila vārdu, kas satur dokumentu identifikatorus un teikumus (dokumentus).. ")
# !! HERE IN PARAMETER ADD REAL FINE NAME
postings_dict = invertedIndexCreator.create_inverted_index()

# result_file_name = input("Ievadiet tekstā faila vārdu, kurā ierakstīt vaicājuma atbildi.. ")
# query_file_name = input("Ievadiet tekstā faila vārdu, kurā glabājās vaicājums.. ")
# !! HERE IN PARAMETER ADD REAL FINE NAMES
queryProcessor.process_query(postings_dict)

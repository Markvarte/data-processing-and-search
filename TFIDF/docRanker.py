def create_ranked_list(posting_dict: dict):
    # sort by dict values
    posting_dict = dict(sorted(posting_dict.items(), key=lambda item: item[1], reverse=True))
    # return ranked keys only
    return posting_dict.keys()

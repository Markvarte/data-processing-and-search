def query_or(selected_postings_dict: dict):
    join_set = set()
    for key, val in selected_postings_dict.items():
        for item in val:
            join_set.add(item)
    if join_set:
        join_list = list(join_set)
        # .sort() return None.
        join_list.sort()
        return join_list
    else:
        return ['empty']

from permutationIndex import templateTransformer


def get_postings_by_template(posting_dict, rotations_dict, template):
    [template, remainder] = templateTransformer.get_transformed_template(template)
    # find template in rotations, return term
    # find postings by term, return term-posting-dict







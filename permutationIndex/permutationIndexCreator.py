from permutationIndex import templateTransformer
from invertedIndex import postingsHandler


def get_postings_by_template(posting_dict, rotations_dict, origin_template):
    [transformed_template, remainder] = templateTransformer.get_transformed_template(origin_template)
    matched_terms = find_terms(transformed_template, rotations_dict)
    # if remainder not None filter founded terms
    if remainder:
        matched_terms = filter_terms_by_remainder(matched_terms, transformed_template, remainder)
    selected_postings_dict = postingsHandler.get_all_postings_by_query(posting_dict, matched_terms)
    return selected_postings_dict


def find_terms(template, rotation_dict: dict):
    matched_terms = []
    # Need to match template according to star position
    for term, rotations in rotation_dict.items():
        for rotation in rotations:
            if len(rotation) < len(template):
                break
            start_poz = template.find('*')
            if start_poz == -1:
                if rotation == template:
                    matched_terms.append(term)
                    break
            if template.endswith('*'):
                template_without_star = template[:start_poz]
                string_start_end_poz = len(template_without_star)
                #  for *e* case, to not ends with e and not starts with e.
                if rotation.startswith(template_without_star) and rotation[string_start_end_poz] != '$' and not rotation.endswith('$'):
                    matched_terms.append(term)
                    break
            if not template.endswith('*'):
                # Case where start is in the middle of template
                if rotation.startswith(template[:start_poz]) and rotation.endswith(template[start_poz + 1:]):
                    matched_terms.append(term)
                    break
    return matched_terms


def filter_terms_by_remainder(terms, template, remainder):
    # check for remainder start
    # remainder + amount of if remainder is part of any template parts
    star_poz = -1
    remainder_without_star = remainder
    if remainder.find('*') == 0:
        star_poz = 0
        remainder_without_star = remainder[1:]
        min_valid_match_amount = 1 + template.count(remainder_without_star)
    elif remainder.find('*') == (len(remainder) - 1):
        star_poz = len(remainder) - 1
        remainder_without_star = remainder[:len(remainder) - 1]
        min_valid_match_amount = 1 + template.count(remainder_without_star)
    else:
        min_valid_match_amount = 1 + template.count(remainder_without_star)
    matched_terms = []
    for term in terms:
        if star_poz == 0:
            if term[1:].count(remainder_without_star) >= min_valid_match_amount:
                matched_terms.append(term)
        elif star_poz == len(remainder) - 1:
            if term[:len(term) - 1].count(remainder_without_star) >= min_valid_match_amount:
                matched_terms.append(term)
        elif term.count(remainder_without_star) >= min_valid_match_amount:
            matched_terms.append(term)
    return matched_terms

def create_rotations(terms):
    term_rotations = {}
    for term in terms:
        rotations = []
        rotation_left = len(term) - 1
        #  mamma$ -> amma$m -> mma$ma -> ma$mam -> a$mamm
        rotated_term = f'{term}$'
        rotations.append(rotated_term)
        while rotation_left:
            rotated_term = rotated_term[1:] + rotated_term[0]
            rotations.append(rotated_term)
            rotation_left -= 1
        term_rotations[term] = rotations
    return term_rotations

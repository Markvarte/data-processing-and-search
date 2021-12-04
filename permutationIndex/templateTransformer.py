def transform_1star_template(template):
    if template.endswith('*'):
        transformed_template = template + "$"
    else:
        star_poz = template.find('*')
        transformed_template = template[star_poz + 1:] + '$' + template[:star_poz + 1]
    return transformed_template


def transform_2star_template(template: str):
    if template.startswith('*') and template.endswith('*'):
        return template[1:], None
    first_star_poz = template.find('*')
    second_star_poz = template.find("*", first_star_poz + 1)
    template_remainder = template[first_star_poz+1: second_star_poz]
    transformed_template = transform_1star_template(template[:first_star_poz] + template[second_star_poz:])
    return transformed_template, template_remainder


def get_transformed_template(template):
    if template.find('*') == -1:
        return template + '$', None
    start_count = template.count("*")
    if start_count < 2:
        return transform_1star_template(template), None
    else:
        return transform_2star_template(template)

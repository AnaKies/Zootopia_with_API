def get_unique_skin_types(animals_data):
    """
    Extracts from the animals JSON data all skin types.
    :param animals_data: JSON formatted animal data.
    :return: List with unique skin types.
    """
    unique_skin_types = []

    for animal in animals_data:
        if "characteristics" in animal.keys():
            if "skin_type" in animal["characteristics"].keys():
                # create a list with unique skin types
                if (animal["characteristics"]["skin_type"]
                        not in unique_skin_types):
                    unique_skin_types.append(
                        animal["characteristics"]["skin_type"])

    return unique_skin_types


def print_skin_types(unique_skin_types):
    """
    Displays the available skin types or an error message
    if no skin types are available.
    :param unique_skin_types:
    :return: None
    """
    if len(unique_skin_types) == 0:
        print("No skin types found in the animals data.")
        return

    print("Available skin types:")
    for skin_type in unique_skin_types:
        print(f"\t{skin_type}")


def collect_animals_with_selected_skin_type(skin_type, animals_data):
    """
    Collects the animals by selected skin type from the animals JSON data.
    :param skin_type: Skin type as filter criteria.
    :param animals_data: JSON formatted animal data.
    :return: JSON formatted animal data filtered by a selected skin type.
    Number of animals not included in the filtration because
    of the missing skin type parameter.
    """
    filtered_animals = []
    counter_animals_without_skin_type = 0

    for animal in animals_data:
        if "characteristics" in animal.keys():
            if "skin_type" in animal["characteristics"].keys():
                if animal["characteristics"]["skin_type"] == skin_type:
                    filtered_animals.append(animal)
            else:
                counter_animals_without_skin_type += 1

    return filtered_animals, counter_animals_without_skin_type


def print_animals_without_skin_type(counter_animals_without_skin_type):
    """
    Displays the number of animals without skin type,
    which could not participate in the filtering by the skin type.
    :param counter_animals_without_skin_type: Number of animals without
    skin type parameter in their data structure.
    :return:
    """
    if counter_animals_without_skin_type > 0:
        print(f"Attention! "
              f"{counter_animals_without_skin_type} "
              f"animals are not included in the animals data "
              f"because of missing skin type data.")
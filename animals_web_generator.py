import json


def load_data(file_path):
    """
    Loads JSON file.
    :param file_path: path to the JSON file
    :return: JSON data as string
    """
    try:
        # use encoding for correct representation of
        # such special symbols like an apostrophe
        with open(file_path, "r", encoding="utf-8") as json_file:
            return json.load(json_file)

    except FileNotFoundError as error:
        print(f"Error: File {file_path} is not found.\n{error}")
    except json.JSONDecodeError as error:
        print(f"Error: JSON {file_path} is not valid.\n{error}")
    except Exception as error:
        print(f"Error: Unexpected error at reading {file_path}.\n{error}")
    return None


def serialize_animal(animal_obj):
    """
    Serializes a single animal to HTML
    :param animal_obj: dictionary with animal data
    :return: HTML string with animal data
    """
    output_animal_data = ""

    # spare one if check later
    characteristic_is_there = False

    # append information to each string
    output_animal_data += ("<li class='cards__item'>\n"
                           "<div class='card__title'>")

    if "name" in animal_obj.keys():
        output_animal_data += f"{animal_obj['name']}"

    if "taxonomy" in animal_obj.keys():
        if "scientific_name" in animal_obj["taxonomy"].keys():
            scientific_name = animal_obj["taxonomy"]["scientific_name"]
            output_animal_data += f" ({scientific_name})"

    output_animal_data += "</div>\n"

    output_animal_data += ("<div class='card__text'>"
                           "<ul class='animal_list'>")
    if "characteristics" in animal_obj.keys():
        characteristic_is_there = True
        if "diet" in animal_obj["characteristics"].keys():
            diet = animal_obj["characteristics"]["diet"]
            output_animal_data += ("<li class='animal_properties'>"
                                   "<strong>"
                                   "Diet: "
                                   "</strong>")
            output_animal_data += f"{diet}</li>\n"

    if "locations" in animal_obj.keys():
        if animal_obj["locations"]:  # check if the list is not empty
            first_location = animal_obj["locations"][0]
            output_animal_data += ("<li class='animal_properties'>"
                                   "<strong>"
                                   "Location: "
                                   "</strong>")
            output_animal_data += f"{first_location}</li>\n"

    if characteristic_is_there:
        if "type" in animal_obj["characteristics"]:
            type_of_animal = animal_obj["characteristics"]["type"]
            output_animal_data += ("<li class='animal_properties'>"
                                   "<strong>"
                                   "Type: "
                                   "</strong>")
            output_animal_data += f"{type_of_animal}</li>\n"

        if "lifespan" in animal_obj["characteristics"]:
            lifespan = animal_obj["characteristics"]["lifespan"]
            output_animal_data += ("<li class='animal_properties'>"
                                   "<strong>"
                                   "Lifespan: "
                                   "</strong>")
            output_animal_data += f"{lifespan}</li>\n"

        if "skin_type" in animal_obj["characteristics"]:
            lifespan = animal_obj["characteristics"]["skin_type"]
            output_animal_data += ("<li class='animal_properties'>"
                                   "<strong>"
                                   "Skin type: "
                                   "</strong>")
            output_animal_data += f"{lifespan}</li>\n"

    output_animal_data += ("</ul>"
                           "</div>"
                           "</li>\n")

    return output_animal_data


def serialize_all_animals(animals_data):
    """
    Create HTML with animal data.
    :param animals_data: JSON-formatted animal data.
    :return: String with HTML-formatted animal data.
    """
    output_animals_data = ""

    for animal in animals_data:
        output_animals_data += serialize_animal(animal)

    return output_animals_data


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


def get_template_html():
    """
    Reads the content of the template HTML file.
    :return: Content of the tamplate HTML file.
    """
    try:
        file_name = "animals_template.html"
        # use encoding for correct representation of
        # such special symbols like an apostrophe
        with open(file_name, "r", encoding="utf-8") as html_file:
            return html_file.read()

    except FileNotFoundError as error:
        print(f"Error: File {file_name} is not found.\n{error}")
    except json.JSONDecodeError as error:
        print(f"Error: JSON {file_name} is not valid.\n{error}")
    except Exception as error:
        print(f"Error: Unexpected error at reading {file_name}.\n{error}")
    return None


def create_html_file(file_name, html_content):
    """
    Writes the content of the HTML file to the HTML file.
    :param file_name: Name of the HTML file.
    :param html_content: HTML content of the HTML file as string.
    :return: None
    """
    try:
        # use encoding for correct representation of
        # such special symbols like an apostrophe
        with open(file_name, "w", encoding="utf-8") as html_file:
            html_file.write(html_content)

    except FileNotFoundError as error:
        print(f"Error: File {file_name} is not found.\n{error}")
    except json.JSONDecodeError as error:
        print(f"Error: JSON {file_name} is not valid.\n{error}")
    except Exception as error:
        print(f"Error: Unexpected error at writing {file_name}.\n{error}")


def insert_new_data_in_html_template(original_html, new_text):
    """
    Replaces HTML content with new text.
    :param original_html: The HTML content of the HTML file as string.
    :param new_text: Text for replacement.
    :return: New HTML content with replaced text.
    """
    if "__REPLACE_ANIMALS_INFO__" not in original_html:
        raise Exception("Error: the "
                        "__REPLACE_ANIMALS_INFO__ "
                        "is not in the template.")

    html_text_replaced = original_html.replace(
        "__REPLACE_ANIMALS_INFO__",
        new_text)
    return html_text_replaced


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


def get_user_input(unique_skin_types):
    """
    Gets the selected skin type from the user input.
    :param unique_skin_types: Unique skin types for all animals.
    :return: Selected skin type by the user.
    """
    while True:
        selected_skin_type = input("Select a skin type to use: ")
        if selected_skin_type in unique_skin_types:
            break
        print("Invalid skin type.")

    return selected_skin_type


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


def main():
    """
    The user chooses a skin type for an animal from the
    list of available skin types. Then the HTML is generated containing
    all the animals with the selected skin type.
    """
    try:
        # get JSON data
        animals_data = load_data("animals_data.json")

        # manage the skin type
        unique_skin_types = get_unique_skin_types(animals_data)
        print_skin_types(unique_skin_types)
        selected_skin_type = get_user_input(unique_skin_types)
        animals_with_selected_skin, counter_animals_without_skin_type = (
            collect_animals_with_selected_skin_type(
                selected_skin_type, animals_data))
        print_animals_without_skin_type(counter_animals_without_skin_type)

        # manage the HTML
        html_formatted_animals = serialize_all_animals(
            animals_with_selected_skin)
        template_html_for_animals = get_template_html()
        full_html_with_animals = insert_new_data_in_html_template(
            template_html_for_animals, html_formatted_animals)
        file_name = "animals.html"
        create_html_file(file_name, full_html_with_animals)
        print(f"The website {file_name} was generated for "
              f"animals with selected skin type.")

    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()

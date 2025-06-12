import json


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


def serialize_animal(animal_obj):
    """
    Serializes a single animal to HTML
    :param animal_obj: dictionary with animal data
    :return: HTML string with animal data
    """
    output_animal_data = ""

    # spare one if check later
    has_characteristics = False

    # append information to each string
    output_animal_data += ("<li class='cards__item'>\n"
                           "<div class='card__title'>")

    if "name" in animal_obj:
        output_animal_data += f"{animal_obj['name']}"

    if "taxonomy" in animal_obj:
        if "scientific_name" in animal_obj["taxonomy"].keys():
            scientific_name = animal_obj["taxonomy"]["scientific_name"]
            output_animal_data += f" ({scientific_name})"

    output_animal_data += "</div>\n"

    output_animal_data += ("<div class='card__text'>"
                           "<ul class='animal_list'>")
    if "characteristics" in animal_obj.keys():
        has_characteristics = True
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

    if has_characteristics:
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
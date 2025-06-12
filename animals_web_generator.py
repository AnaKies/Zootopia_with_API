from manage_skin_type import *
from manage_html import *


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

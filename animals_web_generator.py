from manage_html import *
from html_communication import search_for_animal_in_api


def get_user_input_for_skin_type(unique_skin_types):
    """
    Gets the selected skin type from the user input.
    :param unique_skin_types: Unique skin types for all animals.
    :return: Selected skin type by the user.
    """
    while True:
        selected_skin_type = input("Select a skin type to use: ").strip()
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
        chosen_animal = input("Enter a name of an animal: ").strip()

        # get JSON data from API
        animals_data = search_for_animal_in_api(chosen_animal)
        if animals_data:
            html_formatted_text = serialize_all_animals(animals_data)
        else:
            html_formatted_text = create_message_missing_animal(chosen_animal)
            print("No animals found.")

        template_html_for_animals = get_template_html()
        full_html_with_animals = insert_new_data_in_html_template(
            template_html_for_animals, html_formatted_text)
        file_name = "animals.html"
        create_html_file(file_name, full_html_with_animals)
        print(f"Website was successfully generated to the file {file_name}.")
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()

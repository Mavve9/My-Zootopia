import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')


def load_html_data(file_path):
    """ Loads an HTML file and returns its content """
    with open(file_path, "r", encoding="utf-8") as file:
        animals_template = file.read()
    return animals_template


def animal_name(animal):
    name_value = animal.get("name")
    if name_value is not None:
        return f"Name: {name_value}"
    return None


def animal_diet(animal):
    diet_key = animal.get("characteristics", {})
    diet_value = diet_key.get("diet")
    if diet_value is not None:
        return f"Diet: {diet_value}"
    return None


def animal_locations(animal):
    all_locations = animal.get("locations", [])
    if all_locations:
        first_location = all_locations[0]
        return f"Location: {first_location}"
    return None

def animal_type(animal):
    type_key = animal.get("characteristics", {})
    type_value = type_key.get("type")
    if type_value is not None:
        return f"Type: {type_value}"
    return None

json_animal_data = {
    "name": animal_name,
    "diet": animal_diet,
    "location": animal_locations,
    "type": animal_type
}


def main():
    one_string_output = ""

    for animal in animals_data:
        all_animals = []

        for category in json_animal_data.values():
            value = category(animal)
            if value is not None:
                all_animals.append(value)

        one_string_output += "<li class='cards__item'>\n"
        for item in all_animals:
            one_string_output += f"{item}<br/>\n"
        one_string_output += "</li>\n"


    old_template = load_html_data("animals_template.html")
    overwritten_template = old_template.replace("__REPLACE_ANIMALS_INFO__", one_string_output)

    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(overwritten_template)

if __name__ == "__main__":
    main()

import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')


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

tasks = {
    "name": animal_name,
    "diet": animal_diet,
    "location": animal_locations,
    "type": animal_type
}


def main():
    index = 0
    total_animals = len(animals_data)

    while index < total_animals:
        animal = animals_data[index]

        results = []

        for task in tasks.values():
            value = task(animal)
            if value is not None:
                results.append(value)

        for item in results:
            print(item)

        index += 1
        print()


if __name__ == "__main__":
    main()
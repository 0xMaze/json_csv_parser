from hashlib import new
from json import dump, load
from csv import writer


def json_to_csv(json_file, csv_file):
    with open(json_file) as json_file:
        jsondata = load(json_file)

    data_file = open(csv_file, "w", newline="")
    csv_writer = writer(data_file)

    count = 0
    for data in jsondata:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(data.values())

    data_file.close()


def set_new_item():
    name = input("Name: ")
    birthday = input("Birthday: ")
    height = input("Height: ")
    weight = input("Weight: ")
    car = input("Car(Y/N): ")

    if car == "Y":
        car = True
    elif car == "N":
        car = False

    languages = input("Languages (WITH SPACES), press ENTER if none: ")
    if languages == "":
        languages = None
    else:
        languages = languages.split(" ")

    data = {
        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": car,
        "languages": languages,
    }

    return data


def find_person_by_name(json_file):
    name = input("Name: ")

    with open(json_file) as json_file:
        jsondata = load(json_file)

    for data in jsondata:
        if data["name"] == name:
            print(data)
    return None


def write_json(json_file, new_data=None):
    if new_data is None:
        new_data = set_new_item()

    with open(json_file, "r") as f:
        data = load(f)

    data.append(new_data)

    with open(json_file, "w") as f:
        dump(data, f)
    return


def write_csv(csv_file, new_data=None):
    if new_data is None:
        new_data = set_new_item()

    with open(csv_file, "a", newline="") as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerow(new_data.values())


def find_by_language(json_file):
    found_people = []

    with open(json_file) as json_file:
        jsondata = load(json_file)

    language = input("Language: ")

    for data in jsondata:
        if language in data["languages"]:
            found_people.append(data)

    if len(found_people) == 0:
        print("No people found")
        return
    else:
        for person in found_people:
            print(person["name"])
        return


def filter_by_height(json_file):
    with open(json_file) as json_file:
        jsondata = load(json_file)

    selected_year = int(input("Year: "))
    average_height = 0
    count = 0

    for data in jsondata:
        if int(data["birthday"][-4:]) < selected_year:
            count += 1
            average_height += float(data["height"])

    return average_height


def main():
    while True:
        print(
            """
        1. Add new item
        2. Convert JSON to CSV
        3. Find by name
        4. Find by language
        5. Filter by height
        6. Exit
        """
        )

        choice = input("Choice: ")

        if choice == "1":
            new_data = set_new_item()
            write_json("data.json", new_data)
            write_csv("data.csv", new_data)
        elif choice == "2":
            json_to_csv("data.json", "data.csv")
        elif choice == "3":
            find_person_by_name("data.json")
        elif choice == "4":
            find_by_language("data.json")
        elif choice == "5":
            print(filter_by_height("data.json"))
        elif choice == "6":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

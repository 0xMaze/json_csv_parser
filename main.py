from json import dump, load
from csv import writer


# def add_new_item(FUNCTION):
#     def wrapper(json_file, csv_file):
#         new_data = set_new_item()
#         FUNCTION(json_file, csv_file)
#         return new_data

#     return wrapper

# TODO: Add new item


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

    languages = input("Languages (WITH SPACES): ")
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


def write_json(json_file):
    with open(json_file, "r") as f:
        data = load(f)

    new_data = set_new_item()

    data.append(new_data)

    with open(json_file, "w") as f:
        dump(data, f)
    return


def write_csv(csv_file):
    new_data = set_new_item()

    with open(csv_file, "a", newline="") as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerow(new_data.values())


def find_by_name(json_file):
    with open(json_file) as json_file:
        jsondata = load(json_file)

    name = input("Name: ")

    for data in jsondata:
        if data["name"] == name:
            print(data)
            return
    print("No data found")
    return


def find_by_language(json_file):
    with open(json_file) as json_file:
        jsondata = load(json_file)

    language = input("Language: ")

    for data in jsondata:
        if language in data["languages"]:
            print(data)
            return
    print("No data found")
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
        2. Write JSON file
        3. Write CSV file
        4. Find by name
        5. Find by language
        6. Filter by height
        7. Exit
        """
        )

        choice = input("Choice: ")

        if choice == "1":
            write_json("data.json")
            write_csv("data.csv")
        elif choice == "2":
            json_to_csv("data.json", "data.csv")
        elif choice == "3":
            write_csv("data.csv")
        elif choice == "4":
            find_by_name("data.json")
        elif choice == "5":
            find_by_language("data.json")
        elif choice == "6":
            print(filter_by_height("data.json"))
        elif choice == "7":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

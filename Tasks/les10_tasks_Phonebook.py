# Phonebook application
import json


class EmptyError(Exception):
    pass


def find_info(my_dict: dict) -> None:
    info = input("Enter number: ")
    try:
        for k, v in my_dict[info].items():
            print(k, v)
    except KeyError as err:
        print(err)


def add_info(my_dict: dict) -> None:
    book_date = ["name", "surname", "fullname", "phone_number", "city", "state"]
    phone = input("Enter phone ")
    my_dict[phone] = {}
    for i in book_date:
        print(f"add: {i}")
        my_dict[phone][i] = input()


def del_info(my_dict: dict) -> None:
    if input("YES if you want delete all record").upper() == 'YES':
        number = input("Enter number: ")
        del my_dict[number]
    else:
        number = input("Enter number if record : ")
        info = input("Enter info what you want delete: ")
        del my_dict[number][info]


def update_ingo(my_dict: dict) -> None:
    dict_options_update = {"Update all info about number ": 1, "Update some info about number ": 2}
    for k_u, v_u in dict_options_update.items():
        print(f"{k_u} {v_u}", end=" ")
    options_update = int(input("Enter number of options: "))
    if options_update == 1:
        number_update = input("Enter number for update: ")
        for key in my_dict[number_update].keys():
            print(key)
            my_dict[number_update][key] = input("Enter new info: ")
    if options_update == 2:
        number_update = input("Enter number for update: ")
        key_update = input("Enter info for update: ")
        my_dict[number_update][key_update] = input("Enter new info: ")


def main():
    phone_book = input("Enter name of Phonebook ") + ".json"

    with open(phone_book, 'r', encoding="utf-8") as fo:
        Phonebook_application = json.load(fo)
        if len(Phonebook_application) == 0:
            raise EmptyError("Empty dict")

        while True:
            dict_options = {"Add new entries: ": 1,
                            "Search: ": 2,
                            "Delete a record: ": 3,
                            "Update a record: ": 4,
                            "End program: ": 5}

            for k, v in dict_options.items():
                print(f"{k} {v}", end=" ")
            print()

            options = int(input("Enter number of options: "))
            if options == 1:
                add_info(Phonebook_application)
                print("Record is added")
            elif options == 2:
                find_info(Phonebook_application)
            elif options == 3:
                del_info(Phonebook_application)
                print("Record is delete")
            elif options == 4:
                update_ingo(Phonebook_application)
                print("Record is updated")

            end = input("If you want end the program enter: YES ")
            if options == 5 or end.upper() == "YES":
                break

    with open("My_phonebook.json", 'w', encoding="utf-8") as fi:
        json.dump(Phonebook_application, fi)


if __name__ == "__main__":
    main()

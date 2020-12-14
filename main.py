import json
import math
import os
import random

DATA_FILE_PATH = "./data"

SQUARES = 25

BALANCING = {
    "generic": 0.75,
    "stage": 0.25
}

STAGE_BALANCING = [
    0.36, 0.24, 0.2, 0.12, 0.08
]

LABELS = {
    "am": "(Aquatic Mine)", "dc": "(Death Chamber)", "dl": "(Dry Lagoon)", 
    "eq": "(Egg Quarters)", "mh": "(Meteor Herd)",   "ms": "(Mad Space)", 
    "ph": "(Pumpkin Hill)", "sh": "(Security Hall)", "wc": "(Wild Canyon)"
}

STAGE_ORDER = {
    "knuckles"  : ["wc", "ph", "am", "dc", "mh"],
    "rouge"     : ["dl", "eq", "sh", "ms"]
}


def read_data_files(character=""):
    data = {}

    directory = DATA_FILE_PATH

    if character != "":
        data = [[]] * 5
        directory = f"{DATA_FILE_PATH}/stages/{character}"

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    for f in files:
        file_name = f.split(".")[0]

        with open(os.path.join(directory, f), 'r') as file_object:
            file_data = file_object.read()

            if character != "":
                data[STAGE_ORDER[character].index(file_name)] = file_data.split(",")
            else:
                data[file_name] = file_data.split(",")
    
    return data

def get_bingo_data():
    bingo_data = {
        "generic": {
            "hero": [

            ],
            "dark": [

            ],
            "other": [

            ]
        }, 
        "stages": {
            "hero": {
                "knuckles": {
                    "wc": [],
                    "ph": [],
                    "am": [],
                    "dc": [],
                    "mh": [],
                }
            },
            "dark": {
                "rouge": {
                    "dl": [],
                    "eq": [],
                    "sh": [],
                    "ms": []
                },
            }
        }
    }

    bingo_data["generic"] = read_data_files()

    bingo_data["stages"]["hero"]["knuckles"] = read_data_files("knuckles")
    bingo_data["stages"]["dark"]["rouge"] = read_data_files("rouge")

    # hero stages = ['s1', 's1', 's1', 'd1', 's2', 's2', 's3', 's3', 's4', 's5']
    # dark stages = ['s1', 's1', 's1', 's1', 's1', 's2', 's3', 's3', 's4', 's4']

    return bingo_data

def choices(bingo_data, style, allowed_pool=[]):
    squares = []

    if style in "hd":
        amount_generic_squares = math.ceil(SQUARES * BALANCING["generic"])

        for i in range(amount_generic_squares):
            rand = random.randint(0, 1)
            pool = bingo_data["generic"][allowed_pool[rand]]

            choice = random.choice(pool) 
            squares.append(choice)

            bingo_data["generic"][allowed_pool[rand]].remove(choice)

        for i in range(SQUARES - amount_generic_squares):
            character = random.choice(list(bingo_data["stages"][allowed_pool[0]].keys()))
            stage = random.choice(list(bingo_data["stages"][allowed_pool[0]][character].values()))
            
            square = random.choice(list(character[stage]))
            squares.append(f"{square} {LABELS[stage]}")

            bingo_data["stages"][allowed_pool[0]][character][stage].remove(square)
            
    elif style == "k":
        for index, stage in STAGE_ORDER:
            for i in range(math.ceil(SQUARES * STAGE_BALANCING[index])):
                values = bingo_data["stages"]["hero"]["knuckles"][stage].values()

                choice = random.choice(values)
                squares.append(choice)
                bingo_data["stages"]["hero"]["knuckles"][stage].remove(choice)

        # for i in range(9):
        #     number = random.randint(0, len(s1) - 1)
        #     squares.append(str(s1[number]))
        #     s1.pop(number)

        # for i in range(6):
        #     number = random.randint(0, len(s2) - 1)
        #     squares.append(str(s2[number]))
        #     s2.pop(number)

        # for i in range(5):
        #     number = random.randint(0, len(s3) - 1)
        #     squares.append(str(s3[number]))
        #     s3.pop(number)

        # for i in range(3):
        #     number = random.randint(0, len(s4) - 1)
        #     squares.append(str(s4[number]))
        #     s4.pop(number)

        # for i in range(2):
        #     number = random.randint(0, len(s5) - 1)
        #     squares.append(str(s5[number]))
        #     s5.pop(number)

    else:
        for index, stage in STAGE_ORDER:
            for i in range(math.ceil(SQUARES * STAGE_BALANCING[index])):
                values = bingo_data["stages"]["dark"]["rouge"][stage].values()

                choice = random.choice(values)
                squares.append(choice)
                bingo_data["stages"]["dark"]["rouge"][stage].remove(choice)

        # for i in range(11):
        #     number = random.randint(0, len(s1) - 1)
        #     squares.append(str(s1[number]))
        #     s1.pop(number)

        # for i in range(6):
        #     number = random.randint(0, len(s2) - 1)
        #     squares.append(str(s2[number]))
        #     s2.pop(number)

        # for i in range(5):
        #     number = random.randint(0, len(s3) - 1)
        #     squares.append(str(s3[number]))
        #     s3.pop(number)

        # for i in range(3):
        #     number = random.randint(0, len(s4) - 1)
        #     squares.append(str(s4[number]))
        #     s4.pop(number)

    return(squares)

def out(squares):
    bingo_board = {}
    bingo_board["bingo"] = []

    for i in range(len(squares)):
        bingo_board["bingo"].append({
            'name': str(squares[i])
        })
        print(squares[i])

    with open("output.json", 'w') as outfile:
        json.dump(bingo_board, outfile)


def main():
    print("h = hero, d = dark, k = knuckles centi, r = rouge centi")

    style = input()

    allowed_pool = []
    if style == "h":
        allowed_pool = ["hero", "other"]

    elif style == "d":
        allowed_pool = ["dark", "other"]

    bingo_data = get_bingo_data()
    squares = choices(bingo_data, style, allowed_pool)
    out(squares)

if __name__ == "__main__":
    main()





import random
import json

def data(style):
    story = []
    stages = []
    #Load in knuckles pieces
    if style == "k" or style == "h":
        # Pieces
        f = open("wc.txt", "r")
        bingo = f.read()
        s1 = bingo.split(",")
        f.close()
        f = open("ph.txt", "r")
        bingo = f.read()
        s2 = bingo.split(",")
        f.close()
        f = open("am.txt", "r")
        bingo = f.read()
        s3 = bingo.split(",")
        f.close()
        f = open("dc.txt", "r")
        bingo = f.read()
        s4 = bingo.split(",")
        f.close()
        f = open("mh.txt", "r")
        bingo = f.read()
        s5 = bingo.split(",")
        f.close()
    #Load in rouge pieces
    else:
        f = open("dl.txt", "r")
        bingo = f.read()
        s1 = bingo.split(",")
        f.close()
        f = open("eq.txt", "r")
        bingo = f.read()
        s2 = bingo.split(",")
        f.close()
        f = open("sh.txt", "r")
        bingo = f.read()
        s3 = bingo.split(",")
        f.close()
        f = open("ms.txt", "r")
        bingo = f.read()
        s4 = bingo.split(",")
        f.close()
        s5=[]
    #load in hero bingo squares and others
    if style == "h":
        stages = ['s1', 's1', 's1', 'd1', 's2', 's2', 's3', 's3', 's4', 's5']
        f = open("hero.txt", "r")
        bingo = f.read()
        story = bingo.split(",")
        f.close()
        f = open("other.txt", "r")
        bingo = f.read()
        story += bingo.split(",")
        f.close()
    # load in dark bingo squares and others
    elif style == "d":
        stages = ['s1', 's1', 's1', 's1', 's1', 's2', 's3', 's3', 's4', 's4']
        f = open("dark.txt", "r")
        bingo = f.read()
        story = bingo.split(",")
        f.close()
        f = open("other.txt", "r")
        bingo = f.read()
        story += bingo.split(",")
        f.close()

    return (story, s1, s2, s3, s4, s5, stages)

def choices(style, story, s1, s2, s3, s4, s5, stages):
    squares = []
    if style == "h" or style == "d":
        for i in range(19):
            number = random.randint(0, len(story) - 1)
            squares.append(str(story[number]))
            story.pop(number)

        for i in range(6):
            number = random.randint(0, len(stages) - 1)
            stage = (str(stages[number]))
            if stage == "s1":
                number = random.randint(0, len(s1) - 1)
                squares.append(str(s1[number]))
                s1.pop(number)
            elif stage == "s2":
                number = random.randint(0, len(s2) - 1)
                squares.append(str(s2[number]))
                s2.pop(number)
            elif stage == "s3":
                number = random.randint(0, len(s3) - 1)
                squares.append(str(s3[number]))
                s3.pop(number)
            elif stage == "s4":
                number = random.randint(0, len(s4) - 1)
                squares.append(str(s4[number]))
                s4.pop(number)
            elif stage == "s5":
                number = random.randint(0, len(s5) - 1)
                squares.append(str(s5[number]))
                s5.pop(number)

    elif style == "k":
        for i in range(9):
            number = random.randint(0, len(s1) - 1)
            squares.append(str(s1[number]))
            s1.pop(number)
        for i in range(6):
            number = random.randint(0, len(s2) - 1)
            squares.append(str(s2[number]))
            s2.pop(number)
        for i in range(5):
            number = random.randint(0, len(s3) - 1)
            squares.append(str(s3[number]))
            s3.pop(number)
        for i in range(3):
            number = random.randint(0, len(s4) - 1)
            squares.append(str(s4[number]))
            s4.pop(number)
        for i in range(2):
            number = random.randint(0, len(s5) - 1)
            squares.append(str(s5[number]))
            s5.pop(number)
    else:
        for i in range(11):
            number = random.randint(0, len(s1) - 1)
            squares.append(str(s1[number]))
            s1.pop(number)
        for i in range(6):
            number = random.randint(0, len(s2) - 1)
            squares.append(str(s2[number]))
            s2.pop(number)
        for i in range(5):
            number = random.randint(0, len(s3) - 1)
            squares.append(str(s3[number]))
            s3.pop(number)
        for i in range(3):
            number = random.randint(0, len(s4) - 1)
            squares.append(str(s4[number]))
            s4.pop(number)
    return(squares)

def out(squares):
    bingo_board = {}
    bingo_board['bingo'] = []
    for i in range(len(squares)):
        bingo_board['bingo'].append({
            'name': str(squares[i])
        })
        print(squares[i])

    with open('data.txt', 'w') as outfile:
        json.dump(bingo_board, outfile)


def main():
    print("h = hero, d = dark, k = knuckles centi, r = rouge centi")
    style = input()
    story, s1, s2, s3, s4, s5, stages = data(style)
    squares = choices(style, story, s1, s2, s3, s4, s5, stages)
    out(squares)

main()





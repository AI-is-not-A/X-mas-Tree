# H = Height of tree
# W = Width of tree
# I = Interval of decorations

# Coordinates of 'X'
# L = Line index
# C = Column index

matrix = []


def ask_for_parameters():
    while True:
        try:
            parameters = input("Type the number of lines (min. 3) and the interval for the decoration \n").split()
            parameters = [int(x) for x in parameters]
            assert int(parameters[0]) >= 3
            break
        except ValueError:
            print("Invalid format")
        except AssertionError:
            print("Please minimum 3 lines")
    return parameters


def determine_width_height_of_matrix(number_lines):
    width = number_lines * 2 - 1
    height = number_lines + 2
    return width, height


def init_matrix(width, height):
    for _ in range(height):
        line = []
        for _ in range(width):
            line.append(' ')
        matrix.append(line.copy())


def set_postcard_borders(width, height):
    for line in range(height):
        if line == 0 or line == height - 1:
            for column in range(width):
                matrix[line][column] = '-'
        else:
            matrix[line][0] = '|'
            matrix[line][width - 1] = '|'


def set_sentence_merry_xmas():
    sentence = "Merry Xmas"
    for i in range(20, 30):
        matrix[27][i] = sentence[i - 20]


def set_tree_without_decoration(H, L, C):
    matrix[L][C] = 'X'
    matrix[L + 1][C] = '^'

    steps_left = 1
    for i in range(L + 2, L + 2 + H - 1):
        for j in range(C - steps_left, C + steps_left + 1):
            if j == C - steps_left:
                matrix[i][j] = "/"
            elif j == C + steps_left:
                matrix[i][j] = "\\"
            else:
                matrix[i][j] = "*"
        steps_left += 1

    matrix[L + 2 + H - 1][C - 1] = '|'
    matrix[L + 2 + H - 1][C + 1] = '|'


def place_decoration(H, I, L, C):
    deco_position_number = 1
    for line in range(L + 2, L + 2 + H - 1):
        for number_deco_in_line in range(line - L - 2):
            if deco_position_number == 1 or (deco_position_number - 1) % I == 0:
                matrix[line][C - line + L + 3 + (2 * number_deco_in_line)] = 'O'
            deco_position_number += 1


def show_matrix():
    for line in matrix:
        print(''.join(line))


def main():
    parameters = ask_for_parameters()

    if len(parameters) == 2:
        width, height = determine_width_height_of_matrix(parameters[0])
        init_matrix(width, height)

        set_tree_without_decoration(parameters[0], 0, int(width / 2))
        place_decoration(parameters[0], parameters[1], 0, int(width / 2))
    else:
        init_matrix(50, 30)
        set_postcard_borders(50, 30)
        set_sentence_merry_xmas()

        for i in range(0, len(parameters), 4):
            set_tree_without_decoration(parameters[i + 0], parameters[i + 2], parameters[i + 3])
            place_decoration(parameters[i + 0], parameters[i + 1], parameters[i + 2], parameters[i + 3])

    show_matrix()


main()
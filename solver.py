from algorithms import *
import moves  
WHITE  = 'W'
GREEN  = 'G'
RED    = 'R'
BLUE   = 'B'
ORANGE = 'O'
YELLOW = 'Y'

WHITE_EDGES = [
    (WHITE, GREEN),
    (WHITE, RED),
    (WHITE, BLUE),
    (WHITE, ORANGE)
]
#to lift bottom layer white edge based on side-colour
FACE_MAP = {
    GREEN:  "F",
    RED:    "R",
    BLUE:   "B",
    ORANGE: "L"
}
#temp cube 
def copy_cube(cube):
    return [face[:] for face in cube]

def apply_sequence_to_temp(cube, sequence):
    for move in sequence.split():
        apply_virtual_move(cube, move)

def apply_virtual_move(cube, move):
    if move == 'U':
        moves.turn_U(cube)
    elif move == "U'":
        moves.turn_U_prime(cube)
    elif move == 'F':
        moves.turn_F(cube)
    elif move == "F'":
        moves.turn_F_prime(cube)
    elif move == 'R':
        moves.turn_R(cube)
    elif move == "R'":
        moves.turn_R_prime(cube)
    elif move == 'L':
        moves.turn_L(cube)
    elif move == "L'":
        moves.turn_L_prime(cube)
    elif move == 'B':
        moves.turn_B(cube)
    elif move == "B'":
        moves.turn_B_prime(cube)
    elif move == 'D':
        moves.turn_D(cube)
    elif move == "D'":
        moves.turn_D_prime(cube)


def find_edge(cube, color1, color2):
    edge_pairs = [
        ((0, 7), (2, 1)), ((0, 3), (1, 1)),
        ((0, 1), (4, 1)), ((0, 5), (3, 1)),
        ((2, 3), (1, 5)), ((1, 3), (4, 5)),
        ((4, 3), (3, 5)), ((3, 3), (2, 5)),
        ((2, 7), (5, 1)), ((1, 7), (5, 3)),
        ((4, 7), (5, 7)), ((3, 7), (5, 5))
    ]

    for (f1,i1),(f2,i2) in edge_pairs:
        c1 = cube[f1][i1]
        c2 = cube[f2][i2]

        if c1 == color1 and c2 == color2:
            return (f1, i1)
        elif c1 == color2 and c2 == color1:
            return (f2, i2)

    return None
#top-layer
def is_white_edge_solved(cube, white, side_color):
    pos = find_edge(cube, white, side_color)
    if pos is None:
        return False

    face, _ = pos
    if face != 0:
        return False

    if side_color == GREEN:  return cube[2][4] == GREEN
    if side_color == RED:    return cube[3][4] == RED
    if side_color == BLUE:   return cube[4][4] == BLUE
    if side_color == ORANGE: return cube[1][4] == ORANGE

    return False

def solve_white_cross(cube):
    temp_cube = copy_cube(cube)
    solution = []
    for white, side_color in WHITE_EDGES:
        while not is_white_edge_solved(temp_cube, white, side_color):
            pos = find_edge(temp_cube, white, side_color)
            if pos is None:
                break

            face, _ = pos

            # Case 1: White edge is on bottom
            if face == 5:
                 move = FACE_MAP[side_color]
                 solution.extend([move, move])
                 apply_virtual_move(temp_cube, move)
                 apply_virtual_move(temp_cube, move)

            # Case 2: White edge is in middle layer
            elif face in [1, 2, 3, 4]:
                solution.append("U")
                apply_virtual_move(temp_cube, "U")

            # Case 3: White edge is on top but is not aligned
            elif face == 0:
                solution.append("U")
                apply_virtual_move(temp_cube, "U")

    return " ".join(solution)
def find_corner(cube, color1, color2, color3):
    
    corner_triplets = [
        # Top Layer
        ((2, 0), (1, 2), (0, 6)), # Front, Left, Top
        ((1, 0), (4, 2), (0, 0)), # Left, Back, Top
        ((4, 0), (3, 2), (0, 2)), # Back, Right, Top
        ((3, 0), (2, 2), (0, 8)), # Right, Front, Top

        # Bottom Layer
        ((2, 6), (1, 8), (5, 0)), # Front, Left, Down
        ((1, 6), (4, 8), (5, 6)), # Left, Back, Down
        ((4, 6), (3, 8), (5, 8)), # Back, Right, Down
        ((3, 6), (2, 8), (5, 2))  # Right, Front, Down
    ]

    target = {color1, color2, color3}
    for triplet in corner_triplets:
        # Co-ords
        (f1, i1) = triplet[0]
        (f2, i2) = triplet[1]
        (f3, i3) = triplet[2]

        col = {cube[f1][i1], cube[f2][i2], cube[f3][i3]}

        if col == target:
            if cube[f1][i1] == color1: return (f1, i1)
            if cube[f2][i2] == color1: return (f2, i2)
            if cube[f3][i3] == color1: return (f3, i3)

    return None
def solve_white_corners(cube):
    temp_cube = copy_cube(cube)
    solution = []

    WHITE_CORNERS = [
        (WHITE, GREEN, RED),
        (WHITE, RED, BLUE),
        (WHITE, BLUE, ORANGE),
        (WHITE, ORANGE, GREEN)
    ]

    for colors in WHITE_CORNERS:

        while True:
            pos =find_corner(temp_cube, *colors)
            if pos is None:
                break

            face, _ = pos

            # already solved
            if face == 0:
                break

            # rotate D 
            solution.append("D")
            apply_virtual_move(temp_cube, "D")

            # right-hand algorithm
            solution.extend(["R", "U", "R'", "U'"])
            apply_virtual_move(temp_cube, "R")
            apply_virtual_move(temp_cube, "U")
            apply_virtual_move(temp_cube, "R'")
            apply_virtual_move(temp_cube, "U'")

    return " ".join(solution)

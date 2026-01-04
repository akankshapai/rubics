import random

def init_cube():
    return [
        ['W'] * 9,  
        ['O'] * 9,  
        ['G'] * 9,  
        ['R'] * 9,  
        ['B'] * 9,  
        ['Y'] * 9   
    ]

def scramble(cube, num_moves=20):

    sequence = [] # To store moves

    move_map = {
        'R': turn_R,  "R'": turn_R_prime,
        'L': turn_L,  "L'": turn_L_prime,
        'U': turn_U,  "U'": turn_U_prime,
        'D': turn_D,  "D'": turn_D_prime,
        'F': turn_F,  "F'": turn_F_prime,
        'B': turn_B,  "B'": turn_B_prime,
    }

    move_list = list(move_map.keys()) # List of possible moves

    for _ in range(num_moves):
        move = random.choice(move_list) # Random move
        action_function = move_map[move]
        action_function(cube)
        sequence.append(move)

    scramble_seq = ' '.join(sequence)
    print(f"Scramble sequence: {scramble_seq}")
    return scramble_seq

def rotate_face_clockwise(face_arr):
    return [
        face_arr[6], face_arr[3], face_arr[0], # 1st row
        face_arr[7], face_arr[4], face_arr[1], # 2nd row
        face_arr[8], face_arr[5], face_arr[2]  # 3rd row
    ]

def rotate_face_anticlockwise(face_arr):
    return [
        face_arr[2], face_arr[5], face_arr[8], # 1st row
        face_arr[1], face_arr[4], face_arr[7], # 2nd row
        face_arr[0], face_arr[3], face_arr[6]  # 3rd row
    ]

def turn_R(cube):

    cube[3] = rotate_face_clockwise(cube[3]) # Right face rotated
    
    # Temp storage of Up face column
    temp = [cube[0][2], cube[0][5], cube[0][8]]

    # Front to Up
    cube[0][2] = cube[2][2]
    cube[0][5] = cube[2][5]
    cube[0][8] = cube[2][8]

    # Down to Front
    cube[2][2] = cube[5][2]
    cube[2][5] = cube[5][5]
    cube[2][8] = cube[5][8]

    # Back to Down
    cube[5][2] = cube[4][6]
    cube[5][5] = cube[4][3]
    cube[5][8] = cube[4][0]

    # Up to Back
    cube[4][0] = temp[2]
    cube[4][3] = temp[1]
    cube[4][6] = temp[0]

    return cube

def turn_R_prime(cube):

    cube[3] = rotate_face_anticlockwise(cube[3]) # Right face rotated

    # Temp storage of Up face column
    temp = [cube[0][2], cube[0][5], cube[0][8]]

    # Back to Up
    cube[0][2] = cube[4][6]
    cube[0][5] = cube[4][3]
    cube[0][8] = cube[4][0]

    # Down to Back
    cube[4][0] = cube[5][8]
    cube[4][3] = cube[5][5]
    cube[4][6] = cube[5][2]

    # Front to Down
    cube[5][2] = cube[2][2]
    cube[5][5] = cube[2][5]
    cube[5][8] = cube[2][8]

    # Up to Front
    cube[2][2] = temp[0]
    cube[2][5] = temp[1]
    cube[2][8] = temp[2]

    return cube

def turn_U(cube):

    cube[0] = rotate_face_clockwise(cube[0]) # Up face rotated

    # Temp storage of Front face row
    temp = [cube[2][0], cube[2][1], cube[2][2]]

    # Right to Front
    cube[2][0] = cube[3][0]
    cube[2][1] = cube[3][1]
    cube[2][2] = cube[3][2]

    # Back to Right
    cube[3][0] = cube[4][0]
    cube[3][1] = cube[4][1]
    cube[3][2] = cube[4][2]

    # Left to Back
    cube[4][0] = cube[1][0]
    cube[4][1] = cube[1][1]
    cube[4][2] = cube[1][2]

    # Front to Left
    cube[1][0] = temp[0]
    cube[1][1] = temp[1]
    cube[1][2] = temp[2]

    return cube

def turn_U_prime(cube):

    cube[0] = rotate_face_anticlockwise(cube[0]) # Up face rotated

    # Temp storage of Front face row
    temp = [cube[2][0], cube[2][1], cube[2][2]]
    
    # Left to Front
    cube[2][0] = cube[1][0]
    cube[2][1] = cube[1][1]
    cube[2][2] = cube[1][2]

    # Back to Left
    cube[1][0] = cube[4][0]
    cube[1][1] = cube[4][1]
    cube[1][2] = cube[4][2]

    # Right to Back
    cube[4][0] = cube[3][0]
    cube[4][1] = cube[3][1]
    cube[4][2] = cube[3][2]

    # Front to Right
    cube[3][0] = temp[0]
    cube[3][1] = temp[1]
    cube[3][2] = temp[2]

    return cube

def turn_L(cube):

    cube[1] = rotate_face_clockwise(cube[1]) # Left face rotated

    # Temp storage of Front face column
    temp = [cube[2][0], cube[2][3], cube[2][6]]

    # Up to front
    cube[2][0] = cube[0][0]
    cube[2][3] = cube[0][3]
    cube[2][6] = cube[0][6]

    # Back to Up
    cube[0][0] = cube[4][8]
    cube[0][3] = cube[4][5]
    cube[0][6] = cube[4][2]

    # Down to Back
    cube[4][2] = cube[5][6]
    cube[4][5] = cube[5][3]
    cube[4][8] = cube[5][0]

    # Front to Down
    cube[5][0] = temp[0]
    cube[5][3] = temp[1]
    cube[5][6] = temp[2]

    return cube

def turn_L_prime(cube):

    cube[1] = rotate_face_anticlockwise(cube[1]) # Left face rotated

    # Temp storage of Front face column
    temp = [cube[2][0], cube[2][3], cube[2][6]]

    # Down to Front
    cube[2][0] = cube[5][0]
    cube[2][3] = cube[5][3]
    cube[2][6] = cube[5][6]

    # Back to Down
    cube[5][0] = cube[4][8]
    cube[5][3] = cube[4][5]
    cube[5][6] = cube[4][2]

    # Up to Back
    cube[4][2] = cube[0][6]
    cube[4][5] = cube[0][3]
    cube[4][8] = cube[0][0]

    # Front to Up
    cube[0][0] = temp[0]
    cube[0][3] = temp[1]
    cube[0][6] = temp[2]

    return cube

def turn_D(cube):

    cube[5] = rotate_face_clockwise(cube[5]) # Down face rotated

    # Temp storage of Front face row
    temp = [cube[2][6], cube[2][7], cube[2][8]]

    # Left to Front
    cube[2][6] = cube[1][6]
    cube[2][7] = cube[1][7]
    cube[2][8] = cube[1][8]

    # Back to Left
    cube[1][6] = cube[4][6]
    cube[1][7] = cube[4][7]
    cube[1][8] = cube[4][8]

    # Right to Back
    cube[4][6] = cube[3][6]
    cube[4][7] = cube[3][7]
    cube[4][8] = cube[3][8]

    # Front to Right
    cube[3][6] = temp[0]
    cube[3][7] = temp[1]
    cube[3][8] = temp[2]

    return cube

def turn_D_prime(cube):

    cube[5] = rotate_face_anticlockwise(cube[5]) # Down face rotated

    # Temp storage of Front face row
    temp = [cube[2][6], cube[2][7], cube[2][8]]

    # Right to Front
    cube[2][6] = cube[3][6]
    cube[2][7] = cube[3][7]
    cube[2][8] = cube[3][8]

    # Back to Right
    cube[3][6] = cube[4][6]
    cube[3][7] = cube[4][7]
    cube[3][8] = cube[4][8]

    # Left to Back
    cube[4][6] = cube[1][6]
    cube[4][7] = cube[1][7]
    cube[4][8] = cube[1][8]

    # Front to Left
    cube[1][6] = temp[0]
    cube[1][7] = temp[1]
    cube[1][8] = temp[2]

    return cube
 
def turn_F(cube):

    cube[2] = rotate_face_clockwise(cube[2]) # Front face rotated

    # Temp storage of Up face row
    temp = [cube[0][6], cube[0][7], cube[0][8]]

    # Left to Up
    cube[0][6] = cube[1][8]
    cube[0][7] = cube[1][5]
    cube[0][8] = cube[1][2]

    # Down to Left
    cube[1][2] = cube[5][0]
    cube[1][5] = cube[5][1]
    cube[1][8] = cube[5][2]

    # Right to Down
    cube[5][0] = cube[3][6]
    cube[5][1] = cube[3][3]
    cube[5][2] = cube[3][0]

    # Up to Right
    cube[3][0] = temp[0]
    cube[3][3] = temp[1]
    cube[3][6] = temp[2]

    return cube

def turn_F_prime(cube):

    cube[2] = rotate_face_anticlockwise(cube[2]) # Front face rotated

    # Temp storage of Up face row
    temp = [cube[0][6], cube[0][7], cube[0][8]]

    # Right to Up
    cube[0][6] = cube[3][0]
    cube[0][7] = cube[3][3]
    cube[0][8] = cube[3][6]

    # Down to Right
    cube[3][0] = cube[5][2]
    cube[3][3] = cube[5][1]
    cube[3][6] = cube[5][0]

    # Left to Down
    cube[5][0] = cube[1][2]
    cube[5][1] = cube[1][5]
    cube[5][2] = cube[1][8]

    # Up to Left
    cube[1][2] = temp[2]
    cube[1][5] = temp[1]
    cube[1][8] = temp[0]

    return cube

def turn_B(cube):

    cube[4] = rotate_face_clockwise(cube[4]) # Back face rotated

    # Temp storage of Up face row 
    temp = [cube[0][0], cube[0][1], cube[0][2]]

    # Right to Up
    cube[0][0] = cube[3][2]
    cube[0][1] = cube[3][5]
    cube[0][2] = cube[3][8]

    # Down to Right
    cube[3][2] = cube[5][8]
    cube[3][5] = cube[5][7]
    cube[3][8] = cube[5][6]

    # Left to Down
    cube[5][6] = cube[1][0]
    cube[5][7] = cube[1][3]
    cube[5][8] = cube[1][6]

    # Up to Left
    cube[1][0] = temp[2]
    cube[1][3] = temp[1]
    cube[1][6] = temp[0]

    return cube

def turn_B_prime(cube):

    cube[4] = rotate_face_anticlockwise(cube[4]) # Back face rotated

    # Temp storage of Up face row
    temp = [cube[0][0], cube[0][1], cube[0][2]]

    # Left to Up
    cube[0][0] = cube[1][6]
    cube[0][1] = cube[1][3]
    cube[0][2] = cube[1][0]

    # Down to Left
    cube[1][0] = cube[5][6]
    cube[1][3] = cube[5][7]
    cube[1][6] = cube[5][8]

    # Right to Down
    cube[5][6] = cube[3][8]
    cube[5][7] = cube[3][5]
    cube[5][8] = cube[3][2]

    # Up to Right
    cube[3][2] = temp[0]
    cube[3][5] = temp[1]
    cube[3][8] = temp[2]

    return cube

def find_edge(cube, color1, color2):

    edge_pairs = [
        # Top layer
        ((0, 7), (2, 1)), # Up-Bottom + Front-Top
        ((0, 3), (1, 1)), # Up-Left + Left-Top
        ((0, 1), (4, 1)), # Up-Top + Back-Top
        ((0, 5), (3, 1)), # Up-Right + Right-Top

        # Middle Layer
        ((2, 3), (1, 5)), # Front-Left + Left-Right
        ((1, 3), (4, 5)), # Left-Left + Back-Right
        ((4, 3), (3, 5)), # Back-Left + Right-Right
        ((3, 3), (2, 5)), # Right-Left + Front-Right

        # Bottom Layer
        ((2, 7), (5, 1)), # Front-Bottom + Down-Top
        ((1, 7), (5, 3)), # Left-Bottom + Down-Left
        ((4, 7), (5, 7)), # Back-Bottom + Down-Bottom
        ((3, 7), (5, 5))  # Right-Bottom + Down-Right
    ]

    for pair in edge_pairs:
        # Co-ords
        (f1, i1) = pair[0]
        (f2, i2) = pair[1]

        # Colors
        c1 = cube[f1][i1]
        c2 = cube[f2][i2]

        if c1 == color1 and c2 == color2:
            return (f1, i1) # Edge Found, Location of color1 Returned
        elif c1 == color2 and c2 == color1:
            return (f2, i2) # Flipped Edge Found, Location of color1 Returned
    
    return None # Not Found

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

        cur_color = {cube[f1][i1], cube[f2][i2], cube[f3][i3]}

        if cur_color == target:
            if cube[f1][i1] == color1: return (f1, i1)
            if cube[f2][i2] == color1: return (f2, i2)
            if cube[f3][i3] == color1: return (f3, i3)

    return None
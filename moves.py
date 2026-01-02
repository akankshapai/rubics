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

def turn_R(cube) :

    cube[3] = rotate_face_clockwise(cube[3]) # Right face rotated
    
    # Temp storage of Top face column
    temp = [cube[0][2], cube[0][5], cube[0][8]]

    # Front to Top
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

    # Top to Back
    cube[4][0] = temp[2]
    cube[4][3] = temp[1]
    cube[4][6] = temp[0]

    return cube

def turn_R_prime(cube) :

    cube[3] = rotate_face_anticlockwise(cube[3]) # Right face rotated

    # Temp storage of Top face column
    temp = [cube[0][2], cube[0][5], cube[0][8]]

    # Back to Top
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

    # Top to Front
    cube[2][2] = temp[0]
    cube[2][5] = temp[1]
    cube[2][8] = temp[2]

    return cube

def turn_U(cube) :

    cube[0] = rotate_face_clockwise(cube[0]) # Top face rotated

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

def turn_U_prime(cube) :

    cube[0] = rotate_face_anticlockwise(cube[0]) # Top face rotated

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

def turn_L(cube) :

    cube[1] = rotate_face_clockwise(cube[1]) # Left face rotated

    # Temp storage of Front face column
    temp = [cube[2][0], cube[2][3], cube[2][6]]

    # Top to front
    cube[2][0] = cube[0][0]
    cube[2][3] = cube[0][3]
    cube[2][6] = cube[0][6]

    # Back to Top
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

def turn_L_prime(cube) :

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

    # Top to Back
    cube[4][2] = cube[0][6]
    cube[4][5] = cube[0][3]
    cube[4][8] = cube[0][0]

    # Front to Top
    cube[0][0] = temp[0]
    cube[0][3] = temp[1]
    cube[0][6] = temp[2]

    return cube

def turn_D(cube) :

    cube[5] = rotate_face_clockwise(cube[5]) # Down face rotated

    #Temp storage of Front face row
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

def turn_D_prime(cube) :

    cube[5] = rotate_face_anticlockwise(cube[5]) # Down face rotated

    #Temp storage of Front face row
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
 
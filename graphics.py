from ursina import *
import moves

app = Ursina()
window.color = color.black
EditorCamera(move_speed = 0)  # Allows rotation with right-click drag
camera.world_position = (0, 0, -10)
camera.look_at((0,0,0))

logic_cube = moves.init_cube()

color_map = {
    'W' : color.white, 'O' : color.orange, 'G' : color.green,
    'R' : color.red, 'B' : color.blue, 'Y' : color.yellow
}

visual_faces = []

def create_face(rotation_deg):

    temp_face = []
    parent = Entity(rotation = rotation_deg) # Invisible parent serves as an anchor

    for y in [1, 0, -1]:
        for x in [-1, 0, 1]:
            element = Entity(
                parent = parent,
                model = 'quad', # Flat square
                color = color.gray,
                scale = 0.92, # Black border visibility
                position = (x, y, -1.5) # To make it pop out
            )
            temp_face.append(element)
    visual_faces.append(temp_face)

# 0 : Up face
create_face((90, 0, 0))

# 1 : Left face
create_face((0, 90, 0))

# 2 : Front face
create_face((0, 0, 0))

# 3 : Right face
create_face((0, -90, 0))

# 4 : Back face
create_face((0, 180, 0))

# 5 : Down face
create_face((-90, 0, 0))

def update_visuals():
    for face_index in range(6):
        face = logic_cube[face_index] # Get face from initialised cube
        _3d_element_list = visual_faces[face_index]

        for i in range(9):
            color_code = face[i]
            if color_code in color_map:
                _3d_element_list[i].color = color_map[color_code]

update_visuals()

def input(key):
    if key == 'q':
        app.quit()

    if key == 's':
        moves.scramble(logic_cube, 20)
        update_visuals()
    
    if key == 't':
        print("Resetting cube...")
        fresh_cube = moves.init_cube()
        for i in range(6):
            logic_cube[i] = fresh_cube[i]
        update_visuals()

    move_map = {
        'r': moves.turn_R,
        'l': moves.turn_L,
        'u': moves.turn_U,
        'd': moves.turn_D,
        'f': moves.turn_F,
        'b': moves.turn_B
    }

    prime_map = {
        'r': moves.turn_R_prime,
        'l': moves.turn_L_prime,
        'u': moves.turn_U_prime,
        'd': moves.turn_D_prime,
        'f': moves.turn_F_prime,
        'b': moves.turn_B_prime
    }

    if held_keys['shift']:
        if key in prime_map:
            prime_map[key](logic_cube)

            print(f"Turned {key.upper()}'")
            # Update 3D graphics
            update_visuals()
    
    elif key in move_map:
        move_map[key](logic_cube)

        print(f"Turned {key.upper()}")
        # Update 3D graphics
        update_visuals()

app.run()
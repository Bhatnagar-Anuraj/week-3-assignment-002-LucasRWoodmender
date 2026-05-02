import maya.cmds as cmds
import math

def create_building(width=4, height=8, depth=4, position=(0, 0, 0)):
    x, y, z = position
    building = cmds.polyCube(width=width, height=height, depth=depth)[0]
    cmds.move(x, y + height / 2.0, z, building)
    return building


def create_tree(trunk_radius=0.3, trunk_height=3, canopy_radius=2,
                position=(0, 0, 0)):
    

    trunk = cmds.polyCylinder(radius=trunk_radius, height=trunk_height)[0]
    cmds.move(x, y + trunk_height / 2.0, z, trunk)

    canopy = cmds.polySphere(radius=canopy_radius)[0]
    canopy_y = y + trunk_height + canopy_radius * 0.6
    cmds.move(x, canopy_y, z, canopy)

    tree = cmds.group(trunk, canopy, name="Tree")
    return tree


def create_fence(length=10, height=1.5, post_count=6, position=(0, 0, 0)):
    



    spacing = length / float(post_count - 1)
    parts = []

   
    for i in range(post_count):
        post_x = i * spacing
        post = cmds.polyCube(width=0.2, height=height, depth=0.2)[0]
        cmds.move(post_x, height / 2.0, 0, post)
        

   
    rail = cmds.polyCube(width=length, height=0.2, depth=0.2)[0]
    cmds.move(length / 2.0, height * 0.7, 0, rail)
   )

    fence = cmds.group(post , rail, name="Fence")
    

    return fence


def create_lamp_post(pole_height=5, light_radius=0.5, position=(0, 0, 0)):
    

    pole = cmds.polyCylinder(radius=0.1, height=pole_height)[0]
    cmds.move(x, y + pole_height / 2.0, z, pole)

    lamp = cmds.polySphere(radius=light_radius)[0]
    cmds.move(x, y + pole_height + light_radius, z, lamp)

    lamp_post = cmds.group(pole, lamp, name="LampPost")
    return lamp_post


def place_in_circle(create_tree, count=8, radius=10, center=(0, 0, 0), **kwargs):
    center_x, center_y, center_z = center
    results = []

    for i in range(count):
        angle = (2 * math.pi / count) * i
        x = center_x + math.cos(angle) * radius
        z = center_z + math.sin(angle) * radius

        trees = create_tree(position=(x, center_y, z), **kwargs)
        results.append(result)
    return results

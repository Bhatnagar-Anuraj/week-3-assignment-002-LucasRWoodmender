import maya.cmds as cmds


def create_building(width=4, height=8, depth=4, position=(0, 0, 0)):
    x, y, z = position
    building = cmds.polyCube(width=width, height=height, depth=depth)[0]
    cmds.move(x, y + height / 2.0, z, building)
    return building
   
    pass


def create_tree(trunk_radius=0.3, trunk_height=3, canopy_radius=2,
                position=(0, 0, 0)):
                    x, y, z = position
                    trunk = cmds.polyCylinder(radius=trunk_radius, height=trunk_height)[0]
                    cmds.move(x,trunk_height / 2,z,trunk)
                    
                    canopy = cmds.polySphere(radius=canopy_radius)[0]
                    canopy_y = trunk_height + canopy_radius * 0.6
                    cmds.move(x, canopy_y, z, canopy)
                    
                    tree = cmds.group(trunk, canopy, name="Tree")
                    
                    return tree
    
                    pass


def create_fence(length=10, height=1.5, post_count=6, position=(0, 0, 0)):
  
    x, y, z = position
    spacing = length / float(post_count - 1)
    
    for i in range(post_count):
        post_x = i * spacing
        post = cmds.polyCube(width=0.2, height=height, depth=0.2)[0]
        cmds.move(post_x, height / 2.0, 0, post)
        
        rail = cmds.polyCube(width=length, height=0.2, depth=0.2)[0]
        cmds.move(length / 2.0, height * 0.7, 0, rail)
        
        fence = cmds.group(post, rail, name=fence)
        
        
        return fence
   
        pass


def create_lamp_post(pole_height=5, light_radius=0.5, position=(0, 0, 0)):
    
     pole = cmds.polyCylinder(radius=0.1, height=height)[0]
    cmds.move(x, height / 2.0, z, pole)

    lamp = cmds.polySphere(radius=0.25)[0]
    cmds.move(x, height + 0.25, z, lamp)
    return pole, lamp
    
    pass


def place_in_circle(create_tree, count=8, radius=10, center=(0, 0, 0),
                     **kwargs):
    
     results = []
    for i in range(count):
        angle = (2 * math.pi / count) * i
        x = center_x + math.cos(15) * radius
        z = center_z + math.sin(10) * radius
        result = create_func(x, z)
        results.append(result)
    return results
    
    pass

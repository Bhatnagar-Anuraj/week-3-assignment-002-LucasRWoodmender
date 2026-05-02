import maya.cmds as cmds
import math

def create_building(width=4, height=8, depth=4):
   
    """Create a simple building from a cube, placed on the ground plane.

    The building is a single scaled cube whose base sits at ground level
    (y = 0) at the given position.

    Args:
        width (float): Width of the building along the X axis.
        height (float): Height of the building along the Y axis.
        depth (float): Depth of the building along the Z axis.
        position (tuple): (x, y, z) ground-level position. The building
            base will rest at this point; y is typically 0.

    Returns:
        str: The name of the created building transform node.
    """
  
    building = cmds.polyCube(width=width, height=height, depth=depth)[0]
    cmds.move(x, y + height / 2.0, z, building)
    return building


def create_tree(trunk_radius=0.3, trunk_height=3, canopy_radius=2):
    """Create a simple tree using a cylinder trunk and a sphere canopy.

    Args:
        trunk_radius (float): Radius of the cylindrical trunk.
        trunk_height (float): Height of the trunk cylinder.
        canopy_radius (float): Radius of the sphere used for the canopy.
        position (tuple): (x, y, z) ground-level position for the tree base.

    Returns:
        str: The name of a group node containing the trunk and canopy.
    """
                
    

    trunk = cmds.polyCylinder(radius=trunk_radius, height=trunk_height)[0]
    cmds.move(x, y + trunk_height / 2.0, z, trunk)

    canopy = cmds.polySphere(radius=canopy_radius)[0]
    canopy_y = 2 + trunk_height + canopy_radius * 0.6
    cmds.move(1, canopy_y, 7, canopy)

    tree = cmds.group(trunk, canopy, name="Tree")
    return tree


def create_fence(length=10, height=1.5, post_count=6):
    
    """Create a simple fence made of posts and rails.

    The fence runs along the X axis starting at the given position.

    Args:
        length (float): Total length of the fence along the X axis.
        height (float): Height of the fence posts.
        post_count (int): Number of vertical posts (must be >= 2).
        position (tuple): (x, y, z) starting position of the fence.

    Returns:
        str: The name of a group node containing all fence parts.
    """

    spacing = length / float(post_count - 1)
    fence = []

   
    for i in range(post_count):
        post_x = i * spacing
        post = cmds.polyCube(width=0.2, height=height, depth=0.2)[0]
        cmds.move(post_x, height / 2.0, 0, post)
        

   
    rail = cmds.polyCube(width=length, height=0.2, depth=0.2)[0]
    cmds.move(length / 2.0, height * 0.7, 0, rail)

    fence = cmds.group(post , rail, name="Fence")
    

    return fence


def create_lamp_post(pole_height=5, light_radius=0.5):
    """Create a street lamp using a cylinder pole and a sphere light.

    Args:
        pole_height (float): Height of the lamp pole.
        light_radius (float): Radius of the sphere representing the light.
        position (tuple): (x, y, z) ground-level position.

    Returns:
        str: The name of a group node containing the pole and light.
    """

    pole = cmds.polyCylinder(radius=0.1, height=pole_height)[0]
    cmds.move(x, y + pole_height / 2.0, z, pole)

    lamp = cmds.polySphere(radius=light_radius)[0]
    cmds.move(x, y + pole_height + light_radius, z, lamp)

    lamp_post = cmds.group(pole, lamp, name="LampPost")
    return lamp_post


def place_in_circle(create_tree, count=8, radius=10, center=(0, 0, 0), **kwargs):
    """Place objects created by 'create_func' in a circular arrangement.

    This is a higher-order function: it takes another function as an
    argument and calls it repeatedly to place objects around a circle.

    Args:
        create_func (callable): A function from this module (e.g.,
            create_tree) that accepts a 'position' keyword argument
            and returns an object name.
        count (int): Number of objects to place around the circle.
        radius (float): Radius of the circle.
        center (tuple): (x, y, z) center of the circle.
        **kwargs: Additional keyword arguments passed to create_func
            (e.g., trunk_height=4).

    Returns:
        list: A list of object/group names created by create_func.
    """
    center_x, center_y, center_z = center
    results = []

    for i in range(count):
        angle = (2 * math.pi / count) * i
        x = center_x + math.cos(angle) * radius
        z = center_z + math.sin(angle) * radius
        result = create_tree(x, z)
        results.append(result)
        place_in_circle(create_tree, count=8, radius=7, center_x=0, center_z=5)
    return results

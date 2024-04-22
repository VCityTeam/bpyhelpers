import re

def convert_obj_triangulation_to_point_cloud(triangulation_filename, verbose):
    """
    The input is a given OBJ format file holding a triangulation. Copy this
    file and modify it to become a point cloud (still with OBJ format), that is
    - remove the faces
    - modify the header accordingly
    """

    # Proceed with the copy and modification of the triangulation file to
    # obtain a vertices only PLY format file.
    point_cloud_filename = triangulation_filename.replace(
        "_triangulation", "_point_cloud"
    )
    with open(point_cloud_filename, "w") as point_cloud_file:
        for line in open(triangulation_filename):
            if re.findall("^f ", line):
                # As soon as we reach the first face we are done with
                # the vertices
                break
            point_cloud_file.write(line)
    if verbose:
        print("Point cloud file ", point_cloud_filename, " written.")

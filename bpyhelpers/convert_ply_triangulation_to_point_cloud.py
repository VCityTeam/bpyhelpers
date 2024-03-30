def convert_ply_triangulation_to_point_cloud(triangulation_filename, verbose):
    """
    The input is a given PLY format file holding a triangulation. Copy this
    file and modify it to become a point cloud (still with PLY format), that is
    - remove the faces
    - modify the header accordingly
    """
    # Extract, from header, the number of vertex lines to copy:
    number_of_vertex_lines = 0
    try:
        for line in open(triangulation_filename):
            if "element vertex " in line:
                number_of_vertex_lines = int(line.replace("element vertex ", ""))
                raise StopIteration
    except:
        if verbose:
            print(number_of_vertex_lines, "vertices must be copie to point cloud file.")

    # Proceed with the copy and modification of the triangulation file to
    # obtain a vertices only PLY format file.
    point_cloud_filename = triangulation_filename.replace(
        "_triangulation", "_point_cloud"
    )
    with open(point_cloud_filename, "w") as point_cloud_file:
        try:
            done_with_header = False
            for line in open(triangulation_filename):
                if not done_with_header:
                    # Drop the references to existing faces from the header
                    if "element face " in line:
                        continue
                    if "property list uchar uint vertex_indices" in line:
                        continue
                    if "end_header" in line:
                        done_with_header = True
                else:
                    # We know how many vertex lines we need to copy prior to exiting.
                    if not number_of_vertex_lines:
                        raise StopIteration
                    number_of_vertex_lines -= 1
                point_cloud_file.write(line)
        except:
            if verbose:
                print("Point cloud file ", point_cloud_filename, " written.")

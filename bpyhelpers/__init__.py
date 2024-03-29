from .version import version
from .bmesh_utils import (
    bmesh_assert_genus_number_boundaries,
    bmesh_duplicate,
    bmesh_euler_characteristic,
    bmesh_from_data,
    bmesh_get_boundaries,
    bmesh_get_boundary_edges,
    bmesh_get_number_of_boundaries,
    bmesh_join,
    boundary_select,
    bmesh_triangulate_quad_faces,
)
from .debug_utils import create_sphere
from .UI_utils import (
    UI_boolean_union,
    UI_cleanup_default_scene,
    UI_demote_UI_object_with_mesh_to_bmesh,
    UI_promote_bmesh_to_UI_object,
)

__version__ = version
__title__ = "bpyhelpers"
__all__ = [
    "bmesh_assert_genus_number_boundaries",
    "bmesh_duplicate",
    "bmesh_euler_characteristic",
    "bmesh_from_data",
    "bmesh_get_boundaries",
    "bmesh_get_boundary_edges",
    "bmesh_get_number_of_boundaries",
    "bmesh_join",
    "boundary_select",
    "bmesh_triangulate_quad_faces",
    "create_sphere",
    "UI_boolean_union",
    "UI_cleanup_default_scene",
    "UI_demote_UI_object_with_mesh_to_bmesh",
    "UI_promote_bmesh_to_UI_object",
]

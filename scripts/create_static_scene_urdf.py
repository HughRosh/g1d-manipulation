import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from utils import load_config

IN_URDF = Path("simulation/urdf/g1_d_with_dex1_1_hybrid.urdf")
OUT_URDF = Path("simulation/urdf/g1d_chess_static_scene.urdf")
CONFIG_PATH = Path("configs/scene.yaml")
ROOT_LINK = "AGV_link"


def add_material(root, name, rgba):
    mat = ET.SubElement(root, "material", {"name": name})
    ET.SubElement(mat, "color", {"rgba": rgba})


def add_box_link(root, name, size, color):
    link = ET.SubElement(root, "link", {"name": name})
    for tag in ("visual", "collision"):
        elem = ET.SubElement(link, tag)
        ET.SubElement(elem, "origin", {"xyz": "0 0 0", "rpy": "0 0 0"})
        geom = ET.SubElement(elem, "geometry")
        ET.SubElement(geom, "box", {"size": size})
        if tag == "visual":
            ET.SubElement(elem, "material", {"name": color})


def add_cylinder_link(root, name, radius, length, color):
    link = ET.SubElement(root, "link", {"name": name})
    for tag in ("visual", "collision"):
        elem = ET.SubElement(link, tag)
        ET.SubElement(elem, "origin", {"xyz": "0 0 0", "rpy": "0 0 0"})
        geom = ET.SubElement(elem, "geometry")
        ET.SubElement(geom, "cylinder", {"radius": str(radius), "length": str(length)})
        if tag == "visual":
            ET.SubElement(elem, "material", {"name": color})


def add_fixed_joint(root, name, parent, child, xyz):
    joint = ET.SubElement(root, "joint", {"name": name, "type": "fixed"})
    ET.SubElement(joint, "parent", {"link": parent})
    ET.SubElement(joint, "child", {"link": child})
    ET.SubElement(joint, "origin", {"xyz": xyz, "rpy": "0 0 0"})


def main():
    cfg = load_config(CONFIG_PATH)["scene"]
    table = cfg["table"]
    board = cfg["board"]
    cup = cfg["cup"]

    tree = ET.parse(IN_URDF)
    root = tree.getroot()
    root.set("name", "g1d_chess_static_scene")

    add_material(root, "table_brown", "0.45 0.25 0.12 1")
    add_material(root, "board_light", "0.9 0.85 0.7 1")
    add_material(root, "board_dark", "0.15 0.15 0.15 1")
    add_material(root, "cup_red", "0.8 0.1 0.1 1")

    add_box_link(
        root,
        "table_link",
        f'{table["size_x_m"]} {table["size_y_m"]} {table["thickness_m"]}',
        "table_brown",
    )
    table_z = table["height_m"] - table["thickness_m"] / 2.0
    add_fixed_joint(root, "table_fixed_joint", ROOT_LINK, "table_link", f'{table["x_m"]} {table["y_m"]} {table_z}')

    board_z = table["height_m"] + board["thickness_m"] / 2.0
    square = board["size_m"] / 8.0

    for rank in range(8):
        for file in range(8):
            name = f"board_square_{file}_{rank}"
            color = "board_light" if (file + rank) % 2 == 0 else "board_dark"
            x = board["x_m"] + (file - 3.5) * square
            y = board["y_m"] + (rank - 3.5) * square
            add_box_link(root, name, f"{square} {square} {board['thickness_m']}", color)
            add_fixed_joint(root, f"{name}_joint", ROOT_LINK, name, f"{x} {y} {board_z}")

    cup_z = table["height_m"] + cup["height_m"] / 2.0
    add_cylinder_link(root, "cup_link", cup["radius_m"], cup["height_m"], "cup_red")
    add_fixed_joint(root, "cup_fixed_joint", ROOT_LINK, "cup_link", f'{cup["x_m"]} {cup["y_m"]} {cup_z}')

    ET.indent(tree, space="  ")
    tree.write(OUT_URDF, encoding="utf-8", xml_declaration=True)

    print(f"Wrote {OUT_URDF}")
    print(f"Table x/y: {table['x_m']}, {table['y_m']}")
    print(f"Board x/y: {board['x_m']}, {board['y_m']}")
    print(f"Cup x/y: {cup['x_m']}, {cup['y_m']}")


if __name__ == "__main__":
    main()

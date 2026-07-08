import xml.etree.ElementTree as ET
from pathlib import Path

URDF_PATH = Path("simulation/urdf/g1_d.urdf")

def main():
    tree = ET.parse(URDF_PATH)
    root = tree.getroot()

    print(f"Robot: {root.attrib.get('name')}")
    print("\nJoints:")

    for joint in root.findall("joint"):
        name = joint.attrib.get("name")
        joint_type = joint.attrib.get("type")

        parent = joint.find("parent")
        child = joint.find("child")
        limit = joint.find("limit")

        parent_link = parent.attrib.get("link") if parent is not None else "none"
        child_link = child.attrib.get("link") if child is not None else "none"

        print(f"\n{name}")
        print(f"  type: {joint_type}")
        print(f"  parent: {parent_link}")
        print(f"  child: {child_link}")

        if limit is not None:
            print(f"  lower: {limit.attrib.get('lower')}")
            print(f"  upper: {limit.attrib.get('upper')}")
            print(f"  effort: {limit.attrib.get('effort')}")
            print(f"  velocity: {limit.attrib.get('velocity')}")

if __name__ == "__main__":
    main()

import xml.etree.ElementTree as ET
from pathlib import Path


class RobotModel:
    def __init__(self, urdf_path):
        self.urdf_path = Path(urdf_path)
        self.tree = ET.parse(self.urdf_path)
        self.root = self.tree.getroot()

    def robot_name(self):
        return self.root.attrib.get("name", "unknown")

    def joints(self):
        result = []
        for joint in self.root.findall("joint"):
            name = joint.attrib.get("name")
            joint_type = joint.attrib.get("type")
            limit = joint.find("limit")

            joint_info = {
                "name": name,
                "type": joint_type,
                "lower": None,
                "upper": None,
            }

            if limit is not None:
                joint_info["lower"] = limit.attrib.get("lower")
                joint_info["upper"] = limit.attrib.get("upper")

            result.append(joint_info)

        return result

    def right_arm_joints(self):
        return [
            j for j in self.joints()
            if j["name"] and j["name"].startswith("right_")
        ]

    def dex1_joints(self):
        return [
            j for j in self.joints()
            if "dex1" in j["name"].lower() or "gripper" in j["name"].lower()
        ]

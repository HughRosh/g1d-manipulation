from dataclasses import dataclass
from typing import Tuple


@dataclass
class ImageToRobotMapper:
    image_x_min_px: float
    image_x_max_px: float
    image_y_min_px: float
    image_y_max_px: float

    robot_x_min_m: float
    robot_x_max_m: float
    robot_y_min_m: float
    robot_y_max_m: float

    def map_px_to_robot(self, px: Tuple[float, float]) -> Tuple[float, float]:
        u, v = px

        u_norm = (u - self.image_x_min_px) / (self.image_x_max_px - self.image_x_min_px)
        v_norm = (v - self.image_y_min_px) / (self.image_y_max_px - self.image_y_min_px)

        u_norm = max(0.0, min(1.0, u_norm))
        v_norm = max(0.0, min(1.0, v_norm))

        robot_x = self.robot_x_min_m + v_norm * (self.robot_x_max_m - self.robot_x_min_m)
        robot_y = self.robot_y_min_m + u_norm * (self.robot_y_max_m - self.robot_y_min_m)

        return robot_x, robot_y

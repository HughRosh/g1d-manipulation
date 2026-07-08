def check_workspace(motion_steps, robot_config):
    workspace = robot_config["workspace"]

    for step in motion_steps:
        if step["action"] != "move":
            continue

        x, y, z = step["target"]

        if not (workspace["min_x_m"] <= x <= workspace["max_x_m"]):
            return False, f"x out of workspace: {x}"

        if not (workspace["min_y_m"] <= y <= workspace["max_y_m"]):
            return False, f"y out of workspace: {y}"

        if not (workspace["min_z_m"] <= z <= workspace["max_z_m"]):
            return False, f"z out of workspace: {z}"

    return True, "workspace check passed"


def check_robot_enabled(robot_config):
    robot = robot_config["robot"]

    if robot.get("real_robot_enabled", False):
        return True, "real robot execution enabled"

    return True, "dry-run mode; real robot disabled"


def run_safety_checks(motion_steps, robot_config):
    checks = [
        check_workspace(motion_steps, robot_config),
        check_robot_enabled(robot_config),
    ]

    for passed, message in checks:
        if not passed:
            return False, message

    return True, "all safety checks passed"

def require_top_down_approach(config):
    approach = config.get("approach", {})

    if approach.get("direction") != "top_down":
        return False, "approach direction must be top_down"

    if approach.get("allow_side_grasps", True):
        return False, "side grasps are not allowed"

    return True, "top-down approach constraint passed"

from g1d_chess.robot.safety import safe_pick_place_waypoints

# Fake chess move path: source square to target square
path = safe_pick_place_waypoints(
    from_xyz=(0.35, 0.10, -0.10),
    to_xyz=(0.45, 0.20, -0.10),
)

for i, p in enumerate(path):
    print(i, p)

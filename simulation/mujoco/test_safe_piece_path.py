from g1d_chess.robot.safety import safe_pick_place_waypoints

path = safe_pick_place_waypoints(
    from_xyz=(0.35, -0.10, -0.20),
    to_xyz=(0.55, 0.10, -0.20),
)

print("Safe waypoints:")
for i, p in enumerate(path):
    print(i, p)

assert all(p[2] >= 0.035 for p in path)
print("PASS: no waypoint goes below table-safe height")

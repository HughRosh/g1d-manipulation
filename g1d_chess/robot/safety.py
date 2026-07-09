TABLE_Z = 0.00
SAFE_Z = 0.18
PICK_Z = 0.035
PLACE_Z = 0.035


def clamp_pose_xyz(x, y, z, min_z=PICK_Z):
    if z < min_z:
        print(f"[SAFETY] Clamped z from {z:.3f} to {min_z:.3f}")
        z = min_z
    return x, y, z


def safe_pick_place_waypoints(from_xyz, to_xyz):
    fx, fy, fz = clamp_pose_xyz(*from_xyz)
    tx, ty, tz = clamp_pose_xyz(*to_xyz)

    return [
        (fx, fy, SAFE_Z),  # above source
        (fx, fy, fz),      # down to piece
        (fx, fy, SAFE_Z),  # lift
        (tx, ty, SAFE_Z),  # above target
        (tx, ty, tz),      # place
        (tx, ty, SAFE_Z),  # lift away
    ]

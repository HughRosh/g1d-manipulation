#!/usr/bin/env python3

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from pathlib import Path
from src.utils import load_config

OUT = Path("simulation/mujoco/chess_piece_scene.xml")

PIECE_RADIUS = 0.018
PIECE_HEIGHT = 0.055


def square_xy(square, scene):
    board = scene["board"]
    files = "abcdefgh"
    ranks = "12345678"

    f = files.index(square[0])
    r = ranks.index(square[1])

    s = board["size_m"] / 8.0

    x = board["x_m"] + (f - 3.5) * s
    y = board["y_m"] + (r - 3.5) * s

    return x, y


def main():
    scene = load_config("configs/scene.yaml")["scene"]

    table = scene["table"]
    board = scene["board"]

    table_z = table["height_m"]
    board_z = table_z + board["thickness_m"] / 2.0
    piece_z = table_z + board["thickness_m"] + PIECE_HEIGHT / 2.0

    pieces = []

    for file in "abcdefgh":
        pieces.append((file + "2", "white"))
        pieces.append((file + "7", "black"))

    back_rank = ["a1","b1","c1","d1","e1","f1","g1","h1",
                 "a8","b8","c8","d8","e8","f8","g8","h8"]

    for sq in back_rank:
        color = "white" if sq[1] == "1" else "black"
        pieces.append((sq, color))

    xml = f'''<mujoco model="g1d_chess_piece_scene">
  <compiler angle="radian"/>

  <option timestep="0.002"/>

  <asset>
    <material name="table_mat" rgba="0.32 0.16 0.07 1"/>
    <material name="light_square" rgba="0.85 0.68 0.42 1"/>
    <material name="dark_square" rgba="0.32 0.16 0.07 1"/>
    <material name="white_piece" rgba="0.95 0.88 0.72 1"/>
    <material name="black_piece" rgba="0.12 0.05 0.025 1"/>
    <material name="moving_piece" rgba="0.9 0.1 0.1 1"/>
  </asset>

  <worldbody>
    <light pos="0 0 3"/>

    <geom name="table"
          type="box"
          pos="{table['x_m']} {table['y_m']} {table_z - table['thickness_m']/2.0}"
          size="{table['size_x_m']/2.0} {table['size_y_m']/2.0} {table['thickness_m']/2.0}"
          material="table_mat"/>

    <body name="board" pos="{board['x_m']} {board['y_m']} {board_z}">
'''

    s = board["size_m"] / 8.0
    for r in range(8):
        for f in range(8):
            x = (f - 3.5) * s
            y = (r - 3.5) * s
            mat = "light_square" if (r + f) % 2 == 0 else "dark_square"
            xml += f'''      <geom type="box" pos="{x} {y} 0.004" size="{s/2} {s/2} 0.004" material="{mat}"/>\n'''

    xml += "    </body>\n\n"

    for sq, color in pieces:
        if sq == "e2":
            continue

        x, y = square_xy(sq, scene)
        mat = "white_piece" if color == "white" else "black_piece"

        xml += f'''    <body name="piece_{sq}" pos="{x} {y} {piece_z}">
      <geom type="cylinder" size="{PIECE_RADIUS} {PIECE_HEIGHT/2.0}" material="{mat}"/>
      <geom type="sphere" pos="0 0 {PIECE_HEIGHT/2.0}" size="{PIECE_RADIUS*0.8}" material="{mat}"/>
    </body>\n\n'''

    ex, ey = square_xy("e2", scene)
    xml += f'''    <body name="moving_piece" pos="{ex} {ey} {piece_z}">
      <joint name="moving_piece_free" type="free"/>
      <geom type="cylinder" size="{PIECE_RADIUS} {PIECE_HEIGHT/2.0}" material="moving_piece"/>
      <geom type="sphere" pos="0 0 {PIECE_HEIGHT/2.0}" size="{PIECE_RADIUS*0.8}" material="moving_piece"/>
    </body>\n'''

    xml += '''
  </worldbody>
</mujoco>
'''

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(xml)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()

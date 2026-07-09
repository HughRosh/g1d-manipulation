#!/usr/bin/env python3

from robot.commands.low_command import LowCommand
from robot.commands.position_command import JointPositionCommand
from robot.model.joint_limits import clamp_joint


def command_from_current_position(current_q) -> LowCommand:
    cmd = LowCommand()
    cmd.q_target[:] = current_q
    return cmd


def apply_position_command(cmd: LowCommand, position_command: JointPositionCommand) -> LowCommand:
    new_cmd = cmd.copy()
    index = position_command.joint_index

    new_cmd.q_target[index] = clamp_joint(index, position_command.q_target)
    new_cmd.dq_target[index] = position_command.dq_target
    new_cmd.tau_ff[index] = position_command.tau_ff

    return new_cmd

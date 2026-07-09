# Architecture

G1-D Chess is designed so the chess logic does not care whether it is running in simulation or on the real robot.

## Main Pipeline

```text
Camera / Board State
        ↓
Chess Engine
        ↓
Motion Planner
        ↓
Controller API
        ↓
Mock, Simulation, or Real G1-D

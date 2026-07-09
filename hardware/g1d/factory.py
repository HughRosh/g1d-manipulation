#!/usr/bin/env python3

def make_g1d_controller(backend="mock", interface="eth0"):
    if backend == "mock":
        from hardware.g1d.mock_controller import MockG1DController
        return MockG1DController()

    if backend == "real":
        from hardware.g1d.controller import G1DController
        return G1DController(interface=interface)

    raise ValueError(f"Unknown G1-D backend: {backend}")

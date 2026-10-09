"""Independent finite checker for uniform FR fibre-routing theorem."""
from applications.berge_fulkerson.plateau.energy_barriers.independent_fibre_routing import (
    local_check, verify_five_round_schedule, k4_check
)

def test_exact_local_fibres_and_port_change_lifts():
    local_check()

def test_five_round_universal_routing_and_four_round_failure():
    verify_five_round_schedule()

def test_k4_enumeration_and_full_component_connectivity():
    k4_check()
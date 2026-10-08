from berge_fulkerson.plateau import test_plateau as cases

def test_october_certificate(): cases.test_small_certificate_and_duals()
def test_october_family(): cases.test_vertex_expansion_family()
def test_october_bounded_descent(): cases.test_bounded_coordinate_descent_on_generated_states()
def test_october_Q6_threshold(): cases.test_sharp_Q6_two_coordinates()
def test_october_cover(): cases.test_double_cover_and_aggregate()
def test_october_three_cut(): cases.test_three_cut_toy_algebra()
def test_october_general_Q6(): cases.test_general_q6_pair_criterion()
def test_october_flow_optimizer(): cases.test_two_coordinate_flow_equals_exhaustive()
def test_october_transversal_boundary(): cases.test_transversal_boundary()

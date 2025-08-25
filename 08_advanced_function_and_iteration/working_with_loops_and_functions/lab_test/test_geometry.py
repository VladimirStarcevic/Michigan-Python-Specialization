from geometry_functions import distance


def test_distance_for_same_point():
    assert distance(1, 1, 1, 1) == 0


def test_distance_3_4_5_triangle():
    assert distance(0, 0, 3, 4) == 5.0

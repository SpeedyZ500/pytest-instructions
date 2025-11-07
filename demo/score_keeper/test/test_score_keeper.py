import pytest
from score_keeper.score_keeper import ScoreKeeper

def test_score_keeper_add_points():
    #Given
    score = ScoreKeeper()
    points_to_add = 5
    expected = 5
    #Then
    result = score.add_points(points_to_add)
    assert result == expected
    assert score.total_score == expected

my_score = ScoreKeeper()

def test_show_side_effects_part_1():
    #Given
    points_to_add = 7
    expected = 7
    #Then
    result = my_score.add_points(points_to_add)
    assert result == expected
    assert my_score.total_score == expected

def test_show_side_effects_part_2():
    #Given
    points_to_add = 8
    expected = 8
    #Then
    result = my_score.add_points(points_to_add)
    assert result == expected
    assert my_score.total_score == expected

@pytest.fixture
def score_fixture():
    return ScoreKeeper()

def test_show_fixture_effects_1(score_fixture):
    #Given
    points_to_add = 7
    expected = 7
    #then
    result = score_fixture.add_points(points_to_add)
    assert result == expected
    assert score_fixture.total_score == expected

def test_show_fixture_effects_2(score_fixture):
    #Given
    points_to_add = 8
    expected = 8
    #then
    result = score_fixture.add_points(points_to_add)
    assert result == expected
    assert score_fixture.total_score == expected

class TestScoreKeeper:
    score_obj = ScoreKeeper()
    def test_show_class_effects_1(self):
        #Given
        points_to_add = 7
        expected = 7
        #then
        result = self.score_obj.add_points(points_to_add)
        assert result == expected
        assert self.score_obj.total_score == expected

    def test_show_class_effects_2(self):
        #Given
        points_to_add = 8
        expected = 8
        #then
        result = self.score_obj.add_points(points_to_add)
        assert result == expected
        assert self.score_obj.total_score == expected

from task import *
import pytest
import numpy as np


def test_load_data():
    loaded_df = load_data(Path('.\data\interview_data (1).csv'))
    first_row = pd.DataFrame({'x': 1.5, 'y': 0.0, 'noise': 0.03167706326905716},
                             index=[pd.to_datetime('2018-01-01 00:00:00.000')])
    assert np.allclose(first_row.iloc[0].values, loaded_df.iloc[0].values, np.finfo(float).eps)
    assert all(first_row.iloc[0].index == loaded_df.iloc[0].index)
    assert first_row.index[0] == loaded_df.index[0]


def test_get_mean_draw_velocity():
    test_df = pd.DataFrame({'x': [0, 1, 1, 5], 'y': [0, 0, 1, 4]},
                           index=[pd.to_datetime('2018-01-01 1:00:00.000'),
                                  pd.to_datetime('2018-01-01 2:00:00.000'),
                                  pd.to_datetime('2018-01-01 3:00:00.000'),
                                  pd.to_datetime('2018-01-01 4:00:00.000'),
                                  ])
    velocity = get_mean_draw_velocity(test_df)
    assert np.isclose(velocity, 0.0006481481481481481)


def test_distance_between_points():
    dist = distance_between_points((0, 0), (3, 4))
    assert dist == 5


def test_get_distance_to_point():
    test_df = pd.DataFrame({'x': [0, 1, 1, 5], 'y': [0, 0, 1, 4]})
    result = get_distance_to_point(test_df, (1,1))
    assert result.iloc[-1] == 5
    assert len(result) == 4

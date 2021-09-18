from pathlib import Path
import numpy as np
import pandas as pd


def load_data(datapath: Path) -> pd.DataFrame:
    org_df = pd.read_csv(datapath, delimiter='\t', index_col=0)
    org_df.index = pd.to_datetime(org_df.index)
    return org_df


def get_mean_draw_velocity(sampled_df: pd.DataFrame) -> float:
    distance_pow = (sampled_df - sampled_df.shift(1)).pow(2)
    distance_sum = distance_pow['x'] + distance_pow['y']
    distance = np.sqrt(distance_sum).sum()
    velocity = distance / (sampled_df.index.max() - sampled_df.index.min()).seconds
    return velocity


def calculate_center_of_mass(sampled_df: pd.DataFrame) -> tuple:
    return sampled_df['x'].mean(), sampled_df['y'].mean()


def distance_between_points(p1: tuple, p2: tuple) -> float:
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def get_distance_to_point(sampled_df: pd.DataFrame, point: tuple) -> pd.Series:
    return sampled_df.apply(lambda x: distance_between_points((x['x'], x['y']), point),
                            axis=1)


def metric_system_change():
    length_unit = input('Which unit of length do you want to use:  ')
    return length_unit


def time_unit_system_change():
    unit = input('Which unit do you want it converted to: [default second][ns/ms/s/minutes/hours/days]')
    if unit == "ns":
        ans = 10 * 6
    elif unit == "ms":
        ans = 10 * 3
    elif unit == "minutes":
        ans = 1 / 60
    elif unit == "hours":
        ans = 1 / 60 / 60
    elif unit == "days":
        ans = 1 / 60 / 60 / 24
    else:
        ans = 1
        unit = 's'
    return ans, unit


def length_unit_system_change():
    unit1 = input('Which unit do you want it converted from:  [cm/mm/m/km/ft/inch]')
    unit2 = input('Which unit do you want it converted to: [cm/mm/m/km/ft/inch]')

    if unit1 == "cm" and unit2 == "m":
        ans = 1 / 100

    elif unit1 == "mm" and unit2 == "cm":
        ans = 1 / 10

    elif unit1 == "m" and unit2 == "cm":
        ans = 1 * 100

    elif unit1 == "cm" and unit2 == "mm":
        ans = 1 * 10

    elif unit1 == "mm" and unit2 == "m":
        ans = 1 / 1000

    elif unit1 == "m" and unit2 == "mm":
        ans = 1 * 1000

    elif unit1 == "km" and unit2 == "m":
        ans = 1 * 1000

    elif unit1 == "m" and unit2 == "km":
        ans = 1 / 1000

    elif unit1 == "mm" and unit2 == "km":
        ans = 1 / 1000000

    elif unit1 == "ft" and unit2 == "cm":
        ans = 1 * 30.48

    elif unit1 == "ft" and unit2 == "mm":
        ans = 1 * 304.8

    elif unit1 == "ft" and unit2 == "inch":
        ans = 1 * 12

    elif unit1 == "inch" and unit2 == "cm":
        ans = 1 * 2.54
    elif unit1 == "inch" and unit2 == "mm":
        ans = 1 * 25.4
    else:
        ans, unit2 = 1, unit2

    return ans, unit2


def get_reference_frame():
    px = input('Get axis x reference point')
    py = input('Get axis y reference point')
    px = float(px)
    py = float(py)

    return px, py

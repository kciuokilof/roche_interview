import matplotlib.pyplot as plt

from task_lib import *

if __name__ == '__main__':
    time_metric_factor, time_metric_unit_name = time_unit_system_change()
    length_metric_factor, length_metric_unit_name = length_unit_system_change()
    reference_x, reference_y = get_reference_frame()
    datapath = Path(r'.\data\interview_data (1).csv')
    org_df = load_data(datapath)
    org_df['x'] = org_df['x'] * length_metric_factor
    org_df['y'] = org_df['y'] * length_metric_factor
    org_df['x'] = org_df['x'] - reference_x
    org_df['y'] = org_df['y'] - reference_y
    print(org_df.head())
    sampling_freq = 20
    sampled_df = org_df.asfreq(pd.DateOffset(seconds=1 / 100))
    sampled_df = sampled_df.interpolate().asfreq(pd.DateOffset(seconds=1 / sampling_freq))

    mean_velocity = get_mean_draw_velocity(sampled_df)
    print(f'mean_velocity: {mean_velocity/time_metric_factor} {length_metric_unit_name}/{time_metric_unit_name}'),

    center_of_mass = calculate_center_of_mass(sampled_df)

    ax = org_df.plot.scatter('x', 'y')
    ax.plot(center_of_mass[0], center_of_mass[1], "or")
    ax.set_title('predifned points with mass center')

    ax = sampled_df.plot.scatter('x', 'y')
    ax.plot(center_of_mass[0], center_of_mass[1], "or")
    ax.set_title('Probed trace with mass center')

    plt.show()
    org_df['distance_to_mass_center'] = get_distance_to_point(org_df, center_of_mass)
    org_df.to_csv(r'.\data\distance_to_mass_center.csv')

Code which generated signal for roche interview.

Code contains:
task.py - main script, that should be run in order to get analisis.
task_lib.py - methods used in script
test_task.py - unittests.

Code requirements: matplotlib, pandas and Pathlib installed. Tested on Python 3.8

After running task.py, user must provide:
used time unit 
Then, length unit of original data.
Then, length unit which want to use in analysis.
Then, 2dim. frame of reference origin.

Program will: 
calculate and print mean velocity of drawing in given units.
calculate distance between the predefined points and the center of mass and save it .data\distance_to_mass_center.csv
plot predefined points, sampled drawing trace and the mass center.

To exit program, plots should be closed.








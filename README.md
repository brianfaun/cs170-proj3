# CS 170 Project Fall 2021

**Project Structure**

Files:

- `parse.py`: functions to read/write inputs and outputs
- `solver.py`: where you should be writing your code to solve inputs
- `Task.py`: contains a class that is useful for processing inputs

Instructions:

In order to process inputs from a specific file, assign the field input_path to a file with format "name.in". This field can be found in the main method at the bottom of solver.py. Also, change the max_deadline field in the solve method to the final deadline for all of the tasks to complete by (1440 for CS170 project). Run the main method and the expected output will be a series of print statements that state the igloo id and what time the task is scheduled as well as a list of igloo id's in order of when they should be cleaned.

Example Output:

samples/five5.in samples/test.out <br>
schedule job 4 at time 10 <br>
schedule job 1 at time 35 <br>
schedule job 3 at time 65 <br>
[4, 1, 3]

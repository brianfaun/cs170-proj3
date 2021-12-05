from parse import read_input_file, write_output_file
import os


def solve(igloos):
    """
    Args:
        igloos: list[Task], list of igloos to polish
    Returns:
        output: list of igloos in order of polishing  
    """
    # Task : (task_id, deadline, duration, perfect_benefit)
    #
    # Naive Solution - Start with the task with the earliest deadline, then start next available task
    #
    # Value Solution - Aim to include the highest value tasks
    #
    # Best Solution - Aim to include the highest value tasks, and allowing for
    # substitution of one task for multiple tasks that bring more profit

    time, profit = 0, 0
    rows, columns = 80, 4
    iglooList = []
    for igloo in igloos:
        iglooList.append([igloo.get_task_id(), igloo.get_deadline(), igloo.get_duration(), igloo.get_max_benefit()])
    deadlineList = sorted(iglooList, key=lambda x: x[1])
    durationList = sorted(iglooList, key=lambda x: x[2])
    valueList = sorted(iglooList, key=lambda x: x[3])


    print(iglooList)
    print(deadlineList)
    print(durationList)
    print(valueList)
    return [1]


    """maiden
    time, profit = 0, 0
    highestRatios, iglooList = [], []
    for igloo in tasks:
        ratio = igloo.get_max_benefit() / igloo.get_duration()
        highestRatios.append("{:.2f}".format(ratio))
        iglooList.append(igloo.task_id)
    highestRatios.sort(reverse=True)
    print(highestRatios)
    return iglooList"""


if __name__ == '__main__':
    """for size in os.listdir('inputs/'):
        if size not in ['small', 'medium', 'large']:
            continue
        for input_file in os.listdir('inputs/{}'.format(size)):
            if size not in input_file:
                continue
            input_path = 'inputs/{}/{}'.format(size, input_file)
            output_path = 'outputs/{}/{}.out'.format(size, input_file[:-3])
            print(input_path, output_path)
            tasks = read_input_file(input_path)
            output = solve(tasks)
            write_output_file(output_path, output)"""
    input_path = 'samples/100.in'
    output_path = 'samples/test.out'
    print(input_path, output_path)
    tasks = read_input_file(input_path)
    output = solve(tasks)
    write_output_file(output_path, output)
    print(output)

# Here's an example of how to run your solver.
# if __name__ == '__main__':
#     for size in os.listdir('inputs/'):
#         if size not in ['small', 'medium', 'large']:
#             continue
#         for input_file in os.listdir('inputs/{}/'.format(size)):
#             if size not in input_file:
#                 continue
#             input_path = 'inputs/{}/{}'.format(size, input_file)
#             output_path = 'outputs/{}/{}.out'.format(size, input_file[:-3])
#             print(input_path, output_path)
#             tasks = read_input_file(input_path)
#             output = solve(tasks)
#             write_output_file(output_path, output)

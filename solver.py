from parse import read_input_file, write_output_file
import os

class Taskdata:

    def __init__(self, id, dl, dur, profit, time):
        self.id = id
        self.time = time
        self.dur = dur
        self.dl = dl
        self.profit = profit
        self.calc_profit = 0

    def set_calc_profit(self, calc_profit):
        self.calc_profit = calc_profit

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
    iglooList = [[0, 0, 0, 0]]
    # for igloo in igloos:
    #     iglooList.append([igloo.get_task_id(), igloo.get_deadline(), igloo.get_duration(), igloo.get_max_benefit()])
    # deadlineList = sorted(iglooList, key=lambda x: x[1], reverse=True)
    # durationList = sorted(iglooList, key=lambda x: x[2], reverse=True)
    # valueList = sorted(iglooList, key=lambda x: x[3], reverse=True)

    iglooList = [[0, 0, 0, 0]] #set 0th entry to all 0's so 1st entry corresponds with igloo id #1, 2nd with #2, etc
    for igloo in igloos:
        iglooList.append([igloo.get_task_id(), igloo.get_deadline(), igloo.get_duration(), igloo.get_max_benefit()])
    # iglooList format [id, deadline, duration, profit] where id = list index

    #calculate avg profit/duration for all igloos
    ratioList = [0]
    # print(tasks)
    for task in tasks:
        ratioList.append(task.get_max_benefit() / task.get_duration())
        # ratioList.append("{:.2f}".format(ratio))
    avgProfit = sum(ratioList) / (len(ratioList) - 1) # -1 to account for empty 0th entry
    # print(avgProfit)

    #sort ids/indices by ascending deadlines so [65, 100, 80, 30, 40] -> [4, 5, 1, 3, 2]
    #make a dict of igloo id and deadline
    id_dl_dict = {}
    keys = range(0, len(igloos) + 1)
    # print(keys)
    id_dl_dict[0] = -1 #by default give 0th item the earliest deadline
    for i in range(1, len(igloos) + 1):
        id_dl_dict[i] = tasks[i - 1].get_deadline()

    id_dl_dict = {k: v for k, v in sorted(id_dl_dict.items(), key=lambda item: item[1])} #sort by values/deadlines
    dl_asc_keys = list(id_dl_dict.keys())
    # print(dl_asc_keys)

    soln = []
    # def f(i, t):
    #     iglooDur = iglooList[i][2]
    #     iglooDl = iglooList[i][1]
    #     if (t + iglooDur <= iglooDl):
    #         print(i, ratioList[i])
    #         if ratioList[i] >= 0.5*avgProfit:
    #             nonlocal profit
    #             profit += iglooList[i][3]
    #             max_prof = 0
    #             max_id = 0
    #             for x in range(i+1, len(iglooList) - 1):
    #                 print("x is", x)
    #                 if f(x, t + iglooDur) > max_prof:
    #                     max_prof = f(x, t + iglooDur)
    #                     max_id = x
    #             soln.append(max_id)
    #             profit = max_prof
    #         else:
    #             return f(i+1, t)
    #     return profit

    #f(1, 0)
    #print(soln)
    max_deadline = 1440
    num_tasks = len(tasks)
    B = [[0 for t in range(max_deadline+1)] for i in range(0, num_tasks)]

    # iglooList format [id, deadline, duration, profit] where id = list index
    for i in range(1, num_tasks):
        for t in range(0, max_deadline+1):
            igloo_id = dl_asc_keys[i]
            igloo_dl = iglooList[igloo_id][1]
            igloo_dur = iglooList[igloo_id][2]
            igloo_prof = iglooList[igloo_id][2]
            latest_dl = min(t, iglooList[igloo_id][1]) - iglooList[igloo_id][2]
            if (latest_dl < 0):
                B[i][t] = B[i-1][t]
            else:
                B[i][t] = max(B[i-1][t], igloo_prof + B[i-1][latest_dl])

    def print_opt(i, t):
        if i == 0:
            return
        if B[i][t] == B[i-1][t]:
            print_opt(i-1, t)
        else:
            igloo_id = dl_asc_keys[i]
            latest_dl = min(t, iglooList[igloo_id][1]) - iglooList[igloo_id][2]
            print_opt(i-1, latest_dl)
            print("schedule job", igloo_id, "at time", latest_dl)
            soln.append(igloo_id)

    print_opt(num_tasks-1, max_deadline)

    return soln
    # max_profit(1, 1440, dl_asc_keys, avgProfit)

# def max_profit(i, t, dl_asc_keys, avg_prof_min): #igloo index, time t, lst where keys are ids associated w/deadlines in asc order
#     #initalize an lst of taskdata items
#     tdata_lst = []
#     #placeholder task for task0
#     tdata_lst.append(Taskdata(0, 0, 0, 0, 0))
#     for task in tasks:
#         for min in range(1440):
#             tdata = Taskdata(task.get_task_id(), task.get_deadline(),
#                              task.get_duration(), task.get_max_benefit(),
#                              min) #initalize a taskdata object for each task associated with each minute
#             tdata_lst.append(tdata)
#         #tdata_lst[0].set_profit(10)
#     soln = []
#     def max_profit_helper(ind, time):
#         id = dl_asc_keys[ind] #id of the igloo we want to process
#         task_calc_profit = get_task_calc_profit(id, time)
#         task_dur = get_task_dur(id, time)
#         task_dl = get_task_dl(id, time)
#         task_profit = get_task_profit(id, time)
#         # print("dur is", task_dur)
#         if task_calc_profit != 0: #memoized values are returned
#             return task_calc_profit
#         if (time + task_dur < task_dl):
#             if (task_profit / task_dur >= 0.5 * avg_prof_min): #greedy takes any task whose prof/min is greater than avg scaled
#                 soln.append(id)
#                 # print(soln)
#                 prev_profit = get_task_calc_profit(i - 1, time)
#                 set_task_calc_profit(id, time + task_dur, prev_profit + task_profit)
#                 if (ind + 1 < len(dl_asc_keys)):
#                     max_profit_helper(ind + 1, time + task_dur)
#                 # if (ind + 2 < len(dl_asc_keys)):
#                 #     max_profit_helper(ind + 2, time + task_dur)
#                 return prev_profit + task_profit
#         else:
#             if (ind + 1 < len(dl_asc_keys)):
#                 return max_profit_helper(ind + 1, time)
#
#     def get_task_calc_profit(id, time): #return task with corresponding id and time and -1 if dne
#         for t in tdata_lst:
#             # print(t.id, id, t.time, time)
#             if (t.id == id and t.time == time):
#                 return t.calc_profit
#         return -1
#
#     def set_task_calc_profit(id, time, calc_profit): #return task with corresponding id and time and -1 if dne
#         for t in tdata_lst:
#             # print(t.id, id, t.time, time)
#             if (t.id == id and t.time == time):
#                 t.calc_profit = calc_profit
#         return -1
#
#     def get_task_dur(id, time): #return task dur with corresponding id and time and -1 if dne
#         for t in tdata_lst:
#             if t.id == id and t.time == time:
#                 return t.dur
#         return -1
#
#     def get_task_dl(id, time): #return task dur with corresponding id and time and -1 if dne
#         for t in tdata_lst:
#             if t.id == id and t.time == time:
#                 return t.dl
#         return -1
#
#     def get_task_profit(id, time): #return task dur with corresponding id and time and -1 if dne
#         for t in tdata_lst:
#             if t.id == id and t.time == time:
#                 return t.profit
#         return -1
#
#     max_profit_helper(1, 0)
#     return soln




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
    # print(output)

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


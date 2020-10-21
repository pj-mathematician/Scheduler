#i/p
from math import floor, ceil

# info = {
#     'wakeup': 480,
#     'breakfast': 540,
#     'lunch': 840,
#     'meeting': (900, 1020),
#     'dinner': 1200,
#     'sleep': 1440
# }

# things_td = {'maths': 240, 'physics': 180, 'chem': 180}

# prod_time = 0
# for i in list(things_td.values()):
#     prod_time+=i

# Needs to be calculated from info
"""
NOTE : All times are in minutes in a day
buffer length = 30 min
• Insert buffer length between two events
• If time b/w two events <= 30, then count it in leisure
• Adjust remaining time or required time in the sleep time
• Assume all standard events take 30 min, so pretty much add buffer to them
"""
"""
x
• if x<120, prod_time = floor(120 * 0.75)
• if x>120
    1) x%60<=30, make 2 hr and rest is leisure
    2) If 1) is false, apply scaling
NOTE : 2hr slot is 1:30 minutes of work and 30 minute leisure
"""
def mintohhmmss(min):
	h=min//60
	if h<=9:
		HH='0'+str(h)
	elif h==24:
		HH='00'
	else:
		HH=str(h)
	m=min%60
	if m<=9:
		MM='0'+str(m)
	else:
		MM=str(m)
	return HH+':'+MM+':00'

def ft_calc(d):
    var = 0

    time_slots = list(d.values())
    time_slots.sort
    for j, i in enumerate(time_slots):
        if j == len(time_slots) - 1:
            continue

        elif type(i) != type(tuple()):
            i = tuple([i, i + 30])
            time_slots[j] = i

    return var, time_slots


# def sleep_modif():
#     global free_time
#     if (prod_time - free_time) < 0:
#         info['sleep'] += (prod_time - free_time)
#         return True


def fts_calc(ts):
    free_time_slots = []

    for i in range(len(ts) - 2):
        temp = (ts[i][1], ts[i + 1][0])
        free_time_slots.append(temp)

    free_time_slots.append((ts[-2][1], ts[-1]))
    return free_time_slots


def slot_decision(w):
    p = []
    f = []
    rval = []
    if w < 120:
        p.append(90)
        f.append(w - 90)
    else:
        for i in range(w // 120):
            p.append(90)
            f.append(30)

        temp = w - ((i + 1) * 120)
        if temp <= 30:
            f.append(temp)
        else:
            p.append(floor(temp * 0.75))
            f.append(ceil(temp * 0.25))

    for i in range(len(p)):
        rval.append(p[i])
        rval.append(f[i])

    if f[-1] != 0:
        rval.append(f[-1])

    return rval


def assign(tasks, scheds):
    
    """
    Assigns every time slot a task to perform.
    """
    task = list(tasks.keys())
    sched = scheds
    l = []

    for j, i in enumerate(sched):
        
        k = j % len(tasks)
        if tasks[task[k]]==0:
            for p in range(len(tasks)):
                if tasks[task[p]] != 0:
                    k = p
                    break
            else:
                break
            

        if tasks[task[k]] > 0:
            if tasks[task[k]] >= (i[1] - i[0]):
                l.append((i[0], i[1], task[k]))
                tasks[task[k]] -= (i[1] - i[0])

            elif tasks[task[k]] < (i[1] - i[0]):
                l.append((i[0], i[0] + tasks[task[k]], task[k]))

                temp = i[0] + tasks[task[k]]
                tasks[task[k]] = 0

                for m in range(len(tasks)):
                    if tasks[task[m]] >= (i[1] - temp) and tasks[task[m]] !=0 :
                        l.append((temp, i[1], task[m]))
                        tasks[task[m]]-=(i[1] - temp)
                    elif tasks[task[m]] < (i[1] - temp) and tasks[task[m]] !=0 :
                        l.append((temp, temp+tasks[task[m]] , task[m]))
                        temp+=tasks[task[m]]
                        tasks[task[m]] =0          
        else:
            continue

    l.sort()
    return l


def schedule(fts):
    leisure = []
    sched = []
    prod_time = 0
    faltu = 0

    tracker = fts[0][0]
    for i in fts:
        tracker = i[0]
        diff = i[1] - i[0]

        if diff <= 30:
            sched.append(i)
            tracker += diff
        else:
            temp = slot_decision(diff)
            for j in range(0, len(temp) - 1, 2):
                sched.append((tracker, tracker + temp[j]))
                tracker += temp[j]
                leisure.append((tracker, tracker + temp[j + 1]))
                tracker += temp[j + 1]

            if tracker != i[1]:
                sched.append((tracker, i[1]))

    for i in sched:
        prod_time += i[1] - i[0]
    for i in leisure:
        faltu += i[1] - i[0]

    return sched, leisure, prod_time, faltu


# -- main -- #
def return_sched(info, things_td):
    prod_time = 0
    time_slots = ft_calc(info)[1]
    free_time = schedule(fts_calc(time_slots))[2]
    sched = schedule(fts_calc(time_slots))[0]
    leisure = schedule(fts_calc(time_slots))[1]

    for i in list(things_td.values()):
        prod_time+=i

    if prod_time > free_time:
        temp = leisure.pop(-1)
        sched.append(temp)
        free_time += (temp[1] - temp[0])
        if prod_time > free_time:
            a, b = sched[-1]
            b += prod_time - free_time
            sched[-1] = a, b
            free_time = prod_time
            sched.append((sched[-2][0], sched[-1][1]))
            del sched[-2:-4:-1]

    return (assign(things_td, sched))

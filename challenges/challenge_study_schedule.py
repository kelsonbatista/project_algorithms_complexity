def study_schedule(permanence_period, target_time):
    count = 0
    for period in permanence_period:
        start, end = period
        if (target_time == None or type(target_time) != int
            or start == None or type(start) != int
            or end == None or type(end) != int):
            return None
        if start <= target_time <= end:
            count += 1
    return count
        

# permanence_periods = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# print(study_schedule(permanence_periods, 5))
# print(study_schedule(permanence_periods, 4))
# print(study_schedule(permanence_periods, 3))
# print(study_schedule(permanence_periods, 2))
# print(study_schedule(permanence_periods, 1))

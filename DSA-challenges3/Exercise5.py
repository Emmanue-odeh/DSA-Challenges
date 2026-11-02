def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda interval: interval[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged


intervals = [
    [1, 3],
    [2, 6],
    [8, 10],
    [9, 12]
]

print(merge_intervals(intervals))
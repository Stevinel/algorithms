from collections import defaultdict


def points_count(max_fingers, trainer):
    count_values = defaultdict(int)
    for number in trainer:
        if number == ".":
            continue
        count_values[number] += 1

    fingers = max_fingers * 2
    score = 0
    for number in count_values.values():
        if number <= fingers:
            score += 1
    return score
    

if __name__ == "__main__":
    max_fingers = int(input())
    rows = []

    for row in range(4):
        row = input()
        rows.append(row)
    trainer = "".join(rows)
    print(points_count(max_fingers, trainer))

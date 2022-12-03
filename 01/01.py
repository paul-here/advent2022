input_path = "input.txt"
newline = "\n"

def sum_and_find_max():
    current_maxes = [0,0,0]
    data = []

    with open(input_path, 'r') as reader:
        data = reader.readlines()
        sub_sum = 0

        for i in range(len(data)):
            if data[i] == newline:
                if sub_sum > current_maxes[0]:
                    current_maxes[0] = sub_sum
                    current_maxes.sort()
                sub_sum = 0
                continue

            if data[i] != newline:
                sub_sum += int(data[i])

    total = current_maxes[0] + current_maxes[1] + current_maxes[2]
    print(total)


def main():
    sum_and_find_max()

if __name__ == "__main__":
    main()
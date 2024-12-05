##Advent of Code Day 1 Part 1

import time

def main():

    f = open("input.txt", 'r')
    total = 0

    list1 = []
    list2 = []

    while True:
        line = f.readline().strip()
        if not line: break

        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))

    list1.sort()
    list2.sort()

    for i in range(len(list1)):
        total += abs(list1[i] - list2[i])

    print("%%%%")
    print("Total: %d" % total)
    print("%%%%")

    f.close()

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("Finished in %.2f seconds" % (time.time() - start_time))
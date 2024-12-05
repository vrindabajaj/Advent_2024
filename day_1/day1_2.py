##Advent of Code Day 1 Part 2

import time

def main():

    f = open("input.txt", 'r')
    total = 0

    left = []
    right = []

    while True:
        line = f.readline().strip()
        if not line: break

        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))

    for val in left:
        occurences = 0
        for i in range(len(right)):
            if right[i] == val:
                occurences += 1
        total += val * occurences
        

    print("%%%%")
    print("Total: %d" % total)
    print("%%%%")

    f.close()

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("Finished in %.2f seconds" % (time.time() - start_time))
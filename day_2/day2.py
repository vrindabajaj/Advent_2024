##Advent of Code Day 2 Part 1

import time

def main():

    f = open("input.txt", 'r')
    total = 0

    while True:
        line = f.readline().strip()
        if not line: break

        level = [int(x) for x in line.split()]
        
        print(level)

        inc = False
        dec = False
        unsafe = False

        for current, next in zip(level, level[1:]):

            diff = current - next
            if(abs(diff) > 3 or abs(diff) < 1):
                unsafe = True
                break
            if (diff < 0):
                inc = True
            elif (diff > 0):
                dec = True

            if (inc and dec): 
                unsafe = True
                break
        
        if (not unsafe):
            print("Safe")
            total += 1


    print("%%%%")
    print("Total: %d" % total)
    print("%%%%")

    f.close()

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("Finished in %.2f seconds" % (time.time() - start_time))
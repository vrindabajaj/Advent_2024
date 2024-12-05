##Advent of Code Day 

import time

def main():

    f = open(".txt", 'r')
    total = 0

    while True:
        line = f.readline()
        if not line: break


        


    print("%%%%")
    print("Total: %d" % total)
    print("%%%%")

    f.close()

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("Finished in %.2f seconds" % (time.time() - start_time))
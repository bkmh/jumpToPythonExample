import sys

if __name__ == "__main__":
    arguments = sys.argv
   
    print(arguments)

    if len(sys.argv) > 1:
        params = sys.argv[1:]

        sumValue = 0

        for param in params:

            sumValue += int(param)

        print(sumValue)
        


import sys
from CopyFind import CopyFind

if __name__ == "__main__":

    if len(sys.argv)<4:
        print("Wrong arguments!")
        sys.exit()

    csv_name = sys.argv[1]
    col1 = sys.argv[2]
    col2 = sys.argv[3]
    
    test = CopyFind("t1","t2")
    test.run()

    print("Done")
import sys
import pandas as pd
from CopyFind import CopyFind

def parseFiles(csv, col1, col2, bit):
    df = pd.read_csv("resources/"+csv, error_bad_lines=False, warn_bad_lines=True)
    for index, row in df.iterrows():
        cp = CopyFind(row[col1],row[col2],bit)
        cp.run()

        if index==10:
            break;


#py main.py ea_press_release.csv  snippet_body  pr_snippet_body_1 64
if __name__ == "__main__":

    if len(sys.argv)<5:
        print("Wrong arguments!")
        sys.exit()

    if sys.argv[4]!="32" and sys.argv[4]!="64":
        print("The last argument must have value 32 or 64 based on your machine")
        sys.exit()
        
    parseFiles(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])

    print("Done")
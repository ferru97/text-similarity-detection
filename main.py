import sys
import utils
import pandas as pd
from CopyFind import CopyFind

def parseFiles(csv, col1, col2, bit):
    df = pd.read_csv("resources/"+csv, error_bad_lines=False, warn_bad_lines=True)
    total = len(df.index)
    for index, row in df.iterrows():
        utils.printProgressBar(index+1, total)
        cp = CopyFind(row[col1],row[col2],bit)
        perfect_match, overall_match_l, overall_match_r = cp.run()

        df.loc[index,"Perfect Match"] = perfect_match
        df.loc[index,"Perfect Match (L%)"] = int((100/len(row[col2].split())*perfect_match))
        df.loc[index,"Perfect Match (R%)"] = int((100/len(row[col1].split())*perfect_match))
        df.loc[index,"Overall Match (L)"] = overall_match_l
        df.loc[index,"Overall Match (L%)"] = int((100/len(row[col2].split())*overall_match_l))
        df.loc[index,"Overall Match (R)"] = overall_match_r
        df.loc[index,"Overall Match (R%)"] = int((100/len(row[col1].split())*overall_match_r))

    df.to_csv("results/"+csv)


#py main.py ea_press_release.csv  snippet_body  pr_snippet_body_1 64
if __name__ == "__main__":

    if len(sys.argv)<5:
        print("Wrong arguments!")
        sys.exit()

    if sys.argv[4]!="32" and sys.argv[4]!="64":
        print("The last argument must have value 32 or 64 based on your machine")
        sys.exit()
        
    parseFiles(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])

    print("Done!")
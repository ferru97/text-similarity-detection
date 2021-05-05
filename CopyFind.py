from bs4 import BeautifulSoup
import subprocess
import utils
import os

class CopyFind:

    cf_main = "Copyfind/"
    cf_input = "Copyfind/docs/"
    cf_output = "Copyfind/results/"
    cf_exe64 = "Copyfind\\run64.bat"
    cf_exe32 = "Copyfind\\run32.bat"
    cf_out_file = "Copyfind/results/matches.txt"
    cf_script_template = "resources/script-template.txt"
    
    def __init__(self, doc1, doc2, bit):
        utils.writeFile(os.path.join(self.cf_input,"doc1.txt"),doc1)
        utils.writeFile(os.path.join(self.cf_input,"doc2.txt"),doc2)
        if bit=="32":
            self.cf_exe = self.cf_exe32
        else:
            self.cf_exe = self.cf_exe64
        self.script_template = utils.readFile(self.cf_script_template)


    def genScript(self):
        input_path = os.path.abspath(self.cf_input)
        output_path = os.path.abspath(self.cf_output)
        self.script_template = self.script_template.replace("[doc-input1]",os.path.join(input_path,"doc1.txt"))
        self.script_template = self.script_template.replace("[doc-input2]",os.path.join(input_path,"doc2.txt"))
        self.script_template = self.script_template.replace("[cf-output]",output_path)

    
    def run(self):
        self.genScript()
        utils.writeFile(os.path.join(self.cf_main,"script.txt"),self.script_template)

        result = subprocess.run([self.cf_exe], capture_output=True)
        out = str(result.stdout).replace('\n',' ')+" "+str(result.stderr).replace('\n',' ').strip()

        perfect_match = 0
        overall_match_l = 0
        overall_match_r = 0
        shared_l = ""
        shared_r = ""
        res = utils.readFile(self.cf_out_file)
        res = res.split()
        if len(res)>2:
            perfect_match = int(res[0])
            overall_match_l = int(res[1])
            overall_match_r = int(res[2])
            shared_l = self.getCommonPhrases(self.cf_output+"doc1.txt.doc2.txt.html")
            shared_r = self.getCommonPhrases(self.cf_output+"doc2.txt.doc1.txt.html")

        return perfect_match, overall_match_l, overall_match_r, shared_l, shared_r


    def getCommonPhrases(self,file):
        content = utils.readFile(file)
        soup = BeautifulSoup(content, "html.parser")
        phrases = []
        for p in soup.find_all("font",{"color": "#FF0000"}):
            phrases.append(p.text.strip())
        
        return " - ".join(phrases)
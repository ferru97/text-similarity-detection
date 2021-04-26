import subprocess
import utils
import os

class CopyFind:

    cf_main = "Copyfind/"
    cf_input = "Copyfind/docs/"
    cf_output = "Copyfind/results/"
    cf_exe64 = "Copyfind\\run64.bat"
    cf_exe32 = "Copyfind\\run32.bat"
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
import subprocess
import utils
import os

class CopyFind:

    cf_main = "Copyfind/"
    cf_input = "Copyfind/docs/"
    cf_output = "Copyfind/results/"
    cf_exe = "Copyfind/Copyfind.4.1.5.exe"
    cf_script_template = "resources/script-template.txt"
    
    def __init__(self, doc1, doc2):
        utils.writeFile(os.path.join(self.cf_input,"doc1"),doc1)
        utils.writeFile(os.path.join(self.cf_input,"doc2"),doc2)
        self.script_template = utils.readFile(self.cf_script_template)


    def genScript(self):
        input_path = os.path.abspath(self.cf_input)
        output_path = os.path.abspath(self.cf_output)
        self.script_template = self.script_template.replace("[doc-input]",input_path)
        self.script_template = self.script_template.replace("[cf-output]",output_path)

    
    def run(self):
        self.genScript()
        utils.writeFile(os.path.join(self.cf_main,"script.txt"),self.script_template)

        result = subprocess.run([self.cf_exe, self.script_template], capture_output=True)
        out = result.stdout.decode('utf-8').replace('\n',' ')+" "+result.stderr.decode('utf-8').replace('\n',' ').strip()
        print(out)

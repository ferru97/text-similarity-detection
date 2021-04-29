# text-similarity-detection
A tool to calculate the similarity between two texts using Copyfind4.1.5

## Requirements
- Python 3.x downloadable from [HERE](https://www.python.org/downloads/)
- Copyfind4.1.5 available [HERE](https://plagiarism.bloomfieldmedia.com/software/copyfind/). Already provided

### Script execution
- Only the first time, open the CMD in the script folder and run `pip install -r requirements.txt`
- Run the script using the following format `py main.py "file_name.csv" "column_1" "column_2" bit` where:
    - *file_name.csv* is the csv file to analyze located in the resources folder
    - *column_1* and *column_2* are the two columns to compare for each row
    - *bit* in either 32 or 64 based on your Windows version. To check it follow this [GUIDE](https://support.microsoft.com/en-us/windows/32-bit-and-64-bit-windows-frequently-asked-questions-c6ca9541-8dce-4d48-0415-94a3faa2e13d)

The results are saved on the *results* folder

## Parameter tuning
To tune the parameters of the detection change the values of the **PARAMETERS AREA** of the *resources/script-template.txt* file.
A list of all the parameters il available [HERE](https://plagiarism.bloomfieldmedia.com/software/wcopyfind-instructions/)
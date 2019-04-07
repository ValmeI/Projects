
def file_result_to_list(path, file):
    file_o = open(path + file, encoding="utf8")
    file_text = []
    for x in file_o:
        '# remove color charaters'
        x = x.replace('[31m', '')
        x = x.replace('[0m', '')
        x = x.replace('[32m', '')
        file_text.append(x)
    return file_text

'''
from Portfolio_calculator.Funcions import what_path_for_file
path = str(what_path_for_file()) + r'Calculators\portfolio_result/'
portfolio_result = file_result_to_list(path, "Print_result.txt")
for x in portfolio_result:
    print(x)
'''
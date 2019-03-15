from Portfolio_calculator.Funcions import what_path_for_file
import time
from datetime import date
from Send_Email import Send
'# 0 = Monday and so on..So 4 is friday, then send email to mörr'
Täna = date.today()

print(what_path_for_file())


print(time.strftime('%d-%m-%Y'))
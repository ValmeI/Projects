from Komfovent_Ventilation.functions import get_vent_stats, add_xpos_in_list, column_width, create_excel, write_to_excel
import datetime

'# get today-s datetime but without milliseconds'
today_str = datetime.datetime.now().isoformat(' ', 'seconds')

'# add data from api-s to one big list'
combined_data_list = get_vent_stats("http://192.168.1.60/", 'det') + \
                     get_vent_stats("http://192.168.1.60/", 'i2') + \
                     get_vent_stats("http://192.168.1.60/", 'i')

'# add today-s date the beginning of the list'
new_vent_data_list = add_xpos_in_list(today_str, 0, combined_data_list)
#print(new_vent_data_list)
#create_excel('proov', 'sheet_name')
#column_width('proov', 'sheet_name' )
write_to_excel("SampleData", new_vent_data_list)
print('Success')

import csv
import math
import sys


if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python2 ./src/border_analytics.py ./input/Border_Crossing_Entry_data.csv ./output/report.csv")
    sys.exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

# Converts data into a nested dictionary format with (Border , Measure):{Date:Value}
def dic_conversion(data):
    for row in data:
        border, date, measure, value = row[3], row[4], row[5], row[6]
        final_dict.setdefault((border,measure),{}).setdefault(date,[]).append(int(value))
    return final_dict

# Calculates the sum of the list for crossings using a particular measure 
def get_sum(final_dict):
    for border_key, date_key in final_dict.items():
        for month in date_key.keys():
            date_key[month] = sum(date_key[month])
    return final_dict

# Calculating running monthly average of total number of crossings using a measure for a border.
def get_monthly_avg(final_dict):
    average_dict = {}
    for border_key, date_key in final_dict.items():
        temp = 0
        avg_val = 0
        keyList = sorted(date_key.keys())
        for i, v in enumerate(keyList):
            # print(i)
            temp = 0.0
            flag = 0
            for j in range(0, i):
                temp += date_key[keyList[j]]
                flag += 1
            if flag > 0:
                avg_val = int(math.ceil(temp / flag))

            average_dict[date_key[v]] = avg_val
    return average_dict

# Converts the dictionary into a list format which is similar to the output format
def get_list_from_dict(final_dict):
    temp_list = []
    for k, v in final_dict.items():
        if len(v.keys()) > 1:
            for _k, _v in v.items():
                temp_list.append([k[0], k[1], _k, _v])
        else:
            temp_list.append([k[0], k[1], list(v.keys())[0], list(v.values())[0]])
    return temp_list

# Formatting the list and appending the averages to the corresponding measure
def get_final_format(temp_list):
    for i in range(0, len(temp_list)):
        if temp_list[i][3] in average_dict.keys():
            temp_list[i].append(average_dict[temp_list[i][3]])
    # temp_list
    newTemp = [[x[0], x[2], x[1], x[3], x[4]] for x in temp_list]
    return newTemp


final_dict = {}
#Loading data as a nested dictionary in the format (Border, Measure):{Date:Value}
with open(input_file, 'r') as file:
    data = csv.reader(file, delimiter=',')
    fields = next(data)
    final_dict = dic_conversion(data)
#print(final_dict)

final_dict = get_sum(final_dict)
#print(final_dict)

# Calculating running monthly average of total number of crossings using a measure for a border.
average_dict = get_monthly_avg(final_dict)
#print(average_dict)


#Creating a list from the final_dict dictionary
#final_dict_copy = final_dict
temp_list = get_list_from_dict(final_dict)
#print(temp_list)

newTemp = get_final_format(temp_list)
#print(newTemp)

#Sorting the list as required
newTemp.sort(key=lambda x:[x[1],x[3],x[2],x[0]],reverse=True)
#print(newTemp)

list2 = [x for x in newTemp if x != []]
#Writing results to the report.csv file
with open(output_file,'w') as resultFile:
    wr = csv.writer(resultFile)
    wr.writerow(['Border','Date','Measure','Value','Average'])
    for row in list2:
        wr.writerow(row)

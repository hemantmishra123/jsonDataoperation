import sys
import json
import pandas as pd
import math 
from logging import *
basicConfig(filename='logfile.log',level=DEBUG,filemode='w')
#This is the Function for accessing the jsonfile
def validateJSON(jsonData):
    #File is given correctly it will perform the task.and return a vaues list as per the condition.\
    data_tuples=[]
    try:
        json_data=json.load(jsonData)
        value_list =[]
        for value in json_data.values():
            value_list.append(value)            
        k=0
        for item in value_list:
            if isinstance(item, str):
                item = item[::-1]
                value_list[k]=item
            if isinstance(item, int):
                item=item*item
                value_list[k]=item
            
            if type(item) is list:
                if(type(item[0]) is str):
                    item=[x[::-1] for x in item]
                    value_list[k]=item

                if(type(item[0]) is int):
                    item=[x*x for x in item]
                    value_list[k] = item
            k+=1
        Key=[]
        debug("Json Files is successfully Parsed and performed operations")
        for key in json_data.keys():
            Key.append(key)
        data_tuples = zip(Key,value_list)

    #File is given by the user is not json it will raise an Error.Return a False Statment
    except ValueError as err:
        print("This is Not a Valid Json Files Please Upload a valid json Files")
        error("This is Not a Valid Json Files Please Upload a valid json Files")
        return False
    return data_tuples

f = open(sys.argv[1],'r')
flag=validateJSON(f)
if(type(flag) is not bool):
    #New DataFrame with as per the condition values corrospoding to the keys as per condition.
    data_tuples=flag
    df = pd.DataFrame(data_tuples, columns=['Key','Value'])
    print(df)

#!/usr/bin/python3.8/

import requests
import time
import json
import sched
import os


class IndiaWebScrapper:
    __s = sched.scheduler(time.time, time.sleep)
    __url = "https://www.mohfw.gov.in/data/datanew.json"
    __t = time.localtime()
    __state_name_list = list()
    __data = ''

    def __init__(self):
        self.__get_data()
        self.init_state_names()

    def init_state_names(self):
        for ele in self.__data:
            self.__state_name_list.append(ele['state_name'])

    def __get_data(self):
        try:
            r = requests.get(self.__url)
            self.__data = r.json()
        except:
            print('[-] Error connecting to "{}" '.format(self.__url))
            print('[+] Check for active internet Connection.')
            exit()

    def __new_json_file_name(self, prefx='', file_extension='json'):
        return './' + str(prefx) + str(self.__t.tm_year) + ':' + str(self.__t.tm_mon) + ':' + str(
            self.__t.tm_mday) + ':' + str(self.__t.tm_hour) \
               + ':' + str(self.__t.tm_min) + ':' + str(self.__t.tm_sec) + '.' + file_extension

    def __write_file_to_disc(self, data, dir='json', prefx='', access='w'):
        if not os.path.exists(dir):
            os.mkdir(dir)
        try:
            temp_file_name = self.__new_json_file_name(prefx=prefx)
            file = open(dir + '/' + temp_file_name, access)
            json.dump(data, file, indent=4, sort_keys=False)
            file.close()
            print("\n[+] Write successful. check in /{}/{}\n".format(dir, temp_file_name))
            return
        except:
            print('\n[-] Error writing data to disc.\n')
            exit()

    def get_state_names(self):
        for ele in self.__state_name_list:
            print(ele)

    def get_state(self, state='state', prefx=''):
        if state == 'state':
            sl = 0
            self.__print_state_names()
        else:
            for ele in self.__data:
                if ele["state_name"] == state:
                    print(state)
                    print(ele)
                    exit()
            self.__print_state_names()
            print('[-] State "{}" not found, please enter correct state OR check for spellings.\n'.format(state))

    def get_all_state(self):
        for state in self.__data:
            print(state)

    def __print_state_names(self):
        sl = 0
        for state in self.__state_name_list:
            if state != '':
                sl = sl + 1
                print("[{}] {}".format(sl, state))
        print('\n[-]Please Enter Particular State, from above list.\n')
        return

    def write_state(self, state='state', prefx=''):
        if state == 'state':
            self.__print_state_names()
        else:
            for ele in self.__data:
                if ele["state_name"] == state:
                    print(state)
                    self.__write_file_to_disc(data=ele, dir=str(state), prefx=str(prefx))
                    exit()
            self.__print_state_names()
            print('[-] State "{}" not found, please enter correct state OR check for spellings.\n'.format(state))

    def write_all_state(self):
        self.__write_file_to_disc(data=self.__data)

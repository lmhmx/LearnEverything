from typing import Dict
import yaml
import argparse
import getpass
import re
import os
import time
import random
import struct
from os import environ, error

def str2int(s:str, character:str)->int:
    num = 0
    character_size = len(character)
    for c in s:
        index = character.index(c)
        num = num * character_size + index
    return num
def reverse(s:str)->str:
    return s[::-1]
def int2str(a:int, character:str)->str:
    ans = ""
    size = len(character)
    while(a>0):
        ans = ans + character[a%size]
        a = a//size
    ans = reverse(ans)
    return ans

def repeat_to_size(s:str, size, character)->str:
    s_num = str2int(s, character)
    random.seed(s_num)
    max_num = len(character)
    repeat_s = ""
    for i in range(size):
        r = random.randint(0, max_num-1)
        repeat_s = repeat_s+character[r]
    return repeat_s

def encode(content:str, passwd:str, character:str, extend_passwd_size:int)->str: 
    content_num = str2int(content, character) 
    extend_passwd = repeat_to_size(passwd, extend_passwd_size,character)
    extend_passwd_num = str2int(extend_passwd, character)
    ans = content_num * extend_passwd_num
    ans_str = int2str(ans, character)
    return ans_str
def decode(content_str, passwd:str, character:str, extend_passwd_size:int)->str:
    content_num = str2int(content_str, character)
    extend_passwd = repeat_to_size(passwd, extend_passwd_size, character)
    passwd_num = str2int(extend_passwd,character)
    result = content_num//passwd_num
    check = content_num%passwd_num
    if(check!=0):
        raise ValueError("decode error, the passwd is invalid")
    result_str = int2str(result, character)
    return result_str

def save_user_passwd_of_name(passwd, passwd_of_name, file, character, size):
    print("saving passwd to {}".format(file),end=" ")
    s = yaml.safe_dump(passwd_of_name)
    s_save = encode(s, passwd, character, size)
    with open(file, "w") as f:
        f.write(s_save)
    print("finished")

def update_user_passwd(args, passwd_of_name, character):
    if(args.passwd):
        new_passwd = getpass.getpass("input the new passwd: ")
        confirm = getpass.getpass("input the passwd again: ")
        if(new_passwd == confirm):
            save_user_passwd_of_name(new_passwd, passwd_of_name, args.inputfile, character, args.new_size)
            print("update passwd ok")
        else:
            print("passwd not consisted")
        
if(__name__ == "__main__"):
    character = "0123456789"
    character += "abcdefghijklmnopqrstuvwxyz"
    character += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    character += "!@#$%^&*()-=_+[}{]|\\\"';:.>,</?`~"
    character += "\n \t"
    
    parser = argparse.ArgumentParser()
    parser.description="enter the code parameter"
    parser.add_argument("-s", "--size", help="the extend size of the passwd, default 1000", type=int, default=1000)
    parser.add_argument("-i", "--inputfile", help="input file, default passwd", type=str, default="passwd")
    parser.add_argument("-o", "--outputfile", help="output file, default \"\"",type=str, default="")
    parser.add_argument("-l", "--list", help="list the items, default no", type=bool, default=False)
    parser.add_argument("-a", "--add", help="add new item", type=str, default="")
    parser.add_argument("-d","--delete", help="delete an item", type = str, default="")
    parser.add_argument("-w","--watch",help="watch the item, use * represent any character of any numbers", type=str,default="")
    parser.add_argument("-t", "--time", help = "watch time", type = float, default=1)
    parser.add_argument("-e", "--edit", help="edit an item", type=str, default="")
    parser.add_argument("-p", "--passwd", help="new passwd", action="store_true")
    parser.add_argument("-n", "--new_size", help="the extend size of the new passwd, default 1000", type=int, default=1000)
    args =parser.parse_args()

    try:
        is_changed = False
        passwd = getpass.getpass("input the passwd: ")
        passwd_of_name = None
        f_str = ""
        try:
            with open(args.inputfile, "r") as f:
                f_str = f.read()
            decode_str = decode(f_str, passwd, character, args.size)
            passwd_of_name = yaml.safe_load(decode_str)
            if(passwd_of_name == None or type(passwd_of_name)!=dict):
                raise "error input"
        except Exception as e:
            if(f_str != ""):
                print("*"*80)
                print("Error, the input file `{}` can't be decoded by the passwd.".format(args.inputfile))
                print("*"*80)
                raise Exception("passwd error")
            else:
                passwd_of_name = {}
        
        print(passwd_of_name)
        if(args.passwd):
            update_user_passwd(args, passwd_of_name, character)
        else:
            num = 0
            if(args.watch!=""):
                watch_re = args.watch.replace('*','(.*?)')
                print("*"*80)
                print("watch {} result: ".format(args.watch))
                print("")
                for name in passwd_of_name:
                    if(re.search(watch_re, name)!=None):
                        print("{:<15s}: {:<15s}".format(name, passwd_of_name[name]))
                print("*"*80)
                time.sleep(args.time)
                os.system("clear")
                num = num+1
            if(args.delete):
                if(args.delete in passwd_of_name.keys()):
                    passwd_of_name.pop(args.delete)
                    print("delete {} success".format(args.delete))
                    is_changed = True
                else:
                    print("{} passwd does not exist")
                num = num+1
            if(args.edit!=""):
                if(args.edit in passwd_of_name):
                    item_passwd = getpass.getpass("input the new passwd of {}: ".format(args.edit))
                    confirm = getpass.getpass("input the passwd again: ".format(args.edit))
                    if(item_passwd == confirm):
                        print("update the passwd of {}".format(args.edit))
                        passwd_of_name[args.edit] = item_passwd
                        is_changed = True
                    else:
                        print("the passwd are not consisted")
                else:
                    print("{} does not exist".format(args.edit))
                num = num+1
            if(args.add!=""):
                if(not args.add in passwd_of_name):
                    item_passwd = getpass.getpass("input the new passwd of {}: ".format(args.add))
                    confirm = getpass.getpass("input the passwd again: ".format(args.add))
                    if(item_passwd == confirm):
                        print("update the passwd of {}".format(args.add))
                        passwd_of_name[args.add] = item_passwd
                        is_changed = True
                    else:
                        print("the passwd are not consisted")
                else:
                    print("{} already exists".format(args.add))
                num = num+1
            if(args.outputfile != ""):
                with open(args.outputfile, "w") as f:
                    yaml.safe_dump(passwd_of_name, f)
                num = num+1
            if(args.list):
                for name in passwd_of_name:
                    print("{:<15s}: ****".format(name))
            if(not args.list and num ==0):
                for name in passwd_of_name:
                    print("{:<15s}: ****".format(name))

            if(is_changed):
                save_user_passwd_of_name(passwd, passwd_of_name, args.inputfile, character, args.size)

    except Exception as e:
        # print(e)
        pass

import subprocess
import os
import json
import sys
import re

def convert2csv(data):

    access_dict = {"dir_list": []}
    if data:
        file_info = None
        for line in data.splitlines():
            #print line
            if ':\\' in line or '\\\\' in line:
                #print "This is a new folder"
                if file_info:
                    access_dict['dir_list'].append(file_info)
                    file_info = {'folder_path': line, 'access_list': []}
                else:
                    #First folder in the list
                    file_info = {'folder_path': line, 'access_list': []}
            elif len(line) > 0:
                tokens = line.split()
                nt = None
                access_info = {}
                if " NT " in line:
                    #NT line
                    access, domain_username = line.split(" NT ")
                    access = access.split()[0]
                elif len(tokens) == 2:
                    #Normal line
                    access, domain_username = line.split()
                else:
                    print "line in bad format"
                    continue
                access_info['access'] = access
                if "\\" in domain_username:
                    domain, username = domain_username.split("\\")
                else:
                    domain = domain_username
                    username = domain_username
                access_info['domain'] = domain
                access_info['username'] = username
                file_info['access_list'].append(access_info)
        if file_info:
            access_dict['dir_list'].append(file_info)
        #output to csv file
        f = open('out.csv', 'w')
        print ("Generating the csv file out.csv")
        f.write('Folder Path,   User Domain,    User Name,  User Permission\n') 
        if file_info:
            for directory in access_dict['dir_list']:
                printed = False
                for access in directory['access_list']:
                    if not printed:
                        f.write(directory['folder_path'] + ",\t")
                        printed = True
                    else:
                        f.write(",\t")
                    f.write(access['domain'] + ",\t")
                    f.write(access['username'] + ",\t")
                    f.write(access['access'] + ",\t\n")
                

    #print json.dumps(access_dict, indent=4, sort_keys=True)



if len(sys.argv) != 2:
    print "Invalid argument input"
    sys.exit()
file_path = sys.argv[1]

with open(file_path) as f:
    print ("Reading the input file " + file_path)
    data=f.read()
    convert2csv(data)

print("Finished! Thanks")

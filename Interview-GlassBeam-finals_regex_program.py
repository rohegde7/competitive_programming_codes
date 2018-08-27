import re
import random

in_file = open("Interview-Glassbeam-finals_Sample_log.txt", "r")  #opening the file for reading

str_text = in_file.read()   #all the data from the file

#finding all the valid IP address in the file:
lst_ip_address = re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\b', str_text)

#lst_mac_address = re.findall(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', str_text)
lst_mac_address = re.findall(r'[0-9a-fA-F][0-9a-fA-F][:][0-9a-fA-F][0-9a-fA-F][:][0-9a-fA-F][0-9a-fA-F][:][0-9a-fA-F][0+-9a-fA-F][:][0-9a-fA-F][0-9a-fA-F][:][0-9a-fA-F][0-9a-fA-F]$', str_text)

for ip in range(len(lst_ip_address)):   #replacing all the valid IP address with another radomly generated valid IP address 
    random_ip1 = random.randrange(256)
    random_ip2 = random.randrange(256)
    random_ip3 = random.randrange(256)
    random_ip4 = random.randrange(256)

    replacement_string = str(random_ip1)+str('.')+str(random_ip2)+str('.')+str(random_ip3)+str('.')+str(random_ip4)

    str_text = re.sub(lst_ip_address[ip], replacement_string, str_text)

for mac in range(len(lst_mac_address)):   #replacing all the valid MAC address with another radomly generated valid mac address 
    replacement_mac = ''
    for i in range(6):
        for x in range(2):
            replacement_mac = replacement_mac + random.choice('0123456789ABCDEF')
        
        replacement_mac = replacement_mac + ':'

    replacement_mac = replacement_mac[:len(replacement_mac)-1]
    str_text = re.sub(lst_mac_address[mac], replacement_mac, str_text)
    
#print(str_text)

in_file.close()

in_file = open("Interview-Glassbeam-finals_Sample_log.txt", 'w')
in_file.write(str_text)
in_file.close()


flag = 0

with open("Interview-Glassbeam-finals_Sample_log.txt", 'r') as in_file:
    for line in in_file:    #iterating through all the lines in the file
        if flag == 1:
            if 'show' not in line:
                new_file.write(line)
            else:
                flag = 0

        if 'show' in line:  #checking whether there exist the keyword "show"
            flag = 1
            lst_line = line.split()

            file_name = ''    
            for i in range(1, len(lst_line)):   #file name for the new file to be created
                file_name = file_name + lst_line[i] + str(' ')
            
            new_file = open(file_name, "w")

in_file.close()
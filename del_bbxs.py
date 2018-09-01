import re
import pdb


def del_str_lines(del_file):
    with open(del_file, "r+") as f:
        p = re.compile("0.001|0.002|0.003")
        lines = [line for line in f.readlines() if p.search(line) is None]
        f.seek(0)
        f.truncate(0)
        f.writelines(lines)

def del_redunparts(del_file):
    with open(del_file, "r+") as f:
        lines = f.readlines()
        line_list =['' for n in range(len(lines))]
        count = 0
        for line in lines:
            splict_line = re.split(r'[ ]',line)
            #pdb.set_trace()#################
            #splict_line = re.split(r'.jpg',line)  
            line = ' '.join(splict_line[0:2])+'.jpg,'+splict_line[2]+'\n'
            #line = splict_line[0]+'\n'
            #line = '_'.join(splict_line[2:6])
            #splict_line = re.split('([ ])',line)
            #line = ''.join(splict_line[0:5])
            line_list[count] = line
            #line_list[count] = splict_line[count]+'\n'
            count+=1
        pdb.set_trace()#################
        f.seek(0)
        f.truncate(0)
        f.writelines(line_list)

def op_firstn(del_file,n):
    ori_file = del_file
    line_num = 0
    with open(ori_file, 'r+') as f:
        old_lines = f.readlines()
        new_len = int(len(old_lines) / n)
        new_lines = ['' for n in range(new_len)]
        old_probs = [0.000 for n in range(len(old_lines))]
        new_probs = [0.000 for n in range(new_len)]        
###############
        index = 0
        for i in range(len(new_lines)):
            line_names[count] = re.split(r'[,]',new_lines[i])[0]
            index += 1
        rmsame_line_names = []
        rmsame_old_lines = []
        index = 0
        for line_name in line_names:
            index += 1
            if not line_name in rmsame_line_names:
                rmsame_line_names.append(j)

                if line_i[0] == line_j[0]:
                    if float(line_i[1]) > float(line_j[1]):
                        new_lines.remove(new_lines[j])
                    else:
                        new_lines.remove(new_lines[i])
#################
        count = 0
        for line in old_lines:
            splict_line = re.split(r'[,]',line)
            old_probs[count] = float(splict_line[1])
            count += 1
##############
        count = 0
        for count in range(len(old_probs) -1):
            new_len_num = int(count/n)
            for i in range(n-1):
                new_probs[new_len_num] += old_probs[count+i]
            if new_probs[new_len_num] >= 1.000 :
                new_probs[new_len_num] = 0.9999
            if new_probs[new_len_num] <= 0.009 :
                new_probs[new_len_num] = 0.0
            new_lines[new_len_num] = re.split(r'[,]',old_lines[count])[0]+','+str(float('%.4f'%new_probs[new_len_num]))+'\n'
            count += 1
            count = int(count * n)            
        pdb.set_trace()#################
        f.seek(0)
        f.truncate(0)
        f.writelines(new_lines)

def prob_plus(del_file):
    ori_file = del_file
    line_num = 0
    with open(ori_file, 'r+') as f:
        old_lines = f.readlines()

###############
        index = 0
        line_names = ['' for n in range(len(old_lines))]
        line_probs  = [0.000 for n in range(len(old_lines))]
        for i in range(len(old_lines)):
            line_names[i] = re.split(r'[,]',old_lines[i])[0]
            line_probs[i] = re.split(r'[,]',old_lines[i])[1]
            index += 1
        rmsame_line_names = []
        name_probs = {}
        index = 0
        for line_name in line_names:
            if not line_name in rmsame_line_names:
                rmsame_line_names.append(line_name)
                name_probs[line_name] = float(line_probs[index])
            else:
                name_probs[line_name] += float(line_probs[index])
                name_probs[line_name] /= 2
                #if float(line_probs[index]) > name_probs[line_name]:
                #    name_probs[line_name] = float(line_probs[index])

            index += 1

##############
        count = 0
        rmsame_lines = ['' for n in range(len(name_probs))]
        for key, value in name_probs.items():
            #value = value * 9
            if value >= 1.0 :
                value = 0.999999
            if value == 0 :
                value = 0.000001
            rmsame_lines[count] = key+','+str(float('%.6f'%value))+'\n'
            count += 1        
        pdb.set_trace()#################
        f.seek(0)
        f.truncate(0)
        f.writelines(rmsame_lines)


def del_p1(del_file):
    with open(del_file, "r+") as f:
        lines = f.readlines()
        line_list =['' for n in range(len(lines))]
        count = 0
        for line in lines:
            splict_line = re.split(r'[,]',line)
            prob = float(splict_line[1])  
            if prob == 1.000:
                line = splict_line[0]+','+'0.999\n'
            #splict_line = re.split('([ ])',line)
            #line = ''.join(splict_line[0:5])
            line_list[count] = line
            count+=1
        pdb.set_trace()#################
        f.seek(0)
        f.truncate(0)
        f.writelines(line_list)

del_file = "08031.csv"
#del_str_lines(del_file)
#del_p1(del_file)
del_redunparts(del_file)
#op_firstn(del_file,3)
#prob_plus(del_file)

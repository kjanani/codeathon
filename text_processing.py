# Janani Kalyanam
# text processing code

import os, sys
import re
import json
import unicodedata

def clean(text):

    text = str.replace(text,',','');
    text = str.replace(text,"'",'');
    text = str.replace(text,'"','');
    text = str.replace(text,'!','');
    text = str.replace(text,'^','');
    text = str.replace(text,'(','');
    text = str.replace(text,')','');
    text = str.replace(text,'%','');
    text = str.replace(text,'-','');
    text = str.replace(text,'_','');
    text = str.replace(text,'|','');
    text = str.replace(text,'.','');
    text = str.replace(text,':','');
    text = str.replace(text,'@','');
    text = str.replace(text,'#','');
    
    text = re.sub('\s+', ' ',text).strip();
    text = text.split(' ');
    new_text = [];
    for each in text:
        if(str.find(each,'http') != -1):
            continue;
        if not each.isalnum():
            continue;
        new_text.append(str.lower(each));
    text = ' '.join(new_text);

    return text;


if __name__ == '__main__':

    lines = open('temp.json','r').readlines()
    fout = open('cleantext_tweetid.txt','w')

    for line in lines:
        try:
            JO = json.loads(line)
            if('text' in JO.keys()):
                print(JO['text'])
                fout.write(JO['id_str'] + ':' + clean(JO['text']) + '\n')
        except:
            continue



# Janani Kalyanam
# text processing code

import os, sys
import re
import pymongo
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
        if(!each.isalnum()):
            continue;
        new_text.append(str.lower(each));
    text = ' '.join(text);

    return text;


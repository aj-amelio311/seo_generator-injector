import os
from random import randint

path = os.getcwd()

html_files = []
all_titles = []
all_files = []
all_keywords = []
all_descs = []

town1 = "White Plains"
town2 = "Portchester"
zip1 = "10605"
phone = "(555) 555-5555"
name = "Dr. John Smith"
occupation = "Dentist"

for i in os.listdir(path):
    if i.endswith(".html"):
        html_files.append(i)
        title =  i.split(".")[0]
        if title != "index" and title != "contact":
            name_of_page = title
        elif title == "contact":
            name_of_page = title + " " + occupation
        else:
            name_of_page = occupation
        name_of_page = name_of_page.replace("_", " ").title()
        get_number = [1, 2, 3]
        title_generator = randint(0, len(get_number) - 1)
        if title_generator == 1:
            title_tag = "<title>" + name_of_page + " in " + town1 + " | " + town2 + " " + name_of_page + " | " + name_of_page + " " + zip1 + "</title>"
        elif title_generator == 2:
             title_tag = "<title>" + town2 + " " + name_of_page + " | " + name_of_page+ " in " + town1 + " | " + name_of_page + " in " + town2 + "</title>"
        else:
            title_tag = "<title>" + town1 + " " + name_of_page + " | " + name_of_page + " in " + town2 + " | " + name_of_page + " " + zip1 + "</title>"
        keyword_generator = randint(0, len(get_number) - 1)
        if keyword_generator == 1:
            key_tag = "<meta name='keywords' content=" + "'" + name_of_page + " in " + town1 + ", " + town1 + " " + name_of_page + ", " + name_of_page + " in " + town2 + ", " + town2 + " " + name_of_page + ", " + zip1 + " " + name_of_page + ", " + name_of_page + " " + zip1 + "'>"
        elif keyword_generator == 2:
            key_tag = "<meta name='keywords' content=" + "'" + name_of_page + " in " + town2 + ", " + town2  + " " + name_of_page + ", " + town1 + " " + name_of_page + "," + name_of_page + " in " + town1 + ", " + name_of_page + " " + zip1 + ", " + zip1 + " " + name_of_page + "'>"
        else:
            key_tag = "<meta name='keywords' content=" + "'" + name_of_page + " in " + town1 + ", " + town2 + " " + name_of_page + ", " + name_of_page + " in " + town2 + ", " + town1 + " " + name_of_page + ", " + zip1 + " " + name_of_page + ", " + name_of_page + " " + zip1 +  "'>"
        desc_generator = randint(0, len(get_number) - 1)
        if desc_generator == 1:
            desc_tag = "<meta name='description' content=" + "'" + 'If you need a ' + occupation.lower() + ' appointment in ' + town2 + ', then call ' + name + ' today at ' + phone + ".'>"
        elif desc_generator == 2:
            desc_tag = "<meta name='description' content="  + "'" +'For the best' + occupation.lower() + ' in ' + town1 + ',call ' + phone + ' today for an appointment with ' + name + ".'>"
        else:
            desc_tag = "<meta name='description' content="  + "'" + 'Call ' + name + ' today at ' + phone + ' for an appointment with the best ' + occupation.lower() + ' in ' + town2 + ".'>"
        all_titles.append(title_tag)
        all_files.append(i)
        all_keywords.append(key_tag)
        all_descs.append(desc_tag)
        
title_dict = dict(zip(all_files, all_titles))
key_dict = dict(zip(all_files, all_keywords))
desc_dict = dict(zip(all_files, all_descs))        

for file in all_files:
    with open(file) as current_file:
        fw = open("xxx"+file, "w")
        for line in current_file:
            if "</head>" in line:
                for a in title_dict:
                    if a == file:
                        fw.write("\n" + title_dict[a] + "\n")
                for b in key_dict:
                    if b == file:
                        fw.write("\n" + key_dict[b] + "\n")
                for c in desc_dict:
                    if c == file:
                        fw.write("\n" + desc_dict[c] + "\n")
            fw.write(line.replace("<seo></seo>", " "))
        fw.close();   
        
for z in html_files:
    if "xxx" not in z:
        os.unlink(z)
        
for y in os.listdir(path):
    if y.startswith("xxx"):
        os.rename(y, y[3:])

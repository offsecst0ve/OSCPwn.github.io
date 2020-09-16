import os, re
 
basd_dir = 'C:\\Users\\Steve\\Documents\\GitHub\\OSCPwn.github.io\\Linux Boxes'
css_name = 'styles.css'
directory = os.listdir(basd_dir)
source_path = "C:\\Users\\Steve\\Documents\\GitHub\\OSCPwn.github.io\\Linux Boxes\\styles.css"
# 

with open(source_path, 'r') as file:
    data = file.read()
    print(data)

for dir_name in directory:
	dir_path = os.path.join(basd_dir, dir_name)
	if os.path.isdir(dir_path):
		path = os.path.join(dir_path, css_name)
		with open(path, 'w') as f:
			f.write(data)
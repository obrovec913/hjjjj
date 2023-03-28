import os
 
file_source = 'g\\'
file_destination = 'css\\'
file_destination2 = 'ing\\'
file_destination3 = 'js\\'
 
get_files = os.listdir(file_source)
print(get_files)
for g in get_files:
    if not g.endswith('.html'):
        file_sourc = os.listdir(file_source +g)
        for i in file_sourc:
            if i.endswith('.css'):
                os.replace(file_source + g+ f"\\{i}", file_destination + i)
            elif i.endswith('.png') or i.endswith('.jpg') :
                os.replace(file_source + g+ f"\\{i}", file_destination2 + i)
            elif i.endswith('.js'):
                os.replace(file_source + g+ f"\\{i}", file_destination3 + i)
            elif i.endswith('.Без названия'):
                l = i.split('.Без')
                print()
                os.rename(file_source + g+ f"\\{i}", file_source + l[0])
            else:
                os.replace(file_source + g + f"\\{i}", "g\\" + i)
        

     
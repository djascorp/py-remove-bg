import os

for root, dirs, files in os.walk('D:\\PROJETS\\LANGAGE\\React\\gasikara\\web-build'):
    for file in files:
        with open(os.path.join(root, file), "r") as auto:
            name = auto.name.split("D:\\PROJETS\\LANGAGE\\React\\gasikara\\web-build")
            # print(auto.name)
            file_name = name[len(name) - 1].replace('\\', '/')
            print("'" + file_name + "' ,")

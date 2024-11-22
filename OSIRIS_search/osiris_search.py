import os.path

dir_path = r'h:\data\67P\OSIRIS'
tifCounter = 0

for root_dir, cur_dir, files in os.walk(dir_path):
    for folder in cur_dir:
        if folder != 'JPG' and 'CALIB' and 'CATALOG' and 'DATA' and 'DOCUMENT' and 'EXTRAS' and 'INDEX':
            # print(folder)
            for file in files:
                if file.endswith('.JPG'):
                    tifCounter += 1
print('file count:', tifCounter)
import random
from concurrent.futures import ThreadPoolExecutor
try:
    filenames = ['file1.txt', 'file2.txt', 'file3.txt','file4.txt','file5.txt'] 
    for filename in filenames: 
        with open(filename, 'w') as file: 
            num = random.randint(1, 1000)
            file.write(str(num))
except:
    print("there is an issue with the file",e)
with ThreadPoolExecutor(max_workers=5) as executor:
    for result in executor.map(filenames):
        print(format(result))

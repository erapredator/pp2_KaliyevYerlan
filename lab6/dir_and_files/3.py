import os
print("Test a path exists or not:")
path = r'C:\erapp\pp2_KaliyevYerlan\lab6\dir_and_files\1.py'
print(os.path.exists(path))

print("File name of the path:")
print(os.path.basename(path))
print("Dir name of the path:")
print(os.path.dirname(path))
# File Handling in Python
# Reading a file or "ab+" mode
import pickle
f = open("demo.dat", "ab+")
pickle.dump("\nI am learning python", f)
print("Writing Done......")
f.seek(0)
a = f.read()
print(f'Content : {a}')
f.close()

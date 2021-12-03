import os
import sys

print(os.name)
print(os.getcwd())
new_path = os.path.join(os.getcwd(), 'new_dir')
# os.mkdir(new_path)

print('python entepreter:', sys.executable)
print('os info:', sys.platform)

# folder where modules are being searched
sys.path.append('C:\\Users\\prape\\Desktop')
for path in sys.path:
    print(path)
# import some_module_at_desktop

# name = sys.platform
# for i in range(1, 5):
#     os.mkdir(name + '_' + str(i))


print(sys.argv)
sys.exit()

paths =[]
import os
for dirpath, dirs, files in os.walk("."):
    paths.append(os.path.abspath(dirpath))
print(paths)
for path in paths:
    for a,b,c in os.walk(path):
        for item in c:
            if not item.endswith(".pem") or not item.endswith(".py"):
                print(os.path.join(a,item))
                os.remove(os.path.join(a,item))

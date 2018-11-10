import json

def install_and_import(package):
        import pip
        from pip._internal import main as pipmain
        pipmain(['install', package])
        import imp
        try:
            imp.find_module(package)
            found = True
        except ImportError:
            found = True
        finally:
            return found
        
with open('packages.json') as packages_json:
    import importlib.util
    import sys
    packages = json.load(packages_json)
    my_list = []
    for p in packages['Dependencies']:
        result = install_and_import((p['name']))
        my_list.append(result)
    indexes = [index for index in range(len(my_list)) if my_list[index] == False]
    print(len(indexes));
    if len(indexes) >= 0:
        print("Success")
    else:
        print("Failure")

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
            found = False
        finally:
            return found


with open('packages.json') as packages_json:
    import importlib.util
    import sys
    packages = json.load(packages_json)
    my_list = []
    for p in packages['Dependencies']:
        result = install_and_import((p['name']))
        my_list.append({"status":result,"package":p["name"]})

    
    newlist = [i for i in my_list if i["status"] == False]
    if len(newlist) > 0:
            print("------Failed Packages Are-------")
            for i in newlist:
                    print(i["package"])
    else:
            print("Success")
    

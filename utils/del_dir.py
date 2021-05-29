import os

def delete_recursive(path):
    if os.path.isfile(path):
        try:
            os.remove(path)
        except Exception as e:
            print(e)
    elif os.path.isdir(path):
        for item in os.listdir(path):
            itempath = os.path.join(path, item)
            delete_recursive(itempath)
        try:
            os.rmdir(path)
        except Exception as e:
            print(e)
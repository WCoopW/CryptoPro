import subprocess
import sys
from contextlib import redirect_stdout
import json
from model import Computer
import pydantic
import json


class MyClass:
    def __init__(self, Name, IP, License):
        self.Name = Name
        self.IP = IP
        self.License = License


LicenseKeyPath =[
    # для КриптоПро CSP 4.0:
    'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Installer\\UserData\\S-1-5-18\\Products\\7AB5E7046046FB044ACD63458B5F481C\\InstallProperties',
    # для КриптоПро CSP 5.0:
    'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Installer\\UserData\\S-1-5-18\\Products\\08F19F05793DC7340B8C2621D83E5BE5\\InstallProperties'
]


def get_key(computerName):
    setup_script = 'pwScript\CheckLicense.ps1'
    for path in LicenseKeyPath:
        key = subprocess.check_output([
        "powershell.exe",
        "-File",
        setup_script,
        computerName, path
        ],
        )
        try:
            ComputerLst = key.decode('utf-8')
            return ComputerLst
        except Exception:
            continue
    return False


# def search_pc():
#     ADName = ['DESKOT-FEF31', 'DESKOT-ARSF31', 'DESKOT-GJEF31','DESKOT-HDFHEF31','DESKOT-BFGEF31','DESKOT-AWF31']
#     Computers = []
#     for name in ADName:
#         instance = Computer(name, '', '')
#         Computers.append(instance)

#     for instance in Computers:
#         print(instance.name)

    # lines_list = ComputerLst.splitlines()
    # lines_list = list(filter(lambda x: x != "", lines_list))
    # print(ComputerObj.decode('utf-8'))
# Создание экземпляров классов

def search_pc():
    setup_script = 'pwScript\SearchPC.ps1'
    ComputerObj = subprocess.check_output([
        "powershell.exe",
        "-File",
        setup_script,
    ],
    )
    try:
        ComputerLst = json.loads(ComputerObj)
        return ComputerLst
    except Exception:
        return False
    # lines_list = ComputerLst.splitlines()
    # lines_list = list(filter(lambda x: x != "", lines_list))

    # Computers = []
    # for name in lines_list:
    #     instance = Computer(name, '', '')
    #     Computers.append(instance)
    # return Computers


def create_obj(ComputerLst):
    pcs = []
    i = 0
    for pc in ComputerLst:
        my_obj = MyClass(
            ComputerLst[i]["Name"], ComputerLst[i]['IPv4Address'], ComputerLst[i]['License'])
        pcs.append(my_obj)
        i += 1
    return pcs

def checked_all_pc(ComputerObj):
    for pc in ComputerObj:
        key =get_key(pc.Name)
        print(pc.Name)
        pc.License = key
    return ComputerObj


if __name__ == '__main__':
    
    ComputerLst = search_pc()
    ComputerObj = create_obj(ComputerLst)

    ComputerObj = checked_all_pc(ComputerObj)
    i = 0
    for per in ComputerObj:
        per = json.dumps(ComputerObj[i].__dict__)
        print(per)
        i +=1
   
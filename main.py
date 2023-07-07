import subprocess, sys
from contextlib import redirect_stdout
import json
from model import Computer
from pydantic import BaseModel
import json


class MyClass:
    def __init__(self, Name, IP, License):
        self.Name = Name
        self.IP = IP
        self.License = License

LicenseKey = [
#для КриптоПро CSP 3.6: 
'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Installer\\UserData\\S-1-5-18\Products\\05480A45343B0B0429E4860F13549069\\InstallProperties',
#для КриптоПро CSP 3.9:
'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Installer\\UserData\\S-1-5-18\\Products\\68A52D936E5ACF24C9F8FE4A1C830BC8\\InstallProperties',
#для КриптоПро CSP 4.0:
'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Installer\\UserData\\S-1-5-18\\Products\\7AB5E7046046FB044ACD63458B5F481C\\InstallProperties',
#для КриптоПро CSP 5.0:
'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Installer\\UserData\\S-1-5-18\\Products\\08F19F05793DC7340B8C2621D83E5BE5\\InstallProperties'
]



def getData():
  setup_script = 'pwScript\CheckLicense.ps1'
  path = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Installer\\UserData\\S-1-5-18\\Products\\08F19F05793DC7340B8C2621D83E5BE5\\InstallProperties\\'
  key = 'ProductID'
  computerName = "DESKTOP-NIAPJ6Q"
  p = subprocess.check_output([
              "powershell.exe", 
              "-File", 
              setup_script,
              computerName, path   
            ],
  )
  try:
    data = p.decode('utf-8')
    return data
  except Exception:
      return False
  
  
# def SearchPc():
#     ADName = ['DESKOT-FEF31', 'DESKOT-ARSF31', 'DESKOT-GJEF31','DESKOT-HDFHEF31','DESKOT-BFGEF31','DESKOT-AWF31']
#     Computers = []
#     for name in ADName:
#         instance = Computer(name, '', '')
#         Computers.append(instance)
    
#     for instance in Computers:
#         print(instance.name)
    
      
  #lines_list = data.splitlines()
  #lines_list = list(filter(lambda x: x != "", lines_list))
  #print(p.decode('utf-8'))
# Создание экземпляров классов

def SearchPc():
    setup_script = 'pwScript\SearchPC.ps1'
    p = subprocess.check_output([
            "powershell.exe", 
            "-File", 
            setup_script,
          ],
)

    data = json.loads(p)
    return data
    # lines_list = data.splitlines()
    # lines_list = list(filter(lambda x: x != "", lines_list))
    
    # Computers = []
    # for name in lines_list:
    #     instance = Computer(name, '', '')
    #     Computers.append(instance)
    # return Computers    


if __name__ == '__main__':
    k =getData()
    print(k)
    data = SearchPc()
    pcs = []
    i = 0
    for pc in data:
        my_obj = MyClass(data[i]["Name"], data[i]['IPv4Address'], data[i]['License'])
        pcs.append(my_obj)
        i+=1
        
    for p in pcs:
        print(p.Name)
    per = json.dumps(pcs[0].__dict__)
    print(per)
 
    
    
    
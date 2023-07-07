param($computerName, $path)
$remoteComputer = "DESKTOP-NIAPJ6Q"
$keyPath = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Installer\\UserData\\S-1-5-18\\Products\\08F19F05793DC7340B8C2621D83E5BE5\\InstallProperties\\"
# Установка соединения с удаленным компьютером 
$reg = [Microsoft.Win32.RegistryKey]::OpenRemoteBaseKey('LocalMachine', $remoteComputer)
# Получение подраздела реестра
$key = $reg.OpenSubKey($keyPath)
 # Получение значения ключа ProductID   
$data = $key.GetValue('ProductID')

Write-Output "$data"
# Закрытие соединения
$reg.Close()
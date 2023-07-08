param($computerName, $path)
$remoteComputer = $computerName
$keyPath = $path
# Установка соединения с удаленным компьютером 
$reg = [Microsoft.Win32.RegistryKey]::OpenRemoteBaseKey('LocalMachine', $remoteComputer)
# Получение подраздела реестра
$key = $reg.OpenSubKey($keyPath)
 # Получение значения ключа ProductID   
$data = $key.GetValue('ProductID')

Write-Output "$data"
# Закрытие соединения
$reg.Close()
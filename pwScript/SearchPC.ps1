Get-ADComputer -Filter * -Properties * | Select-Object Name, IPv4Address, License | ConvertTo-Json
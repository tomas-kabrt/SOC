$g = New-Graph -Type BidirectionalGraph

Get-WinEvent -path "C:\Users\tomas\Downloads\sysmon-master\folder\filtered_Sysmon.evtx" | ? {$_.id -eq 1} | Get-EventProps | ConvertTo-Json | Out-File -Encoding ASCII -FilePath my-sysmon-data.json

$events = Get-Content -Raw -Path .\my-sysmon-data.json | ConvertFrom-Json

$array = "2956", "3812", "3264", "6060", "4320", "1832", "2792", "5764", "3280", "3532", "2388", "2872", "2744", "5948", "4952", "6048", "1300", "5844", "5920", "4200", "3296", "6112", "4132", "1820", "780", "5628"

foreach ($event in $events) {
	
	if($event.ParentImage -eq "C:\Windows\System32\services.exe"){continue}
	if($event.ParentImage -eq "C:\Windows\System32\svchost.exe"){continue}
	if($event.ParentImage -eq "C:\Windows\System32\upfc.exe"){continue}
	if($event.ParentImage -like '*Defender*'){continue}
	if($event.ParentImage -like '*Defender*'){continue}
	if($event.Image -like '*conhost.exe*'){continue}
	
	if ($event.ProcessId.ToString() -in $array)
	{
		$name_s = "$($event.UtcTime) - $($event.CommandLine) - $($event.ProcessId.ToString())"
	}
	else{
		$name_s = "$($event.Image) - $($event.ProcessId.ToString())"
	}

	
	$name_g = "$($event.ParentImage) - $($event.ParentProcessId.ToString())"
	
	Add-Edge -From $name_g -To $name_s -Graph $g
	#Add-Edge -From $($event.ParentImage) - $($event.ParentProcessId) -To $event.Image -Graph $g

}

Show-GraphLayout -Graph $g
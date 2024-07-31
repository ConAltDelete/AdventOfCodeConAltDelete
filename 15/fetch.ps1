param(
	[int]$day = $null
)

if($day -eq 0){
	$current_path = Get-Location
	if([Int]::TryParse(@($current_path -Split "\\")[-1],[ref]$day)){
		Write-Host "Next time, just give a number..."
	} else {
		throw "Need a number!"
	}

}

$cookie = Get-Content ..\..\cookie
$path = Get-Location

curl --cookie session=$cookie https://adventofcode.com/2015/day/$day/input > $path/input

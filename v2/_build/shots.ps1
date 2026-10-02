param([string]$list)
$chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe"; $prof = "$env:TEMP\agi_headless_profile"; $out = "$env:TEMP\agi_shots"
New-Item -ItemType Directory -Force $out | Out-Null
foreach ($item in $list.Split(";")) {
  $name, $size, $url = $item.Split("|")
  Start-Process -FilePath $chrome -Wait -WindowStyle Hidden -ArgumentList @("--headless=new","--disable-gpu","--hide-scrollbars","--no-first-run","--user-data-dir=$prof","--window-size=$size","--virtual-time-budget=5000","--screenshot=$out\$name.png","http://127.0.0.1:8080/$url")
  "$name " + [math]::Round((Get-Item "$out\$name.png").Length/1KB) + " KB"
}

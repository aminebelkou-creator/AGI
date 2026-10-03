$ErrorActionPreference = "SilentlyContinue"
$out = "C:\Users\belko\AGI\data\crawl"; New-Item -ItemType Directory -Force $out | Out-Null
function Get-Urls($site) {
  $urls = New-Object System.Collections.Generic.HashSet[string]
  foreach ($idx in "wp-sitemap.xml", "sitemap_index.xml", "sitemap.xml") {
    try { $r = Invoke-WebRequest "$site/$idx" -UseBasicParsing -TimeoutSec 30 } catch { continue }
    $locs = [regex]::Matches($r.Content, "<loc>\s*([^<]+?)\s*</loc>") | ForEach-Object { $_.Groups[1].Value }
    foreach ($l in $locs) {
      if ($l -match "sitemap.*\.xml") {
        try { $s = Invoke-WebRequest $l -UseBasicParsing -TimeoutSec 30; [regex]::Matches($s.Content, "<loc>\s*([^<]+?)\s*</loc>") | ForEach-Object { [void]$urls.Add($_.Groups[1].Value) } } catch {}
      } else { [void]$urls.Add($l) }
    }
    if ($urls.Count -gt 0) { "$site : sitemap $idx"; break }
  }
  return $urls
}
foreach ($pair in @(@("agi", "https://www.americangroup-international.com"), @("anglia", "https://angliamorocco.org"))) {
  $u = Get-Urls $pair[1]
  $list = $u | Where-Object { $_ -notmatch "\.(jpe?g|png|webp|gif|pdf)$" } | Sort-Object
  $list | Set-Content "$out\$($pair[0])-urls.txt" -Encoding UTF8
  "$($pair[0]): $($list.Count) URLs"
  $list | Select-Object -First 60 | ForEach-Object { "   " + $_ }
}

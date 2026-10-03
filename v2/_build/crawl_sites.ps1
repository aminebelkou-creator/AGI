$ErrorActionPreference = "SilentlyContinue"
$base = "C:\Users\belko\AGI\data\crawl"
function Locs($content) { [regex]::Matches($content, "<loc>\s*(?:<!\[CDATA\[)?\s*([^<\]]+?)\s*(?:\]\]>)?\s*</loc>") | ForEach-Object { $_.Groups[1].Value } }
# 1) angliamorocco.org: all URLs from its sitemap index
$urls = New-Object System.Collections.Generic.HashSet[string]
$idx = Invoke-WebRequest "https://angliamorocco.org/wp-sitemap.xml" -UseBasicParsing -TimeoutSec 30
foreach ($sm in (Locs $idx.Content)) { try { $s = Invoke-WebRequest $sm -UseBasicParsing -TimeoutSec 30; Locs $s.Content | ForEach-Object { [void]$urls.Add($_) } } catch {} }
[void]$urls.Add("https://angliamorocco.org/")
$anglia = $urls | Where-Object { $_ -notmatch "\.(jpe?g|png|webp|gif|pdf|xml)$" } | Sort-Object
$anglia | Set-Content "$base\anglia-urls.txt" -Encoding UTF8
"angliamorocco.org: $($anglia.Count) URLs"
# 2) download pages (both sites)
function Save-All($list, $dir) {
  New-Item -ItemType Directory -Force $dir | Out-Null; $ok = 0
  foreach ($u in $list) {
    $name = ($u -replace "^https?://[^/]+/?", "" -replace "/$", "" -replace "[^A-Za-z0-9_-]+", "_"); if (-not $name) { $name = "_home" }
    try { $r = Invoke-WebRequest $u -UseBasicParsing -TimeoutSec 40; [IO.File]::WriteAllText("$dir\$name.html", "<!-- source: $u -->`n" + $r.Content, [Text.Encoding]::UTF8); $ok++ } catch { "  failed: $u" }
  }
  "saved $ok / $($list.Count) -> $dir"
}
Save-All $anglia "$base\anglia"
$agi = Get-Content "$base\agi-urls.txt" | Where-Object { $_ -match "^https" }
Save-All $agi "$base\agi"

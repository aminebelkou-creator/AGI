Add-Type -AssemblyName System.Drawing
$v2 = "C:\Users\belko\AGI\v2"; $src = "$v2\assets"; $dst = "$v2\assets\web"
New-Item -ItemType Directory -Force $dst | Out-Null
function Resize($in, $out, $max) {
  $img = [Drawing.Image]::FromFile($in)
  $r = [math]::Min(1.0, [math]::Min($max / $img.Width, $max / $img.Height))
  $w = [int]($img.Width * $r); $h = [int]($img.Height * $r)
  $bmp = New-Object Drawing.Bitmap $w, $h
  $g = [Drawing.Graphics]::FromImage($bmp); $g.InterpolationMode = 'HighQualityBicubic'; $g.SmoothingMode = 'HighQuality'; $g.PixelOffsetMode = 'HighQuality'
  $g.Clear([Drawing.Color]::Transparent); $g.DrawImage($img, 0, 0, $w, $h)
  if ($out -like "*.jpg") {
    $enc = [Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object MimeType -eq 'image/jpeg'
    $p = New-Object Drawing.Imaging.EncoderParameters 1; $p.Param[0] = New-Object Drawing.Imaging.EncoderParameter ([Drawing.Imaging.Encoder]::Quality), 82L
    $bmp.Save($out, $enc, $p)
  } else { $bmp.Save($out, [Drawing.Imaging.ImageFormat]::Png) }
  $g.Dispose(); $bmp.Dispose(); $img.Dispose()
}
Resize "$src\agi-seal.png" "$dst\agi-seal-520.png" 520
Resize "$src\director-julie-wilburn.jpg" "$dst\director-julie-wilburn.jpg" 720
Get-ChildItem $src -File -Include *.png, *.webp -Name | Out-Null
foreach ($f in Get-ChildItem $src -File | Where-Object { $_.Name -match '^(seal-.*-clean|mark-.*-clean|net-.*)\.png$' }) {
  Resize $f.FullName "$dst\$($f.Name)" 240
}
$before = (Get-ChildItem $src -File | Where-Object { $_.Name -match '^(seal-.*-clean|mark-.*-clean|net-.*|agi-seal|director-julie-wilburn)\.' } | Measure-Object Length -Sum).Sum
$after = (Get-ChildItem $dst -File | Measure-Object Length -Sum).Sum
"web images: " + (Get-ChildItem $dst -File).Count + "  size " + [math]::Round($before/1KB) + " KB -> " + [math]::Round($after/1KB) + " KB"

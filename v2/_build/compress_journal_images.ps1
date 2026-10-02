Add-Type -AssemblyName System.Drawing
$dir = "C:\Users\belko\AGI\v2\assets\journal"; $max = 1400
$jpg = [Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object MimeType -eq 'image/jpeg'
$before = (Get-ChildItem $dir -File | Measure-Object Length -Sum).Sum; $n = 0
foreach ($f in Get-ChildItem $dir -File | Where-Object { $_.Extension -match '^\.(jpe?g|png)$' -and $_.Length -gt 250KB }) {
  try {
    $img = [Drawing.Image]::FromFile($f.FullName)
    $r = [math]::Min(1.0, $max / [math]::Max($img.Width, $img.Height))
    $w = [int]($img.Width * $r); $h = [int]($img.Height * $r)
    $bmp = New-Object Drawing.Bitmap $w, $h; $g = [Drawing.Graphics]::FromImage($bmp)
    $g.InterpolationMode = 'HighQualityBicubic'; $g.SmoothingMode = 'HighQuality'; $g.DrawImage($img, 0, 0, $w, $h)
    $img.Dispose(); $tmp = "$($f.FullName).tmp"
    if ($f.Extension -match 'jpe?g') { $p = New-Object Drawing.Imaging.EncoderParameters 1; $p.Param[0] = New-Object Drawing.Imaging.EncoderParameter ([Drawing.Imaging.Encoder]::Quality), 80L; $bmp.Save($tmp, $jpg, $p) }
    else { $bmp.Save($tmp, [Drawing.Imaging.ImageFormat]::Png) }
    $g.Dispose(); $bmp.Dispose()
    if ((Get-Item $tmp).Length -lt $f.Length) { Move-Item $tmp $f.FullName -Force; $n++ } else { Remove-Item $tmp }
  } catch { "skip $($f.Name): $($_.Exception.Message)" }
}
$after = (Get-ChildItem $dir -File | Measure-Object Length -Sum).Sum
"compressed $n images: $([math]::Round($before/1MB,1)) MB -> $([math]::Round($after/1MB,1)) MB"

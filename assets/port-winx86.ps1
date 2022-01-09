Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
choco install -y curl 7zip.install
curl 'https://github.com/MangDL/MangDL/releases/download/2.0.2/mangdl-winx86.zip' -o mangdl.zip
Remove-Item -Force -Recurse C:\mangdl
tar -xf mangdl.zip
Remove-Item -Force mangdl.zip
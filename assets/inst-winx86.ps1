Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
choco install -y curl 7zip.install
curl 'https://github.com/MangDL/MangDL/releases/download/3.1.0.0/mangdl-winx86.zip' -o mangdl.zip
$FolderName = 'C:\mangdl\'
if (Test-Path $FolderName) {
    Remove-Item -Force -Recurse $FolderName
    "Set-Alias -Name mangdl -Value C:\mangdl\mangdl.bat" >> $PROFILE.CurrentUserAllHosts
    . $PROFILE.CurrentUserAllHosts
}
tar -xf mangdl.zip -C C:\
Remove-Item -Force mangdl.zip
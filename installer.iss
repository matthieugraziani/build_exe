[Setup]
AppName=Mon Application
AppVersion=1.0
DefaultDirName={pf}\MonApplication
DefaultGroupName=Mon Application
OutputDir=dist_installer
OutputBaseFilename=MonApplicationSetup
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\MonApp.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Mon Application"; Filename: "{app}\MonApp.exe"

[Run]
Filename: "{app}\MonApp.exe"; Flags: nowait postinstall skipifsilent

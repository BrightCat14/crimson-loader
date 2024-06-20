[Setup]
AppName=Crimson-Loader
AppVersion=1.0
DefaultDirName={userappdata}\crimson-loader
DefaultGroupName=Crimson
OutputBaseFilename=CrimsonSetup
Compression=lzma
SolidCompression=yes

[Files]
Source: "C:\Users\geoky\Documents\python\output\crimson loader.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Crimson"; Filename: "{app}\crimson loader.exe"

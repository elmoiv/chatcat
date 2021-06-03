version_file = '''
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers={1},
    prodvers={1},
    mask=0x3f,
    flags=0x0,
    OS=0x4,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'elmoiv Apps'),
        StringStruct(u'FileDescription', u'{2}'),
        StringStruct(u'FileVersion', u'{0}'),
        StringStruct(u'InternalName', u'{2}'),
        StringStruct(u'LegalCopyright', u'Khaled El-Morshedy (elmoiv) 2015-2021'),
        StringStruct(u'OriginalFilename', u'{2}.exe'),
        StringStruct(u'ProductName', u'{2}'),
        StringStruct(u'ProductVersion', u'{0}')])
      ]), 
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
'''

sepc_file = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['{0}src\\\\{5}.py'],
             pathex=['{0}{5}'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes={3},
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

excluded_binaries = {1}

a.binaries = TOC([x for x in a.binaries if x[0] not in excluded_binaries])

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='{5}',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console={4} , version='tmp.txt', icon='{0}exe\\\\icon.ico')

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude={2},
               name='{5}')'''

iss_file = '''#define MyAppName "{3}"
#define MyAppVersion "{1}"
#define MyAppPublisher "elmoiv"
#define MyAppURL "https://elmoiv.github.io/"
#define MyAppExeName "{3}.exe"

[Setup]
AppId={{{{{4}}}
AppName={{#MyAppName}}
AppVersion={1}
VersionInfoVersion={2}
AppPublisher={{#MyAppPublisher}}
AppPublisherURL={{#MyAppURL}}
AppSupportURL={{#MyAppURL}}
AppUpdatesURL={{#MyAppURL}}
DefaultDirName={{autopf}}\\{{#MyAppName}}
DisableDirPage=yes
DisableProgramGroupPage=yes
UsedUserAreasWarning=no
PrivilegesRequiredOverridesAllowed=dialog
OutputBaseFilename={3} {1} x64
UninstallDisplayIcon={{app}}\\{3}.exe
WizardSmallImageFile={0}exe\\setup_img.bmp
SolidCompression=yes
Compression=lzma2/ultra64
LZMAUseSeparateProcess=yes
LZMADictionarySize=1048576
LZMANumFastBytes=273
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{{cm:CreateDesktopIcon}}"; GroupDescription: "{{cm:AdditionalIcons}}"
Name: "quicklaunchicon"; Description: "{{cm:CreateQuickLaunchIcon}}"; GroupDescription: "{{cm:AdditionalIcons}}"; Flags: unchecked; OnlyBelowVersion: 6.1; Check: not IsAdminInstallMode

[Files]
Source: "{0}output\\{3}\\{3}.exe"; DestDir: "{{app}}"; Flags: ignoreversion
Source: "{0}output\\{3}\\_socket.pyd"; DestDir: "{{app}}"; Flags: ignoreversion
Source: "{0}output\\{3}\\base_library.zip"; DestDir: "{{app}}"; Flags: ignoreversion
Source: "{0}output\\{3}\\{3}.exe.manifest"; DestDir: "{{app}}"; Flags: ignoreversion
Source: "{0}output\\{3}\\msvcp140.dll"; DestDir: "{{app}}"; Flags: ignoreversion
Source: "{0}output\\{3}\\python37.dll"; DestDir: "{{app}}"; Flags: ignoreversion
Source: "{0}output\\{3}\\Qt5Core.dll"; DestDir: "{{app}}"; Flags: ignoreversion
Source: "{0}output\\{3}\\Qt5Gui.dll"; DestDir: "{{app}}"; Flags: ignoreversion
Source: "{0}output\\{3}\\Qt5Widgets.dll"; DestDir: "{{app}}"; Flags: ignoreversion
Source: "{0}output\\{3}\\select.pyd"; DestDir: "{{app}}"; Flags: ignoreversion
Source: "{0}output\\{3}\\unicodedata.pyd"; DestDir: "{{app}}"; Flags: ignoreversion
Source: "{0}output\\{3}\\VCRUNTIME140.dll"; DestDir: "{{app}}"; Flags: ignoreversion
Source: "{0}output\\{3}\\PyQt5\\*"; DestDir: "{{app}}\\PyQt5"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{0}output\\{3}\\include\\*"; DestDir: "{{app}}\\include"; Flags: ignoreversion
Source: "{0}output\\{3}\\simpleaudio\\*"; DestDir: "{{app}}\\simpleaudio"; Flags: ignoreversion

[Icons]
Name: "{{autoprograms}}\\{{#MyAppName}}"; Filename: "{{app}}\\{{#MyAppExeName}}"
Name: "{{autodesktop}}\\{{#MyAppName}}"; Filename: "{{app}}\\{{#MyAppExeName}}"; Tasks: desktopicon
Name: "{{userappdata}}\\Microsoft\\Internet Explorer\\Quick Launch\\{{#MyAppName}}"; Filename: "{{app}}\\{{#MyAppExeName}}"; Tasks: quicklaunchicon

[Run]
Filename: "{{app}}\\{{#MyAppExeName}}"; Description: "{{cm:LaunchProgram,{{#StringChange(MyAppName, '&', '&&')}}}}"; Flags: nowait postinstall skipifsilent'''

excluded_binaries = ['api-ms-win-core-console-l1-1-0.dll', 'api-ms-win-core-datetime-l1-1-0.dll', 'api-ms-win-core-debug-l1-1-0.dll', 'api-ms-win-core-errorhandling-l1-1-0.dll', 'api-ms-win-core-file-l1-1-0.dll', 'api-ms-win-core-file-l1-2-0.dll', 'api-ms-win-core-file-l2-1-0.dll', 'api-ms-win-core-handle-l1-1-0.dll', 'api-ms-win-core-heap-l1-1-0.dll', 'api-ms-win-core-interlocked-l1-1-0.dll', 'api-ms-win-core-libraryloader-l1-1-0.dll', 'api-ms-win-core-localization-l1-2-0.dll', 'api-ms-win-core-memory-l1-1-0.dll', 'api-ms-win-core-namedpipe-l1-1-0.dll', 'api-ms-win-core-processenvironment-l1-1-0.dll', 'api-ms-win-core-processthreads-l1-1-0.dll', 'api-ms-win-core-processthreads-l1-1-1.dll', 'api-ms-win-core-profile-l1-1-0.dll', 'api-ms-win-core-rtlsupport-l1-1-0.dll', 'api-ms-win-core-string-l1-1-0.dll', 'api-ms-win-core-synch-l1-1-0.dll', 'api-ms-win-core-synch-l1-2-0.dll', 'api-ms-win-core-sysinfo-l1-1-0.dll', 'api-ms-win-core-timezone-l1-1-0.dll', 'api-ms-win-core-util-l1-1-0.dll', 'api-ms-win-crt-conio-l1-1-0.dll', 'api-ms-win-crt-convert-l1-1-0.dll', 'api-ms-win-crt-environment-l1-1-0.dll', 'api-ms-win-crt-filesystem-l1-1-0.dll', 'api-ms-win-crt-heap-l1-1-0.dll', 'api-ms-win-crt-locale-l1-1-0.dll', 'api-ms-win-crt-math-l1-1-0.dll', 'api-ms-win-crt-multibyte-l1-1-0.dll', 'api-ms-win-crt-process-l1-1-0.dll', 'api-ms-win-crt-runtime-l1-1-0.dll', 'api-ms-win-crt-stdio-l1-1-0.dll', 'api-ms-win-crt-string-l1-1-0.dll', 'api-ms-win-crt-time-l1-1-0.dll', 'api-ms-win-crt-utility-l1-1-0.dll', 'd3dcompiler_47.dll', 'libEGL.dll', 'libGLESv2.dll', 'opengl32sw.dll', 'Qt5DBus.dll', 'Qt5Qml.dll', 'Qt5Quick.dll', 'Qt5Svg.dll', 'Qt5WebSockets.dll', 'ucrtbase.dll', 'VCRUNTIME140_1.dll', 'Qt5QmlModels.dll', 'MSVCP140_1.dll', 'libcrypto-1_1.dll', 'libssl-1_1.dll', 'libcrypto-1_1-x64.dll', 'libssl-1_1-x64.dll', 'libeay32.dll', 'ssleay32.dll', 'Qt5Network.dll']

excluded_upx = ['qwindows.dll', 'qsvgicon.dll', 'qxdgdesktopportal.dll', 'qwindowsvistastyle.dll']

excluded_modules = ['tk', 'tcl', '_tkinter', 'tkinter', 'Tkinter', 'FixTk', 'PIL', 'tk', 'tcl', '_tkinter', 'tkinter', 'Tkinter', 'FixTk', 'matplotlib', 'IPython', 'scipy', 'eel', 'jedi', 'win32com', 'numpy', 'wcwidth', 'win32wnet', '_asyncio', '_bz2', '_decimal', '_hashlib', '_lzma', '_multiprocessing', '_overlapped', '_win32sysloader', '_cffi_backend', '_openssl', 'cryptography', '_ssl', 'pyexpat']

is_gui = not bool(input('Press Enter for GUI, or anything for Console: '))
app_name = 'ChatCat'
app_guid = '567E206F-ADF2-460D-8412-E013F6AA97A3'
version = '1.0.0'

import os, shutil, time, re

# Auto update version in main.py
src_main = open('src\\main.py').read()
new_main = re.sub(
              r"self.version = '(\d+\.\d+\.\d+)'",
              f"self.version = '{version}'",
              src_main
          )
open('src\\main.py', 'w').write(new_main)

def version_format(s):
    # Convert xx.xx.xx.xx -> (xx, xx, xx, xx)
    e = [0, 0, 0, 0]
    for n, i in enumerate(s.split('.')):
            e[n] = int(i)
    return tuple(e)

CUR_DIR = os.path.dirname(__file__)

if CUR_DIR:
    os.chdir(CUR_DIR)
    CUR_DIR += '\\'

# Execute Pyinstaller
version_file = version_file.format(
    version,
    version_format(version),
    app_name
)

sepc_file = sepc_file.format(
    CUR_DIR.replace('\\', '\\\\'),
    excluded_binaries,
    excluded_upx,
    excluded_modules,
    not is_gui,
    app_name
)

iss_file = iss_file.format(
    CUR_DIR,
    version,
    '.'.join(map(str, version_format(version))),
    app_name,
    app_guid
)

open('tmp.txt', 'w').write(version_file)
open('tmp.spec', 'w').write(sepc_file)
open('tmp.iss', 'w').write(iss_file)

start = time.time()

print('>>> [PyInstaller] Converting project to exe')
os.system('pyinstaller tmp.spec --log-level "ERROR" --noconfirm')

app_path = 'output\\ChatCat\\'
platforms_dlls = app_path + 'PyQt5\\Qt\\plugins\\platforms\\'

## Remove previous builds
if os.path.exists(app_path):
    shutil.rmtree(app_path)

os.makedirs('output', exist_ok=True)
os.rename('dist\\' + app_name, app_path)

# UPX with Executable
os.system(f'upx {app_path}ChatCat.exe')

print('>>> Removing unnecessary files')
## Remove all platforms dll but qwindows.dll
for dll in os.listdir(platforms_dlls):
    if not 'qwindows.dll' in dll:
        os.remove(platforms_dlls + dll)

## Remove un needed folders
for rm in [
  'dist',
  'build', 
  app_path + 'PyQt5\\Qt\\translations',
  app_path + 'PyQt5\\Qt\\plugins\\imageformats',
  app_path + 'PyQt5\\Qt\\plugins\\iconengines']:
    shutil.rmtree(rm)

print('>>> [Inno Setup] Packaging exe inised Setup file')

# Compile ISS inno setup script
_ = os.popen('iscc tmp.iss').read()

os.remove('tmp.txt')
os.remove('tmp.spec')
os.remove('tmp.iss')

end = time.time()

print('>>> Finished in', int(end - start), 'seconds')
input('\nSee your files at "output\\"')
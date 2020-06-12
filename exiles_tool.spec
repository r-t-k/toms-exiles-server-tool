# -*- mode: python ; coding: utf-8 -*-
import platform

block_cipher = None

added_files = [
         ( '/Users/tommykyser/Projects/python/exile-tool/toms-exiles-server-tool/resources/chromedriver_83', '.' ),
         ( '/Users/tommykyser/Projects/python/exile-tool/toms-exiles-server-tool/resources/chromedriver_83_win.exe', '.' )
         ]

a = Analysis(['main.py'],
             pathex=['/Users/tommykyser/Projects/python/exile-tool/toms-exiles-server-tool'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='exiles_tool',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
if platform.system() == 'Darwin':
    info_plist = {'addition_prop': 'additional_value'}
    app = BUNDLE(exe,
                 name='exiles_tool.app',
                 bundle_identifier=None,
                 info_plist=info_plist
                )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='exiles_tool')



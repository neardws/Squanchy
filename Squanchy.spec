# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Squanchy.py','D:\\singl\\Documents\\Squanchy\\hide_screen.py','D:\\singl\\Documents\\Squanchy\\ico.py','D:\\singl\\Documents\\Squanchy\\readme.py'],
             pathex=['D:\\singl\\Documents\\Squanchy'],
             binaries=[],
             datas=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Squanchy',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='favicon.ico')

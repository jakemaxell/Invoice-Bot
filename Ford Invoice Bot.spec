# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['C:/Users/jacob.maxwell/Programs/Projects/Current Projects/FordInvoiceProject/main.py'],
             pathex=['C:\\Users\\jacob.maxwell\\Programs\\Projects\\Current Projects\\FordInvoiceProject'],
             binaries=[('C:/Users/jacob.maxwell/Programs/Projects/Current Projects/FordInvoiceProject/chromedriver.exe', '.')],
             datas=[('C:/Users/jacob.maxwell/Programs/Projects/Current Projects/FordInvoiceProject', 'FordInvoiceProject/')],
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
          name='Ford Invoice Bot',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='C:\\Users\\jacob.maxwell\\Programs\\Projects\\Current Projects\\FordInvoiceProject\\icon.ico')

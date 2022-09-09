# Youtube Downloader 

Download Youtube Video And Mp3 With Python.

## Usage

### Install Module

```python
  pip install pytube
  pip install colorama
```
### Run Tool

```python
  python main.py
```

### Convert To EXE

- Use Script In File Organizer EXE Folder
```python
  # Using Pyinstaller
  Pyinstaller --noconfirm --onefile main.py

  # Using Nuitka
  py -m nuitka --mingw64 .\main.py --standalone --onefile 
 ```


## Change Output Directory

- Change your downloaded video directory on line 9
- Change your downloaded Mp3 directory on line 18



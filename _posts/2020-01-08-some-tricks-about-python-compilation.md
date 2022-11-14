---
title: EN - Some tricks about python compilation
published: true
---

> This article might help you to learn some useful tricks about python compilation.
> You can train using the code and files given in this article.

# Some information about the ressource path inside executable

After compiling your python code, you need to know where the files added and used by the executable are located. \\
While developing, `_MEIPASS` attribute from `sys` does not exists, so `getattr(sys, '_MEIPASS', os.path.abspath('.'))` returns `os.path.abspath('.')` \\
You will be able to use it only after PyInstaller compilation.

Here is the source code: <a href="/images/posts/PythonCompilation/source_code_ressource_path.py">source_code_ressource_path.py</a>

<img src="/images/posts/PythonCompilation/demo1.png">

After compiling...

<img src="/images/posts/PythonCompilation/demo2.png">

Let's imagine you have copied the folder `images` inside the executable, you can access this folder inside the temp folder `AppData\Local\Temp\_MEI...`

<img src="/images/posts/PythonCompilation/cmd9.png">

# Context

Let's build a simple app that is going to show a random image within a pool of images, i took 3 car images inside an executable: <a href="/images/posts/PythonCompilation/demo.exe">demo.exe</a>

## Prerequisite

```bash
pip install pillow
```

## Code

Here is the source code: <a href="/images/posts/PythonCompilation/source_code.py">source_code.py</a>

<img src="/images/posts/PythonCompilation/pycharmproject.png">

## Compilation

After installing `PyInstaller`, you need to find where `pyinstaller.exe` is located

Example:
```
pip install PyInstaller
C:\Users\Aurelien\PycharmProjects\PythonCompilation\venv\Scripts\pyinstaller.exe -n RandomCar --onefile --no-console --clean --add-data images;images main.py
```

The options used are:
- `--onefile`: Create a one-file bundled executable
- `--no-console`: Do not provide a console window for standard i/o
- `--clean`: Clean PyInstaller cache and remove temporary files before building.
- `-n <name>`: Name to assign to the bundled app and spec file
- `--add-data <SRC;DEST or SRC:DEST>`: Additional non-binary files or folders to be added to the executable. The path separator is platform specific, os.pathsep (which is ; on Windows and : on most unix systems) is used. This option can be used multiple times.

The folder `images` is copyed inside the executable file `RandomCar.exe` \\
You can find your executable file inside the folder `dist` created by PyInstaller

<img src="/images/posts/PythonCompilation/cmd6.png">

## Result 

<img src="/images/posts/PythonCompilation/cmd8.png">

The random car is displayed.

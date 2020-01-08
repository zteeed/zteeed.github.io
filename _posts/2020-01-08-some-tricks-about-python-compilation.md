---
title: Some tricks about python compilation
published: true
---

> This article might help you to learn some usefull tricks about python compilation.
> You can train using the code and files given in this article.

# Some information about the ressource path inside executable

After compiling your python code, you need to know where the files added and used by the executable are located.

Here is the source code: <a href="/images/posts/PythonCompilation/source_code_ressource_path.py">source_code_ressource_path.py</a>

While developing, `_MEIPASS` attribute from `sys` does not exists, so `getattr(sys, '_MEIPASS', os.path.abspath('.'))` return `os.path.abspath('.')` \\
You will be able to use it only after PyInstaller compilation.

<img src="/images/posts/PythonCompilation/demo1.png">

<img src="/images/posts/PythonCompilation/demo2.png">

Let's imagine you have copyed the folder `images` inside the executable, you can access to this folder inside the temp folder `AppData\Local\Temp\_MEI...`

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

After install `PyInstaller`, you need to find where `pyinstaller.exe` is located

Example:
```
pip install PyInstaller
C:\Users\Aurelien\PycharmProjects\PythonCompilation\venv\Scripts\pyinstaller.exe -n RandomCar --onefile --no-console --clean -F --add-data images;images main.py
```

The folder `images` is copyed inside the executable file `RandomCar.exe` \\
You can find your executable file inside the folder `dist` created by PyInstaller

<img src="/images/posts/PythonCompilation/cmd6.png">

## Result 

<img src="/images/posts/PythonCompilation/cmd8.png">

The random car is displayed.

Mac 和 Windows 局域网剪贴板共享
===============

工作中，经常同时使用Windows PC和一台Mac，使用一套键盘，用Synergy 共享键盘鼠标，但Synergy的剪贴板共享一直有Bug,遂用写了以下脚本,脚本同以同步两边的文本信息的剪贴板内容。


### How to use

1. Install python 3
2. Install [pyperclip](https://github.com/asweigart/pyperclip) 
3. Run python CloudClip.py on Windows and Mac
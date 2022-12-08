import pathlib

path1 = pathlib.Path("C:/images/whatsapp/hello.txt")
print(path1.is_absolute())
path2 = pathlib.Path.cwd()
print(path2)
path3 = path2 / "private.jpg"
print(path3)

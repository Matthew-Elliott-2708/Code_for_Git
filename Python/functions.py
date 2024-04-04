def function():
    print("Hello world from a function!")

responce = input("do you want to be welcomed from a function?: ")
if responce.capitalize() == "Y":
    function()
else:
    print("alrigfht ill say it outside of a function, Hello world!")
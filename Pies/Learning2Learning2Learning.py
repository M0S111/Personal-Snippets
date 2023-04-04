def a():
    print("a() called")
    b()
    print("Returning a() now")

def b():
    print("b() called")
    c()
    print("Returning b() now")

def c():
    print("c() called")
    print("Returning c() now")


a()

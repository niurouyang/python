def hello():
    print("Hello from script1.py!")

print("Script1's __name__:", __name__)

if __name__ == '__main__':
    print("Script1 is being executed as the main program.")
    hello()

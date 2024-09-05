def hello() -> str:
    with open("./secret.txt", "r") as f:
        print(f"[[[[{f.read()}]]]] as a secret message.");
    return "Hello from rve!"

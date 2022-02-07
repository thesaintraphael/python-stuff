import typer

app = typer.Typer()


@app.command()
def hello(name: str, age: int, display_age: bool = True):
    print(f"Hello, {name}")
    if display_age:
        print(f"Your age is {age}")


@app.command()
def goodbye():
    print("goodbye")


if __name__ == "__main__":
    app()

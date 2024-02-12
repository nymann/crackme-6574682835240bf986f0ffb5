import typer

app = typer.Typer()


@app.command()
def keygen() -> None:
    typer.echo("Implement your keygen for crackme_6574682835240bf986f0ffb5 here.")


if __name__ == "__main__":
    app()

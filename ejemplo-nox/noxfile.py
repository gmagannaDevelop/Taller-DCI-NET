import nox


@nox.session
def formatting(session):
    """Esta función crea un entorno virtual donde instala `black` para
    formatear el código de Python a un estándar (PEP 8)
    """
    session.install("black")
    session.run("black", "ejemplo.py")


@nox.session
def types(session):
    """Esta función decorada permite crear un entorno virtual y luego
    instalar `mypy` que permite analizar el tipado del código para
    capturar errores de tipo.
    """
    session.install("mypy")
    session.run("mypy", "--ignore-missing-imports", "ejemplo.py")


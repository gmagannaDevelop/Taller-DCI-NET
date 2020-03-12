
import decoradores

@decoradores.email_log("Prueba")
def suma(a, b):
    return a + b

if __name__ == "__main__":
    print(f"Una suma correcta {4}+{5} = {suma(4, 5)}")
    suma(4)


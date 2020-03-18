
import decoradores

@decoradores.log_exception_to_mail("Hola")
def suma(a, b):
    return a + b


"""
@decorador
def mi_funcion()
    ....


mi_funcion =  decorador(mi_funcion)


"""



if __name__ == "__main__":
    print(f"Una suma correcta {4}+{5} = {suma(4, 5)}")
    suma(4, "hola")
    print(f"Otra suma correcta {4}+{5} = {suma(4, 5)}")


class CuentaBancaria:
    def __init__(self, saldo):
        # El atributo saldo es privado porque su nombre comienza con dos guiones bajos
        self.__saldo = saldo

    def depositar(self, monto):
        # Podemos acceder al atributo privado saldo desde dentro de la clase
        self.__saldo += monto

    def retirar(self, monto):
        # Podemos acceder al atributo privado saldo desde dentro de la clase
        if monto > self.__saldo:
            print("Fondos insuficientes")
        else:
            self.__saldo -= monto

    def consultar_saldo(self):
        # Podemos acceder al atributo privado saldo desde dentro de la clase
        return self.__saldo


# Creamos un objeto de la clase CuentaBancaria
cuenta1 = CuentaBancaria(1000)
# Intentamos acceder al atributo privado saldo desde fuera de la clase
# Esto produce un error porque el atributo saldo es privado
print(cuenta1.__saldo)

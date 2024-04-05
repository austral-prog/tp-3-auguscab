def check_vowels():
    # Código a implementar utilizando input.
    nombre= input("Ingrese su nombre: ")
    a= "a" in nombre.lower()
    e= "e" in nombre.lower()
    i= "i" in nombre.lower()
    o= "o" in nombre.lower()
    u= "u" in nombre.lower()
    print("contiene a: " + str(a))
    print("contiene e: " + str(e))
    print("contiene i: " + str(i))
    print("contiene o: " + str(o))
    print("contiene u: " + str(u))


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`

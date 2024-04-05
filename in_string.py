def check_vowels():
    # Código a implementar utilizando input.
    nombre= input("Ingrese su nombre: ")
    print(f"contiene a: {"a" in nombre.lower()}")
    print(f"contiene e: {"e" in nombre.lower()}")
    print(f"contiene i: {"i" in nombre.lower()}")
    print(f"contiene o: {"o" in nombre.lower()}")
    print(f"contiene u: {"u" in nombre.lower()}")


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`

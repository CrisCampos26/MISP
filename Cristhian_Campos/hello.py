import hashlib

# Mensaje original
mensaje = "Hola Mundo"

# Cifrar con SHA-256
hash_obj = hashlib.sha256(mensaje.encode())
hash_cifrado = hash_obj.hexdigest()

# Imprimir el mensaje cifrado
print("Mensaje cifrado en SHA-256:", hash_cifrado)

from time import sleep

def is_prime(number):
    factors = []
    for i in range(2, int(number**0.5)+1):
        if (number/i)%1 == 0:
            factors.append(i)
            
    if len(factors) > 0:
        return False
    else:
        return True

def calculate_generator(prime):
    if is_prime(prime) == False:
        return False

    generators = []
  
    for i in range(2, prime):
        results = []
        for j in range(2, prime):
            results.append(pow(i, j, prime))

        if len(set(results)) == len(results):
            generators.append(i)

    return generators


def create_pub_key(generator, private_key, prime):
    return pow(generator, private_key, prime)

def encode_string(string):
    char_array = []
    for char in string:
        char_array.append(ord(char))
    return char_array

def encrypt_message(super_key, message_array, prime):
    encrypted_array = []
    for num in message_array:
        encrypted_array.append(num + super_key % prime)
    return encrypted_array

def decrypt_message(super_key, encrypted_array, prime):
    decrypted_message = []
    for num in encrypted_array:
        decrypted_message.append(num - super_key % prime)
    return decrypted_message


def dh():
    p1 = input("Person 1's name: ")
    p2 = input("Person 2's name: ")

    prime = int(input("choose a shared prime number: "))

    while is_prime(prime) == False:
        prime = int(input("that's not prime, try again: "))

    gen = int(input(f"select a shared generator from the list {calculate_generator(prime)}: "))

    p1private_key = int(input(f"{p1} select a private key: "))
    p1public_key = create_pub_key(gen, p1private_key, prime)

    p2private_key = int(input(f"{p2} select a private key: "))
    p2public_key = create_pub_key(gen, p2private_key, prime)

    print("calculating public keys: a**(private_key) % p \n")
    
    sleep(2)

    print(f"{p1}'s private key: {p1private_key}, public key: {p1public_key}")
    print(f"{p2}'s private key: {p2private_key}, public key: {p2public_key}")
    input(f"Your shared numbers are p: {prime}, a: {gen}")

    print("calculating super key")

    sleep(2)

    super_key1 = pow(p2public_key, p1private_key, prime)
    super_key2 = pow(p1public_key, p2private_key, prime)
    
    if super_key1 != super_key2:
        print("Oops, something went wrong...")

    print(f"super key is {super_key1}")

    message = input(f"{p1}, what message do you want to send to {p2}? ")
    
    message_array = encode_string(message)
    print(message_array)

    print("now encrypting message (each letter individually)")

    encrypted = encrypt_message(super_key1, message_array, prime)
    print(encrypted)
    

def key_generator(size:int):

    # import required libraries
    from math_functions import prime_finder
    try:
        from math import gcd
    except:
        from math_functions import gcd

    print("-------------RSA Key Generator Powered by Davood-------------")
    print()
    print("Initializing...")
    # generate basic parameters
    p = prime_finder(size)
    print("Parameter p generated successfully.")
    q = prime_finder(size)
    print("Parameter q generated successfully.")    
    n = p * q
    print("Parameter n initalized successfully.")    
    phi = (p-1) * (q-1)
    print("Parameter phi initalized successfully.") 

    # generate possible public keys
    print("Generating list of possible public keys...")
    public_keys = []
    for i in range(phi -1 , 3 , -1):
        if gcd(i, phi) == 1 and gcd(i, n) == 1:
            public_keys.append(i)
        if len(public_keys) == 1_000_000:
            break
    print(f"List of possible public keys generated successfully.")

    # choose a public key    
    from random import choice
    e = choice(public_keys)
    from math import log2
    print(f"Public key selected successfully, size = {int(log2(e)) + 1} bits.")
    del public_keys

    # generate possible private keys
    print("Generating list of possible privaye keys...")
    private_keys = []
    i = 2
    while len(private_keys) <= 4:
        if i * e % phi == 1:
            private_keys.append(i)
        i += 1
    print(f"List of possible private keys generated successfully.")

    # choose a private key    
    d = choice(private_keys)
    print(f"Private key selected successfully, size = {int(log2(d)) + 1} bits.")
    print("Finishing...") 
    print()
    print("-------------Key generation completed successfully-------------")
    return e , d
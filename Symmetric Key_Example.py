import random
# Cryptography: Symmetric Key, ROT CONCEPT!

ORDER_ = ["a", "u", "w", "x", "e", "g", "f", "h", "i", "j", "k", "z", "s", "n", "o", "y", "q", "r", "t", "m",
          "b", "v", "c", "d", "p", "l"]

def Encryption_2():
    global encrypted_message
    encrypted_message = ""

    Symmetric_Key = random.randrange(9999, 9999999, 1)
    print("Symmetric Key:", Symmetric_Key)

    while (Symmetric_Key > 26):
        Symmetric_Key = Symmetric_Key // 2
        Symmetric_Key2 = Symmetric_Key

    plain_text = input("Enter the plaintext: ")

    for x in plain_text:
        n = ord(x)
        algorithm = (int(n) + Symmetric_Key2) // 10
        algorithm2 = (int(n) + Symmetric_Key2) / 10
        algorithm3 = str(algorithm2)

        counter = 0

        for x in str(algorithm3):
            counter = counter + 1
            if (x == '.'):
                global z
                z = str(algorithm3[counter:])

                if (int(z) > 0):
                    global z_counter
                    z_counter = z
                    encrypted_message = encrypted_message + '|'
                    encrypted_message = encrypted_message + ORDER_[int(algorithm)]
                    encrypted_message = encrypted_message + '.'
                    encrypted_message = encrypted_message + chr(33 + int(z_counter))
                    encrypted_message = encrypted_message + '|'

                else:
                    encrypted_message = encrypted_message + ORDER_[int(algorithm)]

    print('EncryptedMessage| CipherText:', encrypted_message)

def Decryption_2():
    global Decrypted_Text
    Decrypted_Text = []
    Symmteric_Key = 0
    try:
        Symmetric_Key = int(input("Enter the valid Symmetric KEY: "))
    except ValueError:
        print('Please enter a valid key!')
        Decryption_2()

    while (Symmetric_Key > 26):
        Symmetric_Key = Symmetric_Key // 2
        Symmetric_Key2 = Symmetric_Key

    ciphertext = input('Please enter the cipher text: ')

    counter = 0

    INDEX_OF_STRING_ = []
    INDEX_OF_STRING_2 = []
    temp_string = []
    STRING_TO_CHANGE = []

    for x in ciphertext:
        counter = counter + 1  # Every step of the counter.

        if (x == "|"):
            INDEX_OF_STRING_.append(counter)

    for x in range(len(INDEX_OF_STRING_)):
        try:
            temp_string.append(ciphertext[INDEX_OF_STRING_[x]:INDEX_OF_STRING_[x + 1]].replace('|', ''))

        except IndexError:
            break

    # Analyzing the temp_string_list

    for x in range(0, len(temp_string)):
        temp_string_2 = temp_string[x]

        if (len(temp_string_2) > 1):
            convert1 = temp_string_2[0] # Value before the .
            convert2 = temp_string_2[2] # Value after the .

            convert2_ = ord(convert2) - 33  # The point value
            convert3_ = str(ORDER_.index(convert1)) + str(convert2_)
            convert4_ = int(convert3_) - Symmetric_Key2
            Decrypted_Text.append(str(chr(convert4_)))

        elif (len(temp_string_2) == 1):
            convert1 = temp_string_2[0]
            convert3_ = str((int(ORDER_.index(convert1)) * 10) - Symmetric_Key2)
            Decrypted_Text.append(chr(int(convert3_)))

    print("".join(str(x) for x in Decrypted_Text))

Encryption_2()
Decryption_2()

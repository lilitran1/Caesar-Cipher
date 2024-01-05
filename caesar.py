import string

option = input("Do you want to (e)ncrypt or (d)ecrypt?: ")

while True:
    if option == "e":
        decrypted_message = input("Enter the message you want to encrypt: ").strip()
        k = int(input("Enter the key (1 through 26): "))
        output = ""

        for i in range(len(decrypted_message)):
            ch = decrypted_message[i]

            if ch == " ":
                output += " "
            elif ch.isupper():
                output += chr((ord(ch) + k-65) % 26 + 65)
            elif ch.islower():
                output += chr((ord(ch) + k-97) % 26 + 97)

        print("Your decrypted message is: " + output)


    elif option == "d":
        letters = (string.ascii_letters + string.digits + "!@#$%^&*()")

        encrypted_message = input("Enter the message you want to decrypt: ").strip()
        k = int(input("Enter the key (1 through 26): "))
        message = ""

        for ch in encrypted_message:
            if ch in letters:
                position = letters.find(ch)
                new_pos = (position - k) % 26
                new_char = letters[new_pos]
                message += new_char
            else:
                message += ch
        print("Your decrypted message is: " + message)

    try_again = input("Do you want to use caesar cipher again? (Yes/No): ")
    if try_again.lower() == "yes":
        option = input("Do you want to (e)ncrypt or (d)ecrypt?: ")
        continue
    elif try_again.lower() == "no":
        print("Program ended")
        break




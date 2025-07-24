import secrets
import string
import time 
import pyperclip
import os

def inputDetector(hint, limit):
    while True:
            try:
                user = int(input(f"{hint}{f"(0-{limit})" if limit == 1 else "(minimum 8)"}: "))
                if limit == 0:
                    if user < 8:
                        raise IndexError
                    else:
                        return user
                elif limit == 1:
                    if user != 0 and user != 1:
                        raise IndexError
                    else:
                        return user
            except (ValueError, IndexError):
                print(f"Try again!")
    """
    Handle user input for password settings.

    Args:
        hint (str): Prompt text to display to the user.
        limit (int): Input mode. 
            - 0: Minimum password length (must be >= 8)
            - 1: Boolean toggle (must be 0 or 1)

    Returns:
        int: Validated user input based on the mode.
    """
def getUserPreference():
    while True:
        try:
            length = inputDetector("How long the password've to be", 0)
            useUpper = inputDetector("Is uppercase required", 1)    
            useLower = inputDetector("Is lowercase required", 1)
            useDigits = inputDetector("Is digits required", 1)
            useSymbols = inputDetector("Is symbols required", 1)
            if useDigits == useLower == useSymbols == useUpper == 0:
                raise ValueError
            return length, useUpper, useLower, useDigits, useSymbols
        except ValueError:
            print("Password generate fail. Try Again.")
    """
    Collect user preferences for password generation.

    Prompts for:
        - Length of the password (>=8)
        - Whether to include uppercase, lowercase, digits, symbols

    Returns:
        tuple: (length, useUpper, useLower, useDigits, useSymbols)

    Raises:
        ValueError: If all character options are set to 0 (empty pool).
    """

def generatePassword(length, upper, lower, digits, symbols):
    wordPool = ''
    if upper:
        wordPool += string.ascii_uppercase
    if lower:
        wordPool += string.ascii_lowercase
    if digits:
        wordPool += string.digits
    if symbols:
        wordPool += string.punctuation
    if not wordPool:
        print("Password generate fail")
        return None
    return ''.join(secrets.choice(wordPool) for _ in range(length))
    """
    Generate a secure random password based on user preferences.

    Args:
        length (int): Desired length of the password.
        upper (int): Include uppercase letters (1 or 0).
        lower (int): Include lowercase letters (1 or 0).
        digits (int): Include digits (1 or 0).
        symbols (int): Include special characters (1 or 0).

    Returns:
        str: Generated password or None if no valid character set.
    """

def main():
    while True:
        preference = getUserPreference()
        if preference:
            password = generatePassword(*preference)
            os.system('cls')
            print("Your password is", password)
            pyperclip.copy(password)
            time.sleep(0.5)
            print("Password copied to clipboard.")
            again = input("Generate another password(y/n)").lower()
            if again == 'y':
                continue
            elif again == 'n':
                print("Bye..")
                time.sleep(3)
                break
            else:
                print("Idc anyway bye")
                time.sleep(1)
                break
    """
    Main loop for the password generator program.

    - Gets user preferences
    - Generates and displays a password
    - Copies the password to clipboard
    - Asks if user wants to generate another
    """

if __name__ == "__main__":
    main()
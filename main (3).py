import random
import string
import subprocess
import platform

def password_strength_looker(their_password):
    print(f'There are 5 conditions, length, presence of special characters, presence of digits and presence of different ASCII')
    score = []
    bad_reasons = []
    thing = list(their_password)
    if len(thing)>8:
        score.append('Has long enough length')
    else:
        bad_reasons.append('Does not have enough length')
    if any(char in string.punctuation for char in their_password):
        score.append('Has special characters.')
    else:
        bad_reasons.append('Does not have special_characters')
    if any(char.isdigit() for char in their_password):
        score.append('Has numbers')
    else:
        bad_reasons.append('Does not have numbers')
    if any(char.isupper() for char in their_password) and any(char.islower() for char in their_password):
        score.append('Has presence of different ASCII')
    else:
        bad_reasons.append('Does not have different presence of ASCII')
    return print(f'You got a {len(score)}/5 because of {score} and may have lost points due to {bad_reasons}.')

def copy_to_clipboard(text):
    """
    Copy text to clipboard using system commands.
    
    Args:
        text (str): The text to copy to clipboard
    Returns:
        bool: True if successful, False if failed
    """
    current_os = platform.system()
    
    try:
        if current_os == "Windows":
            # Windows clipboard command
            subprocess.run(
                "clip", 
                text=True,
                input=text,
                check=True,
                shell=True
            )
            return True
            
        elif current_os == "Darwin":  # macOS
            # macOS clipboard command
            subprocess.run(
                "pbcopy", 
                text=True,
                input=text,
                check=True
            )
            return True
            
        elif current_os == "Linux":
            # Try xclip first
            try:
                subprocess.run(
                    ["xclip", "-selection", "clipboard"],
                    input=text.encode('utf-8'),
                    check=True
                )
                return True
            except:
                # Try xsel if xclip fails
                try:
                    subprocess.run(
                        ["xsel", "-b", "-i"],
                        input=text.encode('utf-8'),
                        check=True
                    )
                    return True
                except:
                    print("Linux clipboard requires 'xclip' or 'xsel'")
                    return False
        else:
            print(f"Unsupported operating system: {current_os}")
            return False
            
    except Exception as e:
        print(f"Error copying to clipboard: {e}")
        return False
    

def password_gen(length):
    #get all characters from string module
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    special_characters = string.punctuation
    numbers = string.digits
    
    #put first 4 to guarantee everything is there
    #make sure to random choice again since you duplicated it
    password = [
            random.choice(uppercase),
            random.choice(lowercase),
            random.choice(special_characters),
            random.choice(numbers)
        ]
        
    #get the rest of the characters then format it properly
    for i in range(length-4):
        password.append(random.choice(uppercase + lowercase + special_characters + numbers))
        random.shuffle(password)
        
    return ''.join(password)
        

def main():
    #option a
    print('Welcome to my first practice project!')
    print('We have two systems, option (a) which is a password generator and option(b) which are to check if your current password is strong enough or not')
    options = input('Which do you choose?')
    if options == 'a':
        k = input('How many passwords do you want to make')
        passwords = []
        for i in range(int(k)):
            passwords.append(password_gen(random.randint(8,20)))
        print("\nYour passwords:")
        for i in range(len(passwords)):
            print(f"{i+1}. {passwords[i]}")
        print("\nWhich passwords do you want to copy?")
        print("Example: Enter '1 3 5' to copy passwords 1, 3, and 5")
        print("Or enter 'all' to copy all passwords")
        choice_input = input("Your choice: ")
            
        if choice_input.lower() == 'all':
            # Prepare text to copy
            text_to_copy = '\n'.join([f"{i+1}. {passwords[i]}" for i in range(len(passwords))])
            
            print("\nAll passwords to copy:")
            print("=" * 40)
            for i in range(len(passwords)):
                print(f"Password {i+1}: {passwords[i]}")
            print("=" * 40)
            
            # Actually copy to clipboard
            if copy_to_clipboard(text_to_copy):
                print("Copied to clipboard!")
        
        else:
            # Copy selected passwords
            try:
                # Split input into numbers
                choices = choice_input.split()
                selected_numbers = [int(num) - 1 for num in choices]
                
                # Prepare text to copy
                text_to_copy = '\n'.join([f"{num+1}. {passwords[num]}" for num in selected_numbers])
                
                print("\nSelected passwords to copy:")
                print("=" * 40)
                for num in selected_numbers:
                    print(f"Password {num+1}: {passwords[num]}")
                print("=" * 40)
                
                # Actually copy to clipboard
                if copy_to_clipboard(text_to_copy):
                    print("Copied to clipboard!")
            
            except:
                print("Invalid input. Please enter numbers like '1 3 5' or 'all'")
    if options == 'b':
        their_password = input('Put in the password you want to check: ')
        password_strength_looker(their_password)
        
if __name__ == '__main__':
    main()
from utils import generate_art_code, modify_art_code

def main():
    print("\nWelcome to Art Generation Chat!")
    print("Type 'exit' to quit")
    
    current_code = None
    while True:
        if current_code is None:
            print("\nOptions:")
            print("1. Create new art")
            print("2. Load existing art")
            choice = input("Choose an option (1-2): ").strip()
            
            if choice == "1":
                user_input = input("\nDescribe what you'd like to create: ").strip()
                current_code = generate_art_code(user_input)
                # Save and execute the generated code
                with open("generated_art.py", "w") as f:
                    f.write(current_code)
                exec(current_code)
                print("Art has been created!")
            elif choice == "2":
                try:
                    with open("generated_art.py", "r") as f:
                        current_code = f.read()
                    print("Previous art loaded!")
                    exec(current_code)
                except:
                    print("No existing art found. Let's create new art instead.")
                    user_input = input("\nDescribe what you'd like to create: ").strip()
                    current_code = generate_art_code(user_input)
                    exec(current_code)
                    print("Art has been created!")
            continue
            
        user_input = input("\nWhat would you like to change? (or type 'new' for new art, 'q' to quit): ").strip().lower()
        
        if user_input == 'q':
            print("Goodbye!")
            break
        elif user_input == 'new':
            current_code = None
            continue
            
        # Modify existing art
        current_code = modify_art_code(current_code, user_input)
        
        # Save and display the art
        with open("generated_art.py", "w") as f:
            f.write(current_code)
        exec(current_code)
        print("Art has been updated!")

if __name__ == "__main__":
    main()

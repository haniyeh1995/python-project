import random
def guessing_word():
    max_attemp = 6
    word_list = ["react", "python", "javascript", "katlin", "golang"]
    
    
    print("🎯Guess the word!")
    # print("_" * len(word))

    while True:
        attempt_left = max_attemp
        word = random.choice(word_list)
        letters = list(word)
        guessed_letters = []

        while attempt_left > 0:
            display = ""
            for i in letters:
                if i in guessed_letters:
                    display += i + " "
                else:
                    display += " _ "
            print("Word:", display.strip())

            if all(i in guessed_letters for i in letters):
                print("\n🎉 You won! The word was:", word)
                break
            
            guess = input("Guess a letter: ").lower()
           

            if len(guess) != 1 or not guess.isalpha():
                print("❗ Please enter only one letter.")
                continue

            if guess in guessed_letters:
                print("⚠️ You already guessed that letter.")
                continue

            guessed_letters.append(guess)

            if guess in letters:
                print("✅ Good guess!")
            else:
                attempt_left -= 1
                print(f"❌ Wrong! {attempt_left} tries left.")
        else:
            print("\n😢 You lost! The word was:", word)
        
        play_again= input("Do you want to play again?(yes/no):\n")
        if play_again.lower() == "no":
          print("ok, Bye!")
          break
        else:
           guessed_letters = []
           print("\nNew Game Started!")
guessing_word()

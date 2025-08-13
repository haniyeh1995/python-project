class Movie:
    def __init__(self, title, director, duration, watched_minute = 0):
        self.title = title
        self.director = director
        self.duration = duration
        self.watched_minute = watched_minute

    def watch(self, minute):
        if self.watched_minute + minute >= self.duration:
            self.watched_minute = self.duration
            print(f"You've finished watching '{self.title}'")
        else:
            self.watched_minute += minute
            print(f"you watch {self.watched_minute} minute of the '{self.title}'")
    
    def movie_info(self):
        print(f"🎬{self.title} | Director: {self.director} | Duration: {self.duration} minute | Watched: {self.watched_minute}")
    
    def remaining_time(self):
        return self.duration - self.watched_minute
    
movies = []

while True:
    print("\n🎞 Movie Manager Menu:")
    print("1. Add movie")
    print("2. Delete movie")
    print("3. Watch movie")
    print("4. Show movie list")
    print("5. Show remaining time")
    print("6. Exit")        


    choice = int(input("enter your option from 1 to 6: \n"))

    if choice == 1 :
        title = input("Enter movie title: ")
        director = input("Enter director name: ")
        duration = int(input("Enter duration (in minutes): "))
        movies.append(Movie(title, director, duration))
        print(f"✅ Movie '{title}' added.")

    elif choice == 2 :
         for idx, m in enumerate(movies):
            print(f"{idx + 1}. {m.title}")
         delete_index = int(input("Enter movie number to delete: ")) - 1
         if 0 <= delete_index < len(movies):
            removed = movies.pop(delete_index)
            print(f"🗑 '{removed.title}' deleted.")
         else:
            print("❌ Invalid number.")

    elif choice== 3 :
        for idx, m in enumerate(movies):
            print(f"{idx + 1}. {m.title}")
        index = int(input("Which movie did you watch? ")) - 1
        if 0 <= index < len(movies):
            minutes = int(input("How many minutes did you watch? "))
            movies[index].watch(minutes)
        else:
            print("❌ Invalid number.")
    
    elif choice == 4 :
        if movies:
            print("\n📚 Your Movies:")
            for m in movies:
                m.movie_info()
        else:
            print("⚠️ Movie list is empty.")

    elif choice == 5:
        for m in movies:
            print(f"{m.title}: {m.remaining_time()} minutes remaining.")

    elif choice == 6:
        print("👋 Exiting Movie Manager. Goodbye!")
        break

    else:
        print("❌Invalid choice. Please select 1 to 6.")
# Victor Cruzat CIS 261 Movie Guide Part 1
 

print ("\nThe Movie List Program")

def show_menu():
   
    
    print ("\nCOMMAND MENU")
    print ("list - List all movies")
    print ("add - Add a movie")
    print ("del - Delete a movie")
    print ("exit - Exit the program")
    
def list_movies(movies):
    print ("\nMovies:")
    for index, movie in enumerate (movies, start = 1):
        print (f"{index}. {movie}")
        
def add_movie(movies):
    movie = input ("\nEnter the movie title: ")
    movies.append(movie)
    print(f"{movie} has been added to the list.")
    
def delete_movie(movies):
    list_movies(movies)
    try:
        index = int(input("Enter a movie number to delete: "))
        if  1 <= index <= len(movies):
            removed_movie = movies.pop(index-1)
            print(f"{removed_movie} has been deleted from the list.")
        else:
            print(f"Invalid number. Please try again.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    movies = ["The Fiddler on The Roof", "Die Hard", "Rush Hour", "Limitless"]
    show_menu()
    while True:
        
        choice = input("\nCommand: ")
        if choice == "list":
            list_movies(movies)
        elif choice == "add":
            add_movie(movies)
        elif choice == "del":
            delete_movie(movies)
        elif choice == "exit":
            print("Bye!")
            break
        else:
            print("Invalid choice. please try again.")
            


main()
    
 
 

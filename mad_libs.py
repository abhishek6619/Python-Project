def mad_libs():
    print("Welcome to the Mad Libs Game!\n")
    
    # Taking user inputs
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    
    # Creating a funny story
    story = f"One day, {name} went to {place}. There, they saw a {adjective} {animal} that was {verb} all around. It was the most hilarious thing {name} had ever seen!"
    
    print("\nHere is your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    mad_libs()

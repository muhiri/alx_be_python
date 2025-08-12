print ("""
       You will be prompted to enter a noun and adjectives.
       The program will then create a short story using your inputs.
       """)
adj1 = input("Enter an adjective (sunny/cold/windy):")
adj2 = input("Enter another adjective (new/finished/tall):")
adj3 = input("Enter another adjective (humble/hardworking/organized):")
noun = input("Enter a noun (a name or construction role):")
new_apartments = f"apartments being constructed in my neighborhood"
finished_apartments = f"apartments being shown to the public"
tall_apartments =f"apartments that were almost being completed"
match adj2:
    case "new":
        filler = new_apartments
    case "finished":
        filler = finished_apartments
    case "tall":
        filler = tall_apartments
    case _:
        filler = "buildings that were under construction"
story = f"""
Today, on a beautiful {adj1} evening, I decided to take a walk.
I saw some {adj2} {filler}.
In the construction, I saw {noun} waving to their partners to hurry up and end the day.
I thought to myself, 'Wow, people are so {adj3}'
"""
print(story)
print("I hope you enjoyed the story!")

print ("""
       You will be prompted to enter a noun and adjectives.
       The program will then create a short story using your inputs.
       """)
adj1 = input("Enter an adjective:")
adj2 = input("Enter another adjective:")
adj3 = input("Enter another adjective:")
noun = input("Enter a noun:")
story = f"""
Today, on a beautiful {adj1} evening, I decided to take a walk.
I saw big {adj2} apartments that were almost being completed.
In the construction, I saw {noun} waving to their partners to hurry up and end the day.
I thought to myself, 'Wow, people are so {adj3}'
"""
print(story)
print("I hope you enjoyed the story!")

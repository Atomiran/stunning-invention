
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)

print(bicycles[0])  # First bicycle
print(bicycles[1].title())  # Second bicycle with title case
print(bicycles[2])  # Third bicycle
print(bicycles[3])  # Fourth bicycle
print(bicycles[-1])  # Last bicycle using negative index
print(bicycles[-2].upper())  # Second to last bicycle in uppercase
print(bicycles[-3].lower())  # Third to last bicycle in lowercase
print(bicycles[-4].title())  # Fourth to last bicycle with title case
print(f"My first bicycle was a {bicycles[0].title()}.")  # Formatted string with first bicycle
bicycles[0] = 'ducati'  # Modifying the first bicycle
print(bicycles)  # Print modified list
bicycles.append('harley-davidson')  # Adding a bicycle to the end of the list
print(bicycles)  # Print list after appending




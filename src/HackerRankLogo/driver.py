from util import generate_logo

thickness = int(input())
logo = generate_logo(thickness)

for line in logo:
    print(line)

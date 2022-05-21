import time
print("Hey ich helfe dir zu berechnen, wie Schwer du auf den verschiedenen Planeten bist ;)")
time.sleep(3)
user_weight = input("Wie viel wiegst du in kg?").strip().capitalize()
time.sleep(1)
print("Es gibt 6 verschiedene Planeten zur Auswahl")
planeten = ["Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
for x in planeten:
    print(x)
    time.sleep(1)
planet_choice = input("Für welchen Planeten entscheidest du dich?").strip().capitalize()
if planet_choice == "Venus":
    weight = float(user_weight) * 0.91
elif planet_choice == "Mars":
    weight = float(user_weight) * 0.38
elif planet_choice == "Jupiter":
    weight = float(user_weight) * 2.34
elif planet_choice == "Saturn":
    weight = float(user_weight) * 1.06
elif planet_choice == "Uranus":
    weight = float(user_weight) * 0.92
elif planet_choice == "Neptun":
    weight = float(user_weight) * 1.19
print("Dein Gewicht beträgt auf dem Planet " + planet_choice + " " + str(round(weight)) +" kg")

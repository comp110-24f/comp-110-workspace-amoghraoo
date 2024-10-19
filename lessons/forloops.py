"""Writing for loops."""

pets: list[str] = ["Louie", "Bo", "Bear"]
new_pets: list[str] = []

for elem in pets:
    print(f"Good boy, {elem}!")

for x in [1, 2, 3]:
    print(x)

names: list[str] = ["Alyssa", "Janet", "Vrinda"]

for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")

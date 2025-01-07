string = input("Enter a String:")
v = 0
w = 0
x = 0
y = 0
z = 0



for a in string:
    if a == "a":
        v += 1
for e in string:
    if e == "e":
        w += 1
for i in string:
    if i == "i":
        x += 1
for o in string:
    if o == "o":
        y += 1
for u in string:
    if u == "u":
        z += 1

if v > 0:
    print(f"a = \"{v}\"")

if w > 0:
    print(f"e = \"{w}\"")

if x > 0:
    print(f"i = \"{x}\"")

if y > 0:
    print(f"o = \"{y}\"")

if z > 0:
    print(f"u = \"{z}\"")

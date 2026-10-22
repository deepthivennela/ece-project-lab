
print("DIGITAL LOGIC TRUTH-TABLE GENERATOR")
print()

print("A  B  AND  OR")

for A in [0, 1]:
    for B in [0, 1]:
        and_output = int(bool(A) and bool(B))
        or_output = int(bool(A) or bool(B))
        print(A, B, and_output, or_output)

print()
print("NOT GATE")
print("A  NOT")

for A in [0, 1]:
    not_output = 1 - A
    print(A, not_output)

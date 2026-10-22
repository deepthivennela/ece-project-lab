print("DIGITAL LOGIC TRUTH-TABLE GENERATOR")
print()

print("A B | AND OR XOR NAND NOR")
print("-------------------------")

for A in [0, 1]:
    for B in [0, 1]:
        and_out = A & B
        or_out = A | B
        xor_out = A ^ B
        nand_out = 1 - and_out
        nor_out = 1 - or_out

        print(A, B, "|", and_out, or_out,
              xor_out, nand_out, nor_out)

print()
print("NOT GATE")
print("A | NOT")
print("--------")

for A in [0, 1]:
    print(A, "|", 1 - A)

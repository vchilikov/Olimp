number_of_faces = {'T': 4, 'C': 6, 'O': 8, 'D': 12, 'I': 20}
n = int(input())
print(sum(number_of_faces[input()[0]] for _ in range(n)))

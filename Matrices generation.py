N = int(input("Diemnsão da Matriz: "))
matriz = [0] * N #Gera um vetor principal de tamanho N
print(matriz)
for i in range(N): #Laço para gerar um vetor de tamanho N em cada posição do vetor principal
    matriz[i] = [0]*N

print(matriz)


#===================================================================
for l in range(N):
    for c in range(N):
        matriz[l][c] = int(input(f"Entradas da Matriz[{l}][{c}]: "))
print("-="*30)

for l in range(N):
    for c in range(N):
        print(f"[{matriz[l][c]:^3}]", end="")
    print()# print que faz parte da linha para fazer o pulo

total = 0
i = 0
while total <= 2 and i < N:
    grau = 0
    for c in range(N):
        grau += matriz[i][c]
    if grau % 3 == 0:
        total += 1
    i +=1

if total > 2:
    print("\nNão existe um caminho de Euler")
else:
    print("\nExiste um caminho de Euler")
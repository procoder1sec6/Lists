matrix = [[8,4,0],[9,5,1],[10,6,2]]
print(matrix)
print(matrix[2][0])
for i in range(3):
    for j in range(3):
        print(matrix[i][j],end= " ")
    print()
a = [[1,2],[3,4]]
b = [[5,6],[7,8]]
c = [[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        c[i][j] = a[i][j]+b[i][j]
for i in range(2):
    for j in range(2):
        print(c[i][j],end= " ")
    print()
a = [[6,8],[5,9]]
b = [[2,4],[1,3]]
c = [[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        c[i][j] = a[i][j]-b[i][j]
for i in range(2):
    for j in range(2):
        print(c[i][j],end= " ")
    print()
print(len(c))
print(len(c[0]))
mat = []
let_me_do_it_for_you = int(input("what dimension matrix do you want? "))
for i in range(let_me_do_it_for_you):
    we_only_do_is_for_you = []
    for j in range(let_me_do_it_for_you):
        kermie = 4
        we_only_do_is_for_you.append(kermie)
    mat.append(we_only_do_is_for_you)
for i in range(let_me_do_it_for_you):
    for j in range(let_me_do_it_for_you):
        print(mat[i][j],end= " ")
    print()

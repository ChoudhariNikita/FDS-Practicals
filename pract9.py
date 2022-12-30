'''
Experiment No. 9 : Write a Python Program to compute following computation on matrices :
                   a)Addition of two matrices
                   b)Subtraction of two matrices
                   c)Multiplication of two matrices
                   d)Transpose of a matix
'''
matrix1=[[1,2],[3,4]]
matrix2=[[5,6],[7,8]]
result=[[0,0],[0,0]]

# 1 2  5 6
# 3 4  7 8

flag=1
while flag==1:
    print("\n\n--------------------MENU--------------------\n")
    print("1. View Matrix 1 & Matrix 2")
    print("2. Addition of matrix")
    print("3. Subtraction of matrix")
    print("4. Multiplication of matrix")
    print("5. Transpose of matrix")
    print("6. Exit\n")
    ch=int(input("Enter your Choice (from 1 to 6) :"))

    if ch==1:
        print("Matrix 1:")
        for i in matrix1:
            print(i)

        print("Matrix 2:")
        for i in matrix2:
            print(i)

        a = input("Do you want to continue (y/n) :")
        if a == "y":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==2:
        result=[[0,0],[0,0]]
        print("Addition of matrix: ")
        
        for i in range(len(matrix1)):
            for j in range(len(matrix2)):
                result[i][j]=matrix1[i][j]+matrix2[i][j]

        for i in result:
            print(i)

        a = input("Do you want to continue (y/n) :")
        if a == "y":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==3:
        result=[[0,0],[0,0]]
        print("Subtraction of matrix: ")
        
        for i in range(len(matrix1)):
            for j in range(len(matrix2)):
                result[i][j]=matrix1[i][j]- matrix2[i][j]

        for i in result:
            print(i)

        a = input("Do you want to continue (y/n) :")
        if a == "y":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==4:
        result=[[0,0],[0,0]]
        print("Multiplication of matrix: ")
        
        for i in range(len(matrix1)):
            for j in range(len(matrix2)):
                for k in range(len(matrix1)):
                    result[i][j]+=matrix1[i][k]*matrix2[k][j]

        for i in result:
            print(i)

        a = input("Do you want to continue (y/n) :")
        if a == "y":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==5:
        result=[[0,0],[0,0]]
        print("Transpose of matrix1: ")

        for i in range(len(matrix1)):
            for j in range(len(matrix2)):
                result[i][j]=matrix1[j][i]

        for i in result:
            print(i)

        result=[[0,0],[0,0]]
        print("Transpose of matrix2: ")

        for i in range(len(matrix1)):
            for j in range(len(matrix2)):
                result[i][j]=matrix2[j][i]

        for i in result:
            print(i)

        a = input("Do you want to continue (y/n) :")
        if a == "y":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==6:
        flag=0
        print("Thanks for using this program!")

    else:
        print("!!Wrong Choice!! ")
        a=input("Do you want to continue (y/n) :")
        if a=="y" :
            flag=1
        else:
            flag=0
            print("Thanks for using this program!")

import numpy as np
"""1 – Crie um array NumPy com valores de 0 a 11, faça um reshape deste array para uma matriz 3x4. Utilizando indexação, imprima:
Toda a segunda linha.
O valor localizado na terceira linha, quarta coluna."""
opcoes = input("Digite uma opção: ")
match opcoes:
    case "1":
        n_array= np.array([0,1,2,3,4,5,6,7,8,9,10,11])
        n_array=np.reshape(n_array,(3,4))
        print(n_array[1])
        print(n_array[2,3])
    case "2":
        '''2 – Crie dois arrays 1D NumPy com valores [1, 2, 3] e [4, 5, 6] e concatene-os formando um único array. Após isso, faça slicing para obter apenas os elementos [2, 3, 4, 5].
'''
        a1=np.array([1,2,3])
        a2=np.array([4,5,6])
        a1=np.concatenate((a1,a2))
        print(a1[1:5])
    case"3":
        """3 – Crie um array original com valores [10, 20, 30, 40, 50].  Faça uma cópia deste array.  Remova o elemento 30 da cópia sem alterar o original.  Imprima os dois arrays para mostrar que o original permanece inalterado."""
        sim=np.array([10,20,30,40,50])
        nao= np.copy(sim)
        nao=np.delete(nao,[2])
        print(sim)
        print(nao)
    case"4":
        """
4 – Crie um array com valores [100, 200, 300, 400, 500, 600], divida-o (split) esse array em dois arrays separados, cada um com três elementos.  No segundo array resultante, adicione o valor 700 ao final.  Imprima ambos arrays finais."""
        new=np.array([100,200,300,400,500,600])
        a,b = np.split(new,2)
        print(a)
        print(b)
        b=np.append(b,[700])
        print(b)
        

                
        




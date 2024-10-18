def solution(lista1,lista2):
    soma=0
    for c in range(0,len(lista1)):
        soma += ((lista1[c]-lista2[c])**2)
    media = soma/len(lista1)
    print(media)

solution([1,2,3],[4,5,6])
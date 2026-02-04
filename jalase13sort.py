for i in range(len(A)-1):
    min=A[i]
    k=i
    for j in range(i,len(A)):
        if A[j]<min:
            min=A[j]
            k=j
     A[i],A[k]=A[k],A[i]
    



def merge(A):
    if len(A)>1:
        mid=len(A)//2
        L=A[:mid]
        R=A[mid:]
        merge(L)
        merge(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i] < R[j]:
                A[k]=L[i]
                i+=1
            else :
                A[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            A[k]=L[i]
            i+=1
            K+=1
        while j<len(R) :
            A[k]=R[j]
            j+=1
            k+=1




def partiton(A,low,high):
    pivot = A[high]   
    i = low-1 
    for j in range(low,high):
        if A[j] <= pivot:
            i += 1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[high]=A[high],A[i+1]
    return i+1



def Quick(A,low,high):
    if low<high:
        pi = partiton(A,low,high)
        Quick(A,low,pi-1)
        Quick(A,pi+1,high)
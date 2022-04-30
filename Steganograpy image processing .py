from matplotlib.cbook import flatten
import numpy as np
import matplotlib.image as mpi

img=mpi.imread('dp.jpg')
n=np.array(img)
a=n.flatten()

while True :
    print ("\n 1.Encode")
    print ("2.Decode")
    choice=int(input("enter the type of action to perform : "))
    if choice== 1:  ######## encode
        print ("Encode :")
        message=input('Enter the message : ')
        l=list(message) ## read message as 
        for i in range (0,len(l)):
            a[i]=ord(l[i]) 
            # print(a[i],ord(l[i])) 
            d=a.reshape(img.shape)
            #mpi.imsave('encrypted.jpg', d) #### print encrypted image and saves it
            continue
    elif choice== 2:
        print("Decode :")
        q=np.equal(img,d)
        c=d[q==False]
        F=[]
        for i in range (0,len(c)):
            g = (chr(c[i]))
            print(g,end="")# print decrypted message

            
            continue
    else:
         break
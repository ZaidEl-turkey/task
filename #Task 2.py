##########
# task 2 #
##########

"""
old=int(input("Old Bread"))
freash=int(input("Freash Bread"))

def price(old,freash):
    old_price=((500*old)*0.06)
    freash_price=(500*freash)
    total= old_price+freash_price
    print("the old cost : "+str(old_price))
    print("the freash cost : "+str(freash_price))
    print("the total price : "+str(total))



price(old,freash)    

"""

##########
# task 1 #
##########

m=[]
list=int(input("Enter Your Numbers As a list"))

for i in range (0,list):
   x=int(input("Enter the elment of the list"))
   m.append(x)
for i in range (0,len(m)-1):
   for x in range (i+1,len(m)) :
      if (m[i]>m[x]) :
         print("False")
      else :
         print("True")
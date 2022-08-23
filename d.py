# l=[1,9,3,7,5]
# for i in range(0,len(l)-1):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==10:
#             print(l[i],l[j])
# n=int(input())
# for i in range(n):
#     a,b=input().split()
#     if b==0:
#         print(int(a)/int(b))
#     elif b=='$':
#         print(int(a)/int(n))
#     else:
#         print(int(a)/int(b))
# n=3
# y=0
# sum=0
# l=[1,2,3,9,12,13,7,6,14,5]
# for i in range(0,len(l)-n):
# # class big():
# #     def m1(self):
# #         n=int(input())
# #         l=list(map(int,input().split()))
# #         x=0
# #         y=0
# #         for i in range(0,len(l)):
# #             z=sum(l[i:i+n])
# #             if z>x:
# #                 x=z
# #                 y=i
# #         print(l[y:y+n])
# #         print(sum(l[y:y+n]))
    

        
   
# # b=big()
# # b.m1()
# # class parent():
# #     def first(self):
# #         print('first function')
# # class child(parent):
# #     def second(self):
# #         print('secon function')
# # ob=child()
# # ob.first()
# # ob.second()
# class parent:
#     def __init__(self,fname,fage):
#         self.firstname=fname
#         self.age=fage
#     def show(self):
#         print(self.firstname,self.age)
# class child(parent):
# #     def __init__(self,fname,fage):
# #         parent.__init__(self,fname,fage)
# #         self.lastname='jain'
# #     def show(self):
# #         print(self.firstname,self.age,self.lastname)
# # ob=child('gourav',28)
# # ob.show()

# # for i in range(1,11):
# #     for j in range(1,11):
# #         print(i*j,end=' ')
# #     print()
# # # l=[(i*j) for j in range(1,11) for i in range(1,11)]
# # # print(l)
# # class parent:
# #     def m1(self):
# #         print('this is fun 1')
# # class child(parent):
# #     def m2(self):
# #         print('this is second fun')
# # class child1(parent):
# #     def m3(self):
# #         print('this is a third fun')
# # class child3(child1,child,parent):
# #     def m4(self):
# #         print('i am a fourth fun')
# # ob=child3()
# # ob.m2()
# from re import sub


# a=list(set(map(int,input().split())))
# n=int(input())
# ll=[]
# for i in range(n):
#     b=list(set(map(int,input().split())))
#     # print(b)
#     ll.append(b)
#     # print(ll)
# for i in range(0,len(ll)):
#     # print(ll[i])
#         for j in ll[i]:
#             if ll[i] not in 
    # if ll[i] in a and ll[i+1] not in a:
    #     print('false')
#     # elif ll[i] not in a and ll[i+1] in a:
#     #     print('false')
#     # elif ll[i] in a and ll[i+1] in a:
# #     #     print('true')
    

# #     # if i in ll[0] and i not in ll[1]:
# #     #     print('Flase')
# #     # # elif ll[0] not in i and ll[1] in i:

# #     # #     print('flase')
# #     # #     break

# #     # elif ll[0] in i and ll[1]  in i:
# #     #     print('true')
# # # l=[2,3,4,5,6]
# # # l.sort()
# # # print(l)
# # a=set(map(int,input().split()))
# # n=int(input())
# # ll=[]
# # for i in range(n):
# #     j=list(set(map(int,input().split())))
# #     ll.append(j)
# # for i in a:
# #     if i in ll[0] and ll[1] :
# #         print('True') 
# #         continue
# #     else:
# #         print('False') 

# n=int(input())
# for i in range(0,n):
#     for j in range(0,n):
#         if i==j:
#             break
#         elif i!=j:
#             print(i,j)
# x=int(input())
# y=int(input())
# z=int(input())
# n=int(input())
# m=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
# print(m)

# file = open(r"C:\Users\saura\Downloads\Sukoshal_Jain_Resume (1).pdf",errors="ignore")
# for i in file:
#     print(i)
# class ExceptionHandling():
#     def fun(self,x):
#         self.x=2
#         for i in range(-4,10):
#             try:
#                 print(self.x/2)
#             # except ZeroDivisionError as e:
#             #     print("errorzzz",e)
#             except Exception as e:
#                 print("error",e)
#             except Exception as e:
#                 print("Exception",e)
#             finally:
#                 print("sssssssssssssssssss")
#         print("loop ended!!")
# c = ExceptionHandling()
# c.fun(5)



a=5
b=5
try:
    a/b
except Exception as e:
    print('error occured' , e)
finally:
    print('code over!!')



        













    






    



        

        


        



    



    
    
    
        
    
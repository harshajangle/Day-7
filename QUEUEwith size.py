# ###===========QUEUE ELEMENT WITH SIZE limit============###
# import sys
# class Queue:
#     def __init__(self,queueSize): #parameterize constructor
#         self.queueList=[]
#         self.queueSize=queueSize
        
#     def isFull(self):
#         if len(self.queueList)==self.queueSize:
#             return True
#         else:
#             return False
        
#     def Enqueue(self,value):
#         if self.isFull():
#             print("queue is full")
#         else:
#              self.queueList.append(value)
        
#     def displayQueue(self):
#         print("--------------------")
#         print(self.queueList)
#         print("--------------------")
        
#     def isEmpty(self):
#         if self.queueList==[]:
#             return True
#         else:
#             return False
        
#     def dequeue(self):
#         if self.isEmpty():
#             return "queue is empty"
#         else:
#             return self.queueList.pop(0)
        
#     def deleteQueue(self):
#         self.queueList=None
#         return "queue is deleted"
    
#     def peek(self):
#         if self.isEmpty():
#             return "queue is empty"
#         else:
#             return self.queueList[0]
        
# size=int(input("enter the size of queue="))      
# queueObj = Queue(size)
        
# while True:
    
#     print("1.enqueue element in queue:")
#     print("2.display queue element:")
#     print("3.Check queue isEmpty:")
#     print("4.dequeue operation:")
#     print("5.delete queue")
#     print("6.peek operation")
#     print("7.exit")

#     choice=int(input("enter your choice"))
#     if choice == 1:
#         val=int(input("enter the value for queue:"))
#         queueObj.Enqueue(val)
#     elif choice==2:
#         queueObj.displayQueue()
#     elif choice==3:
#         print(queueObj.isEmpty())
#     elif choice==4:
#          print(queueObj.dequeue())
#     elif choice==5:
#         print(queueObj.deleteQueue())
#     elif choice==6:
#         print(queueObj.peek())
#     elif choice==7:
#         sys.exit()
        
        
#####==========TIME COMPLEXITY=========#####
# def findBiggestNumber(array):   
#     firstVal=array[0]          =======>O(1)
#     for i in range(1,len(array)): ======>O(N)
#         if array[i]>firstVal:    =======>O(1)
#             firstVal=array[i]    =======>O(1)
#     return firstVal              ======>O(1)
# array=[2,4,5,6,7,1,9,3,4,5,6]
# print(findBiggestNumber(array))  ========>O(1)


# s=input("enter string:")
# special=['@','#,"|',""]
# count=0
# for ch in s:
#     if ch in special:
#         count+=1
# print("output:",count)       

# import math
# n = int(input())
# arr = list(map(int, input().split()))
# count = 0
# for num in arr:
#     root = int(math.sqrt(num))
#     if root * root == num:
#         count += 1
# print(count)


#####=========================LINEAR SEARCH========================#####
# def linearSearch(array,target):
#     for i in range(len(array)):
#         if array[i]==target:
#             return i
#     return -1
# array=[1,2,3,4,5,6,7,8,9]
# target=5
# result=linearSearch(array,target)
# if result==-1:
#     print("Not found")
# else:
#     print("Element found at index no=",result)


#####==========================Binary SEARCH==========================#####
# def linearSearch(array,target):
#     start=0
#     end=len(array)-1
#     while start <=end:
#         mid=(start+end)//2
#         if array[mid]==target:
#             return mid
#         elif array[mid]<target:
#             start=mid+1
#         else:
#             end=mid-1
# sortedArray=[1,2,3,4,5,6,7,8,9]
# target=5
# result=linearSearch(sortedArray,target)
# if result==-1:
#     print("Not found")
# else:
#     print("Element found at index no=",result)



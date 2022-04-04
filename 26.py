#計算字元出現次數
a = lambda x,y:x.count(y)

str1= list(input())
char1= input()

times=a(str1,char1)

print("字元 {} 出現次數為 {} ".format(char1,times))

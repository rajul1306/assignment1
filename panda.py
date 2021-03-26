cls = int(input())
lst = input().split()
lst = list(map(int,lst))
start,max = cls,0
for i in range(cls):
    if lst[i] == 1:
        start = i
        break
p = range(cls)
for i in p[cls-1 ::-1]:
    if lst[i]==1:
        max = i
        break
count = 0
for i in range(start,max-1):
     if lst[i]==1:
      if lst[i+1]!=1:
         count+=1
     else:
            count+=1
print(count+1)




# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

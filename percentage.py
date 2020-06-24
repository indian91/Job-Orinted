import time
def main():
    s='''1.Create File\n2.Enter Marks\n3.Show Result'''
    print(s)
    ch=int(input('Enter choice from above'))
    if ch==1:
        create_file()
    elif ch==2:
        enter_marks()
    elif ch==3:
        show_result()
    else:
        exit()
        
def exit():
    print('Thanks for using our service')
    for i in '..........Exciting..........':
        time.sleep(0.1)
        print(i,end='')
        
def create_file():
    f=open('percentage1.txt','w')
    s='Name\tP\tC\tM'
    f.write(s)
    f.close()
    print('File Created Successfully')
    time.sleep(1)
    main()
    
def enter_marks():
    f=open('percentage1.txt','a')
    for i in range(int(input('Enter the number of student: '))):
        s=f"\n{input('Enter Name')}\t{input('Enter Physics Marks')}\t{input('Enter Chemistry Marks')}\t{input('Enter Maths Marks')}"
        f.write(s)
    f.close()
    
    
def show_result():
    f=open('percentage1.txt')
    data=f.read()
    data=data.split('\n')
    for i in range(1,len(data)):
        data1=data[i].split('\t')
        sum1=0
        for j in range(1,len(data1)):
            sum1+=int(data1[j])
        print(f"{data1[0]} got {round(sum1/3,2)}%")
        
        
main()

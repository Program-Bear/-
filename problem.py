import random
import time
def poem_pro(poem,num):
    emp = '〇'
    l = len(poem)
    f = random.randint(0,l - 1)
    s = random.randint(0,l - 1)
    while abs(f - s) <= 1:
        s = random.randint(0,l - 1)
    #print("two num: %d, %d"%(f,s))
    ans = ''
    
    for i in range(0, l):
        
        if (i == f):
            ans = ans + poem[i]
            continue
            
        if (i == s and num == 2):
            ans = ans + poem[i]
            continue

        ans = ans + emp
        
    return ans

if __name__ == "__main__":
    file_object = open("data.txt",'r')
    pro = file_object.readlines();
    fin = False
    print("开始答题，输入n并回车下一题，输入e并回车退出")
    tot = len(pro)
    index = [i for i in range(0,tot)]
    #random.shuffle(index)

    for i in index:
        line = pro[i]
        
        start = time.time()
        
        try:
            poem = line.split()[0]
            author = line.split()[1]

            num = 1
            temp = random.randint(1,10)
            if (temp <= 3):
                num = 2
            print(poem_pro(poem,num) + '||' + author)
        
            while(True):

                temp = input()
                if (temp == 'n'):
                    break
                if (temp == 'e'):
                    fin = True
                    break
                
            if (fin == True):
                break

            print("正确答案为：" + poem + '||' +author)
            #print(time.time() - start)
            spend = (time.time() - start)
            print("用时：" + str(spend) +'秒')
            
            if spend > 10:
                print("已超时，答题失败")
            print("\n")

        except:
            print("panic")
            
    print("答题结束")

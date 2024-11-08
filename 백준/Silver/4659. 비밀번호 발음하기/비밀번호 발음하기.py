import sys
input = sys.stdin.readline

if __name__ == '__main__':
    vowel = ['a', 'e', 'i' , 'o', 'u']
    cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

    while True:
        password = input()[:-1]
        accept = True
        if password == 'end':
            break

        #조건3
        for v in vowel:
            if v != 'e' and v != 'o' and v*2 in password:
                accept = False
                break
        for c in cons:
            if c*2 in password:
                accept = False
                break
        
        if accept == True:
            # 모든 모음을 a로 변경하기
            a_password = password.replace('e', 'a').replace('i', 'a')\
                .replace('o', 'a').replace('u', 'a')
            words = a_password.split('a')
    
            #조건1
            if len(words) == 1:
                accept = False
    
            #조건2
            elif 'aaa' in a_password:
                accept = False
            for w in words:
                if len(w) >= 3:
                    accept = False
                    break

        if accept:
            print(f'<{password}> is acceptable.')
        else:
            print(f'<{password}> is not acceptable.')
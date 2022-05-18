
def Convert(n):
    thousads =["","M","MM","MMM"]
    hundres = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]

    th = thousads[ (n//1000)% 10]
    h = tens[ (n//100)% 10]
    t = [ (n//10)% 10]
    O = ones[n%10]


    result = (th+h+t+O)


if __name__ =="__main__":
    
     number= int(input("Enter a number: "))
     print(Convert(number))
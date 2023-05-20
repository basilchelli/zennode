def cart_total(p,q):
    t=0
    for i in range(3):
        t+=q[i]*p[i]
    return t

def Shipping_fee(tq):
    p=tq//10
    if tq%10 != 0:
        p+=1
    fee=p*5
    return fee

def flat_10_discount(p,q):
    z=cart_total(p,q)
    if z>=200:
        return 10
    return 0

def bulk_5_discount(q,p):
    total=0
    for i in range(3):
        if q[i]>=10:
            t=q[i]*p[i]*0.05
            if t>total:
                total=t
    return total

def bulk_10_discount(tq,p,q):
    if tq>=20:
        z=cart_total(p,q)
        return z*0.1
    return 0

def tiered_50_discount(tq,p,q):
    result=0
    if tq>=30:
        for i in range(3):
            r=0
            if q[i]>15:
                t=tq-q[i]-15
                if t>=0:
                    r=q[i]*p[i]*.5
                else:
                    r=(q[i]+t)*p[i]*.5
            if r>result:
                result=r
    return result

def discount_choose(tq,p,q):
    a=flat_10_discount(p,q)
    b=bulk_5_discount(q,p)
    c=bulk_10_discount(tq,p,q)
    d=tiered_50_discount(tq,p,q)
    if a==0 and b==0 and c==0 and d==0:
        return 0
    elif a>=b and a>=c and a>=d:
        return 1
    elif b>=a and b>=c and b>=d:
        return 2
    elif c>=b and c>=a and c>=d:
        return 3
    else:
        return 4
    
def final(q):
    p=[20,40,50]
    n=["Product A","Product B","Product C"]
    tq=q[0]+q[1]+q[2]
    dic={
        1:"'flat_10_discount'",
        2:"'bulk_5_discount'",
        3:"'bulk_10_discount'",
        4:"'tiered_50_discount'",
        0:"'Discount is not applicable!'"
    }
    dic1={
        1:flat_10_discount(p,q),
        2:bulk_5_discount(q,p),
        3:bulk_10_discount(tq,p,q),
        4:tiered_50_discount(tq,p,q),
        0:0
    }
    for i in range(3):
        print("product name:",n[i],"quantity:",q[i],"amount:",q[i]*p[i])
    print("total quantity:",tq,"total amount:",cart_total(p,q))
    print("applied discount:",dic.get(discount_choose(tq,p,q)),"discount amount:",dic1.get(discount_choose(tq,p,q)))
    print("shipping fee:",Shipping_fee(tq),"gift wrap fee:",tq)
    print("total:",cart_total(p,q)+Shipping_fee(tq)+tq-dic1.get(discount_choose(tq,p,q)))

    
q=[16,15,15]
final(q)

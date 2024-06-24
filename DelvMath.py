from math import sqrt
import time
#//Creator : DelvCH
print("Creator : DelvCH")
print("v1.1")
print("Latest update 6/24/2024:")
print("-Added Quadratic Formula Calculator")
print("-Support Decimal number")
print("-Bugs fixed")
def changelog():
    print("----------------------------------------")
    print("Changelog")
    print()
    print("[Area of 2D Geometry] Unreleased - 9/9/2023")
    print("-Added Area(A) of Square,Rectangle,Triangle,Circle,Trapesium,Diamond,Parallelogram,kite,1/2 Circle,1/4 Circle")
    print()
    print("[v0.1 Beta] Unreleased - 5/15/2024")
    print("-Added 2D_Geometry Perimeter(p)")
    print()
    print("[v0.2 Beta] Unreleased - 5/18/2024")
    print("-Added 3D_Geometry Volume(V) and Area(A)")
    print()
    print("[v1.0] Released - 6/14/2024")
    print("-Added smart features")
    print("-Added quick exit")
    print()
    print("[v1.0.1] Released - 6/14/2024")
    print("-Bugs fixed")
    print()
    print("[v1.1] Released - 6/24/2024")
    print("-Added Quadratic Formula Calculator")
    print("-Support Decimal number")
    print("-Bugs fixed")
    print()
    print("1.Back")
    option=input("Input : ")
    while option!='1':
        option=input("Input : ")
    if option=='1':
        optionMain()
def geometry():
    def area2D():
        print("----------------------------------------")
        print("Area(A)")
        print()
        print("1.Square")
        print("2.Rectangle")
        print("3.Triangle")
        print("4.Circle")
        print("5.Trapesium")
        print("6.Diamond")
        print("7.Parallelogram")
        print("8.Kite")
        print("9.1/2_Circle")
        print("10.1/4_Circle")
        print("11.3/4_Circle")
        print("12.Back")
        print("13.Return to Geometry option")
        print("14.Quick exit")
        option=input("Input : ")
        while option!='1' and option!='2' and option!='3' and option!='4' and option!='5' and option!='6' and option!='7' and option!='8' and option!='9' and option!='10' and option!='11' and option!='12' and option!='13' and option!='14':
            option=input("Input : ")
        if option=='1':
            print("----------------------------------------")
            s=float(input("Side(s) : "))
            Square=s*s
            print("Area(A) : {}cm^2". format(Square))
            time.sleep(3)
            area2D()
        elif option=='2':
            print("----------------------------------------")
            l=float(input("Length(l) : "))
            w=float(input("Width(w) : "))
            Rectangle=l*w
            print("Area(A) : {}cm^2". format(Rectangle))
            time.sleep(3)
            area2D()
        elif option=='3':
            print("----------------------------------------")
            b=float(input("Base(a) : "))
            h=float(input("Height(b) : "))
            Triangle=b*h/2
            print("Area(A) : {}cm^2". format(Triangle))
            time.sleep(3)
            area2D()
        elif option=='4':
            print("----------------------------------------")
            print("π=?")
            print("1.π=22/7")
            print("2.π=3.14")
            print("3.π=3.141592653589793")
            option = input("Input : ")
            while option!='1' and option!='2' and option!='3':
                option = input("Input : ")
            if option =='1':
                pi=22/7
            elif option =='2':
                pi=3.14
            elif option =='3':
                pi=3.141592653589793
            r=float(input("Radius(r) : "))
            Circle=pi*r*r
            print("Area(A) : {}cm^2". format(Circle))
            time.sleep(3)
            area2D()
        elif option=='5':
            print("----------------------------------------")
            a=float(input("Side A(a) : "))
            b=float(input("Base(b) : "))
            h=float(input("Height(h) : "))
            Trapesium=(a+b)*h/2
            print("Area(A) : {}cm^2". format(Trapezium))
            time.sleep(3)
            area2D()
        elif option=='6':
            print("----------------------------------------")
            d1=float(input("Diagonal 1(d1) : "))
            d2=float(input("Diagonal 2(d2) : "))
            Diamond=d1*d2/2
            print("Area(A) : {}cm^2". format(Diamond))
            time.sleep(3)
            area2D()
        elif option=='7':
            print("----------------------------------------")
            b=float(input("Base(b) : "))
            h=float(input("Height(h) : "))
            Parallelogram=b*h
            print("Area(A) : {}cm^2". format(Parallelogram))
            time.sleep(3)
            area2D()
        elif option=='8':
            print("----------------------------------------")
            d1=float(input("Diagonal 1(d1) : "))
            d2=float(input("Diagonal 2(d2) : "))
            Kite=d1*d2/2
            print("Area(A) : {}cm^2". format(Kite))
            time.sleep(3)
            area2D()
        elif option=='9':
            print("----------------------------------------")
            print("π=?")
            print("1.π=22/7")
            print("2.π=3.14")
            print("3.π=3.141592653589793")
            option = input("Input : ")
            while option!='1' and option!='2' and option!='3':
                option = input("Input : ")
            if option =='1':
                pi=22/7
            elif option =='2':
                pi=3.14
            elif option =='3':
                pi=3.141592653589793
            r=float(input("Radius(r) : "))
            Circle=(1/2)*pi*r*r
            print("Area(A) : {}cm^2". format(Circle))
            time.sleep(3)
            area2D()
        elif option=='10':
            print("----------------------------------------")
            print("π=?")
            print("1.π=22/7")
            print("2.π=3.14")
            print("3.π=3.141592653589793")
            option = input("Input : ")
            while option!='1' and option!='2' and option!='3':
                option = input("Input : ")
            if option =='1':
                pi=22/7
            elif option =='2':
                pi=3.14
            elif option =='3':
                pi=3.141592653589793
            r=float(input("Radius(r) : "))
            Circle=(1/4)*pi*r*r
            print("Area(A) : {}cm^2". format(Circle))
            time.sleep(3)
            area2D()
        elif option=='11':
            print("----------------------------------------")
            print("π=?")
            print("1.π=22/7")
            print("2.π=3.14")
            print("3.π=3.141592653589793")
            option = input("Input : ")
            while option!='1' and option!='2' and option!='3':
                option = input("Input : ")
            if option =='1':
                pi=22/7
            elif option =='2':
                pi=3.14
            elif option =='3':
                pi=3.141592653589793
            r=float(input("Radius(r) : "))
            Circle=(3/4)*pi*r*r
            print("Area(A) : {}cm^2". format(Circle))
            time.sleep(3)
            area2D()
        elif option=='12':
            option2D()
        elif option=='13':
            geometryOption()
        elif option=='14':
            exit()
    def perimeter2D():
        print("----------------------------------------")
        print("Perimeter(P)")
        print()
        print("1.Square")
        print("2.Rectangle")
        print("3.Triangle")
        print("4.Circle")
        print("5.Trapesium")
        print("6.Diamond")
        print("7.Parallelogram")
        print("8.Kite")
        print("9.1/2_Circle")
        print("10.1/4_Circle")
        print("11.3/4_Circle")
        print("12.Back")
        print("13.Return to Geometry option")
        print("14.Quick exit")
        option=input("Input : ")
        while option!='1' and option!='2' and option!='3' and option!='4' and option!='5' and option!='6' and option!='7' and option!='8' and option!='9' and option!='10' and option!='11' and option!='12' and option!='13' and option!='14':
            option=input("Input : ")
        if option=='1':
            print("----------------------------------------")
            s=float(input("Side(s) : "))
            Square=4*s
            print("Perimeter(P) : {}cm". format(Square))
            time.sleep(3)
            perimeter2D()
        elif option=='2':
            print("----------------------------------------")
            l=float(input("length(l) : "))
            w=float(input("width(w) : "))
            Rectangle=2*(l*w)
            print("Perimeter(P) : {}cm". format(Rectangle))
            time.sleep(3)
            perimeter2D()
        elif option=='3':
            print("----------------------------------------")
            print("If a=?, Please type ''0''")
            a=float(input("Base(a) : "))
            if a==0:
                b=float(input("Height(b) : "))
                c=float(input("Hypotenuses(c) : "))
                a=sqrt((c**2)-(b**2))
                triangle=a+b+c
                print("Perimeter(P) : {}cm". format(triangle))
                time.sleep(3)
                perimeter2D()
            elif a>0:
                print("If b=?, Please type ''0''")
                b=float(input("Height(b) : "))
                if b==0:
                    c=float(input("Hypotenuses(c) : "))
                    b=sqrt((c**2)-(a**2))
                    triangle=a+b+c
                    print("Perimeter(P) : {}cm". format(triangle))
                    time.sleep(3)
                    perimeter2D()
                elif b>0:
                    c=sqrt((a**2)+(b**2))
                    triangle=a+b+c
                    print("Perimeter(P) : {}cm". format(triangle))
                    time.sleep(3)
                    perimeter2D()
        elif option=='4':
            print("----------------------------------------")
            print("π=?")
            print("1.π=22/7")
            print("2.π=3.14")
            print("3.π=3.141592653589793")
            option = input("Input : ")
            while option!='1' and option!='2' and option!='3':
                option = input("Input : ")
            if option =='1':
                pi=22/7
            elif option =='2':
                pi=3.14
            elif option =='3':
                pi=3.141592653589793
            r=float(input("Radius(r) : "))
            circle=pi*r*2
            print("Perimeter(P) : {}cm". format(circle))
            time.sleep(3)
            perimeter2D()
        elif option=='5':
            print("----------------------------------------")
            print("Rule : a<b")
            a=float(input("Side a(a) : "))
            b=float(input("Base(b) : "))
            print("If c=?, Please type ''0''")
            c=float(input("Hypotenuses(c) : "))
            if c>0:
                trapezium=((a+b)+(c*2))
                print("Perimeter(P) : {}cm". format(trapezium))
                time.sleep(3)
                perimeter2D()
            elif c==0:
                h=float(input("Height(h) : "))
                c=sqrt((((b-a)/2)*((b-a)/2))+(h*h))
                print("Hypotenuses(c) : {}cm". format(c))
                trapezium=((a+b)+(c*2))
                print("Perimeter(P) : {}cm". format(trapezium))
                time.sleep(3)
                perimeter2D()
        elif option=='6':
            print("----------------------------------------")
            d1=float(input("Diagonal 1(d1) : "))
            d2=float(input("Diagonal 2(d2) : "))
            c=sqrt(((d1/2)**2)+((d2/2)**2))
            diamond=4*c
            print("Hypotenuses(c) : {}cm". format(c))
            print("Perimeter(P) : {}cm". format(diamond))
        elif option=='7':
            print("----------------------------------------")
            b=float(input("Base(b) : "))
            c=float(input("hypotenuses(c) : "))
            parallelogram=2*(b+c)
            print("Perimeter(P) : {}cm". format(parallelogram))
            time.sleep(3)
            perimeter2D()
        elif option=='8':
            print("----------------------------------------")
            a=float(input("Side a(a) : "))
            b=float(input("Side b(b) : "))
            kite=2*(a+b)
            print("Perimeter(P) : {}cm". format(kite))
            time.sleep(3)
            perimeter2D()
        elif option=='9':
            print("----------------------------------------")
            print("π=?")
            print("1.π=22/7")
            print("2.π=3.14")
            print("3.π=3.141592653589793")
            option = input("Input : ")
            while option!='1' and option!='2' and option!='3':
                option = input("Input : ")
            if option =='1':
                pi=22/7
            elif option =='2':
                pi=3.14
            elif option =='3':
                pi=3.141592653589793
            r=float(input("Radius(r) : "))
            d=2*r
            circle=((1/2)*pi*d)+(d)
            print("Perimeter(P) : {}cm". format(circle))
            time.sleep(3)
            perimeter2D()
        elif option=='10':
            print("----------------------------------------")
            print("π=?")
            print("1.π=22/7")
            print("2.π=3.14")
            print("3.π=3.141592653589793")
            option = input("Input : ")
            while option!='1' and option!='2' and option!='3':
                option = input("Input : ")
            if option =='1':
                pi=22/7
            elif option =='2':
                pi=3.14
            elif option =='3':
                pi=3.141592653589793
            r=float(input("Radius(r) : "))
            d=2*r
            circle=((1/4)*pi*d)+(d)
            print("Perimeter(P) : {}cm". format(circle))
            time.sleep(3)
            perimeter2D()
        elif option=='11':
            print("----------------------------------------")
            print("π=?")
            print("1.π=22/7")
            print("2.π=3.14")
            print("3.π=3.141592653589793")
            option = input("Input : ")
            while option!='1' and option!='2' and option!='3':
                option = input("Input : ")
            if option =='1':
                pi=22/7
            elif option =='2':
                pi=3.14
            elif option =='3':
                pi=3.141592653589793
            r=float(input("Radius(r) : "))
            d=2*r
            circle=((3/4)*pi*d)+(d)
            print("Perimeter(P) : {}cm". format(circle))
            time.sleep(3)
            perimeter2D()
        elif option=='12':
            option2D()
        elif option=='13':
            geometryOption()
        elif option=='14':
            exit()
    def option2D():
        print("----------------------------------------")
        print("2D_Geometry")
        print()
        print("1.Area(A)")
        print("2.Perimeter(P)")
        print("3.Back")
        option=input("Input : ")
        while option!='1' and option!='2' and option!='3':
            option=input("Input : ")
        if option=='1':
            area2D()
        elif option=='2':
            perimeter2D()
        elif option=='3':
            geometryOption()
    def area3D():
        print("----------------------------------------")
        print("Area(A)")
        print()
        print("1.Cube")
        print("2.Rectangular_prism")
        print("3.Triangular_prism")
        print("4.Square_pyramid")
        print("5.Cylinder")
        print("6.Cone")
        print("7.Sphere")
        print("8.Back")
        print("9.Return to Geometry option")
        print("10.Quick exit")
        option=input("Input : ")
        while option!='1' and option!='2' and option!='3' and option!='4' and option!='5' and option!='6' and option!='7' and option!='8' and option!='9' and option!='10':
            option=input("Input : ")
        if option=='1':
            print("----------------------------------------")
            s=float(input("Side(s) : "))
            area=6*(s**2)
            print("Area(A) : {}cm^2". format(area))
            time.sleep(3)
            area3D()
        elif option=='2':
            print("----------------------------------------")
            l=float(input("Length(l) : "))
            w=float(input("Width(w) : "))
            h=float(input("Height(h) : "))
            area= 2*((l*h)+(l*w)+(w*l))
            print("Area(A) : {}cm^2". format(area))
            time.sleep(3)
            area3D()
        elif option=='3':
            print("----------------------------------------")
            a=float(input("Base side(a) : "))
            b=float(input("Base side(b) : "))
            c=float(input("Base side(c) :"))
            height=int(input("Base height of Horizontal side a : "))
            h=float(input("Height(h) : "))
            bArea=a*height/2
            area=(2*bArea)+((a+b+c)*h)
            print("Area(A) : {}cm^2". format(area))
            time.sleep(3)
            area3D()
        elif option=='4':
           print("----------------------------------------")
           print("If a=?, Please type ''0''")
           a=float(input("Base edge(a) : "))
           if a==0:
               h=float(input("Height(h) : "))
               l=float(input("Slant height(l) : "))
               a=2*(sqrt((l**2)-(h**2)))
               area=(a**2)+(2*a)*(sqrt(((a**2)/4)+(h**2)))
               print("Area(A) : {}cm^2". format(area))
               time.sleep(3)
               area3D()
           elif a>0:
                h=float(input("Height(h) : "))
                area=(a**2)+(2*a)*(sqrt(((a**2)/4)+(h**2)))
                print("Area(A) : {}cm^2". format(area))
                time.sleep(3)
                area3D()
        elif option=='5':
            print("----------------------------------------")
            print("π=?")
            print("1.π=22/7")
            print("2.π=3.14")
            print("3.π=3.141592653589793")
            option = input("Input : ")
            while option!='1' and option!='2' and option!='3':
                option = input("Input : ")
            if option =='1':
                pi=22/7
            elif option =='2':
                pi=3.14
            elif option =='3':
                pi=3.141592653589793
            r=float(input("Radius(r) : "))
            h=float(input("Height(h) : "))
            bArea=pi*r*r
            bPerimeter=2*pi*r
            area=(bArea*2)+(h*bPerimeter)
            print("Area(A) : {}cm^2". format(area))
            time.sleep(3)
            area3D()
        elif option=='6':
            print("----------------------------------------")
            print("π=?")
            print("1.π=22/7")
            print("2.π=3.14")
            print("3.π=3.141592653589793")
            option = input("Input : ")
            while option!='1' and option!='2' and option!='3':
                option = input("Input : ")
            if option =='1':
                pi=22/7
            elif option =='2':
                pi=3.14
            elif option =='3':
                pi=3.141592653589793
            print("If r=?, Please type ''0''")
            r=float(input("Radius(r) : "))
            if r==0:
                l=float(input("Slant height(l) : "))
                h=float(input("Height(h) : "))
                r=sqrt((l**2)-(h**2))
                area=pi*r*(r+l)
                print("Area(A) : {}cm^2". format(area))
                time.sleep(3)
                area3D()
            elif r>0:
                print("If l=?, Please type ''0''")
                l=float(input("Slant height(l) : "))
                if l==0:
                    h=float(input("Height(h) : "))
                    l=sqrt((r**2)+(l**2))
                    area=pi*r*(r+l)
                    print("Area(A) : {}cm^2". format(area))
                    time.sleep(3)
                    area3D()
                elif l>0:
                    area=pi*r*(r+l)
                    print("Area(A) : {}cm^2". format(area))
                    time.sleep(3)
                    area3D()
        elif option=='7':
            print("----------------------------------------")
            print("π=?")
            print("1.π=22/7")
            print("2.π=3.14")
            print("3.π=3.141592653589793")
            option = input("Input : ")
            while option!='1' and option!='2' and option!='3':
                option = input("Input : ")
            if option =='1':
                pi=22/7
            elif option =='2':
                pi=3.14
            elif option =='3':
                pi=3.141592653589793
            r=float(input("Radius(r) : "))
            area=4*pi*r*r
            print("Area(A) : {}cm^2". format(area))
            time.sleep(3)
            area3D()
        elif option=='8':
            option3D()
        elif option=='9':
            geometryOption()
        elif option=='10':
            exit()
    def volume3D():
        print("----------------------------------------")
        print("Volume(V)")
        print()
        print("1.Cube")
        print("2.Rectangular_prism")
        print("3.Triangular_prism")
        print("4.Square_pyramid")
        print("5.Triangular_pyramid")
        print("6.Cylinder")
        print("7.Cone")
        print("8.Sphere")
        print("9.Back")
        print("10.Return to Geometry option")
        print("11.Quick exit")
        option=input("Input : ")
        while option!='1' and option!='2' and option!='3' and option!='4' and option!='5' and option!='6' and option!='7' and option!='8' and option!='9' and option!='10' and option!='11':
            option=input("Input : ")
        if option=='1':
            print("----------------------------------------")
            s=float(input("Side(s) : "))
            v=s**3
            print("Volume(V) : {}cm^3". format(v))
            time.sleep(3)
            volume3D()
        elif option=='2':
            print("----------------------------------------")
            l=float(input("Length(l) : "))
            w=float(input("Width(w) : "))
            h=float(input("Height(h) : "))
            v=l*w*h
            print("Volume(V) : {}cm^3". format(v))
            time.sleep(3)
            volume3D()
        elif option=='3':
            print("----------------------------------------")
            a=float(input("Base(a) : "))
            b=float(input("Base(b): "))
            h=float(input("Triangular Prism Height(h) : "))
            area=a*b/2
            v=area*h
            print("Volume(V) : {}cm^3". format(v))
            time.sleep(3)
            volume3D()
        elif option=='4':
            print("----------------------------------------")
            s=float(input("Side(s) : "))
            h=float(input("Height(h) : "))
            v=(1/3)*(s**2)*h
            print("Volume(V) : {}cm^3". format(v))
            time.sleep(3)
            volume3D()
        elif option=='5':
            print("----------------------------------------")
            a=float(input("Base(a) : "))
            b=float(input("Base(b) : "))
            h=float(input("Triangular pyramid Height : "))
            area=a*b/2
            v=area*h/3
            print("Volume(V) : {}cm^3". format(v))
            time.sleep(3)
            volume3D()
        elif option=='6':
            print("----------------------------------------")
            print("π=?")
            print("1.π=22/7")
            print("2.π=3.14")
            print("3.π=3.141592653589793")
            option = input("Input : ")
            while option!='1' and option!='2' and option!='3':
                option = input("Input : ")
            if option =='1':
                pi=22/7
            elif option =='2':
                pi=3.14
            elif option =='3':
                pi=3.141592653589793
            r=float(input("Radius(r) : "))
            h=float(input("Height(h) : "))
            area=pi*(r**2)
            v=area*h
            print("Volume(V) : {}cm^3". format(v))
            time.sleep(3)
            volume3D()
        elif option=='7':
            print("----------------------------------------")
            print("π=?")
            print("1.π=22/7")
            print("2.π=3.14")
            print("3.π=3.141592653589793")
            option = input("Input : ")
            while option!='1' and option!='2' and option!='3':
                option = input("Input : ")
            if option =='1':
                pi=22/7
            elif option =='2':
                pi=3.14
            elif option =='3':
                pi=3.141592653589793
            print("If r=?, Please type ''0''")
            r=float(input("Radius(r) : "))
            if r==0:
                l=float(input("Slant height(l) : "))
                h=float(input("Height(h) : "))
                r=sqrt((l**2)-(h**2))
                bArea=pi*(r**2)
                v=bArea*h/3
                print("Volume(V) : {}cm^3". format(v))
                time.sleep(3)
                volume3D()
            elif r>0:
                print("if h=?, Please type '0'")
                h=float(input("Height(h) : "))
                if h==0:
                    c=float(input("Slant height(l) : "))
                    h=sqrt((r**2)+(c**2))
                    bArea=pi*(r**2)
                    v=bArea*h/3
                    print("Volume(V) : {}cm^3". format(v))
                    time.sleep(3)
                    volume3D()
                elif h>0:
                    bArea=pi*(r**2)
                    v=bArea*h/3
                    print("Volume(V) : {}cm^3". format(v))
                    time.sleep(3)
                    volume3D()
        elif option=='8':
            print("----------------------------------------")
            print("π=?")
            print("1.π=22/7")
            print("2.π=3.14")
            print("3.π=3.141592653589793")
            option = input("Input : ")
            while option!='1' and option!='2' and option!='3':
                option = input("Input : ")
            if option =='1':
                pi=22/7
            elif option =='2':
                pi=3.14
            elif option =='3':
                pi=3.141592653589793
            r=float(input("Radius(r) : "))
            v=(4/3)*pi*(r**3)
            print("Volume(V) : {}cm^3". format(v))
            time.sleep(3)
            volume3D()
        elif option=='9':
            option3D()
        elif option=='10':
            geometryOption()
        elif option=='11':
            exit()
    def option3D():
        print("----------------------------------------")
        print("3D_Geometry")
        print()
        print("1.Area(A)")
        print("2.Volume(V)")
        print("3.Back")
        option=input("Input : ")
        while option!='1' and option!='2' and option!='3':
            option=input("Input : ")
        if option=='1':
            area3D()
        elif option=='2':
            volume3D()
        elif option=='3':
            geometryOption()
    def geometryOption():
        print("----------------------------------------")
        print("Geometry")
        print()
        print("1.2D_Geometry")
        print("2.3D_Geometry")
        print("3.Back")
        option=input("Input : ")
        while option!='1' and option!='2' and option!='3':
            option=input("Input : ")
        if option=='1':
            option2D()
        elif option=='2':
            option3D()
        elif option=='3':
            optionMain()
    geometryOption()
def quadraticFormulaCalculator():
    print("----------------------------------------")
    print("ax^2+bx+c=0")
    a=float(input("a : "))
    b=float(input("b : "))
    c=float(input("c : "))
    xPlus=(-(b)+sqrt((b**2)-(4*a*c)))/(2*a)
    xMin=(-(b)-sqrt((b**2)-(4*a*c)))/(2*a)
    print("x1 : {}". format(xPlus))
    print("x2 : {}". format(xMin))
    time.sleep(3)
def optionMain():
    print("----------------------------------------")
    print("1.Geometry")
    print("2.Changelog")
    print("3.Quadratic formula calculator (x1∈ℤ, x2∈ℤ)")
    print("4.Exit")
    option=input("Input : ")
    while option!='1' and option!='2' and option!='3' and option!='4':
        option=input("Input : ")
    if option=='1':
        geometry()
    elif option=='2':
        changelog()
    elif option=='3':
        quadraticFormulaCalculator()
    elif option=='4':
        exit()
optionMain()

import sympy as sp
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import tkinter as tk
import random
import math

matplotlib.use('TkAgg')

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

end_x = 500

current_T = int(input("현재 온도 >>> "))
s = int(input("주변 온도 >>> "))
c = int(input("C >>> "))
k_ = list(map(int,input("k = ln?/? >>> ").split()))
k = math.log(k_[0]/k_[1])
print("k =",k)

def f(T):
    return k*(T - s)

#풀이
sol_t = np.arange(0,end_x+1)
sol_T = c*(math.e**(k*sol_t))+s

#수치해
h = 0.5

#오일러 방법
def Eul(current_T,end_x,h): 
    iteration = int(end_x*(1/h))+1
    print(iteration)
    
    D = 0

    t = np.linspace(0,end_x,iteration)
    print(t)
    T = np.array([])

    this_current_T = current_T

    for i in range(iteration):  
        this_current_T += D*h
        D = f(this_current_T)

        T = np.append(T,this_current_T)

    return t, T

#RK4 방법
def Rk4(current_T,end_x,h):
    iteration = int(end_x*(1/h))+1
    
    D = 0

    t = np.linspace(0,end_x,iteration)
    T = np.array([])

    this_current_T = current_T

    for i in range(iteration):
        this_current_T += D

        k1 = f(this_current_T)
        k2 = f(this_current_T+(1/2)*(k1*h))
        k3 = f(this_current_T+(1/2)*(k2*h))
        k4 = f(this_current_T+(k3*h))

        D = 1/6*(k1+2*k2+2*k3+k4)*h

        T = np.append(T,this_current_T)
    
    return t, T


def ShowGraph():
    Eul_result = Eul(current_T,end_x,h)
    Rk4_result = Rk4(current_T,end_x,h)

    plt.figure(figsize = (15,8))

    plt.subplot(231)
    plt.plot(sol_t,sol_T,color = 'g')
    plt.xlabel('시간')
    plt.ylabel('온도')
    plt.title("솔루션")

    plt.subplot(232)
    plt.plot(Eul_result[0],Eul_result[1],'.-',color='b')
    plt.xlabel('시간')
    plt.ylabel('온도')
    plt.title(f"오일러 방법 (간격:{h})")

    plt.subplot(233)
    plt.plot(Rk4_result[0],Rk4_result[1],'.-',color='r')
    plt.xlabel('시간')
    plt.ylabel('온도')
    plt.title(f"Rk4 방법 (간격:{h})")

    plt.subplot(235)
    plt.plot(sol_t,sol_T,color='g')
    plt.plot(Eul_result[0],Eul_result[1],color='b')
    plt.plot(Rk4_result[0],Rk4_result[1],color='r')
    plt.xlabel('시간')
    plt.ylabel('온도')
    plt.title("비교",loc='right')


    plt.subplots_adjust(wspace=0.5)

    plt.show()

#region 간격 입력 창
def click_button():
    global h

    h = float(entry.get())  

    ShowGraph()

window = tk.Tk()
window.title("간격 입력")
window.geometry("500x200")
color = ['#FF6347','#FFD700','#3CB371','#4682B4','#7B68EE']
window.configure(background=random.choice(color))
window.resizable(0,0)

currentfont = ("Courier", 16,"bold")

label = tk.Label(window,text="간격 입력",font=currentfont)
label.pack(pady=10)
entry = tk.Entry(window,font=currentfont,justify="center")
entry.pack(pady=10)
button = tk.Button(window,text="입력",command=click_button)
button.pack()

tk.mainloop()
#endregion

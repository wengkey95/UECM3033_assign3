import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def system(y,t,a,b): #predator-prey
    y0,y1 = y;
    dydt = [a*(y0-y0*y1),b*(-y1+y0*y1)];
    return dydt;
    
if __name__ == "__main__":
    a = 1;
    b = 0.2;
    y_initial = [0.1,1.0]; #initial condition y0 and y1
    t = np.linspace(0,5,200); # 0-5 , 200 patition
    sol = odeint(system,y_initial ,t,args=(a,b));
    
    #Graph of y0 and y1 against t
    #Initial Condition y0=0.1
    plt.plot(t,sol[:,0],label='y0(t)');
    plt.plot(t,sol[:,1],label='y1(t)');
    plt.title('Plot of y(t) against t with y0(0)=0.10');
    plt.xlabel('t');
    plt.ylabel('y(t)');
    plt.legend(loc='best');
    plt.grid();
    plt.show();

######################################
    #Graph of y0 and y1 against t
    #Initial condition y0=0.11
    y_initial_2 = [0.11, 1.0]
    sol_2 = odeint(system,y_initial ,t,args=(a,b));
    plt.plot(t,sol[:,0],label='y0(t)');
    plt.plot(t,sol[:,1],label='y1(t)');
    plt.title('Plot of y(t) against t with y0(0)=0.11');
    plt.xlabel('t');
    plt.ylabel('y(t)');
    plt.legend(loc='best');
    plt.grid();
    plt.show();
    
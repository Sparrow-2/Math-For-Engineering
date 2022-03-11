

from sympy import fourier_series, pi, plot
from sympy.abc import x

def Calc():
    function_Fourier = input("write down the function:  ")
    l = float(input("give l :  "))
    s = fourier_series(function_Fourier, (x, -l, l))



    s100 = s.truncate(n=100)
    print(s.sigma_approximation(100))
    p = plot(function_Fourier,s100, (x, -l, l), show=False, legend=True)
    p[0].line_color = 'b'
    p[0].label = 'function'

    p[1].line_color = 'red'
    p[1].label = 'of 100'


    p.show()

Calc()

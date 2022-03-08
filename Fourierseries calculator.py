import math

from sympy import fourier_series, pi, plot
from sympy.abc import x

def Calc():
    function_Fourier = input("write down the function")
    l = float(input("give l"))
    s = fourier_series(function_Fourier, (x, -l, l))
    s10 = s.truncate(n=10)


    s100 = s.truncate(n=250)
    p = plot(function_Fourier,s10,s100, (x, -l, l), show=False, legend=True)
    p[0].line_color = 'b'
    p[0].label = 'function'
    p[1].line_color = 'r'
    p[1].label = 'of 10'
    p[2].line_color = 'green'
    p[2].label = 'of 100'


    p.show()

Calc()

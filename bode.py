# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 17:07:14 2021

Programa simples para implementação do gráfico de bode de
função de transferência, cujos coeficientes devem ser determinados
nas variáveis num e den.

O programa utiliza as bibliotecas scipy e matplotlib.pyplot.

Ao rodar, é gerado o gráfico de bode para a função determinada

Se: G(s) = num/den

se num = [1,1] e den = [1,2]

Então G(s) =

s + 1
-----
s + 2


@author: mateusjaffer
"""

from scipy import signal
import matplotlib.pyplot as plt

num = [1]
den = [1,0,1,1]

sys = signal.TransferFunction(num, den)
w, mag, phase = signal.bode(sys)

plt.figure()
plt.subplot(1,2,1)
plt.semilogx(w, mag) 
plt.subplot(1,2,2)
plt.semilogx(w, phase)  # Bode phase plot
plt.tight_layout()





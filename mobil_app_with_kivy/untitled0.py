# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 12:38:46 2021

@author: Menings
"""

import scipy.integrate as spi
import scipy.constants as cn
import numpy as np
import scipy.linalg as spl

# %% constanten
m_eff = 0.17
epsilon_inf = 6.2
epsilon_null = 9.2
opt_phonon_energy = 31.40  # in meV unsicher in welcher Einheit das sein soll
E_f = 0  # wie finde ich das heraus
E_c = 0   # wie finde ich das heraus
piezo_coeff = 2.283*1e-2
# %%

def mobility(T):
    """Final function"""
    mu = 348.2 * (fermi_integral()*T**0.5*(m_eff/cn.m_e)**1.5*z_l*\
                  (1/epsilon_inf - 1/epsilon_null))**(-1)*D_drei_halbe/dd
    return mu

def nu(T):
    return (E_f-E_c)/(cn.k*T)

def arg_fermi_integral(epsilon, nu):
    return epsilon**0.5 / (1+np.exp(epsilon-nu))

def fermi_integral(nu):
    return 2/np.sqrt(np.pi)*spi.quad(arg_fermi_integral, 0, np.inf, args=(nu))[0]

def z_l(T):
    return opt_phonon_energy / (cn.k * T)

def x(E, T):
    return E/(cn.k * T)

def derivative_fermi_dist(E, T):
    return -1/(cn.k*T) * np.exp((E-E_f)/cn.k*T) / (1+np.exp((E-E_f)/cn.k*T))**2

# %%
def epsilon_1():
    pass

def a():
    pass

def F(b):
    return np.log(1+b)-(b/ (1+b))
# %%
def 1_tau_accoust(E, T):
    return 4.16*1e19* (T*m_eff/cn.m_e)**(1.5)*epsilon_1**2*x(E, T)**0.5 # epsilon_1 fehlt

def 1_tau_piezo(E, T):
    return 1.052*1e7*piezo_coeff*(T/x(E, T)*m_eff/cn.m_e)

def 1_tau_ion_imp():
    return 2.415(N_i/epsilon_0**2) * ((m_eff/cn.m_e)*(x(E, T)*T)**3)**(-0.5)*F(4*x(E, T)/a)

# %% calculate L
def L_opt(C):
    pass

def L_elast(C, A):
    return C/A * (1_tau_accoust + 1_tau_piezo +1_tau_ion_imp)

def L(c):
    return L_opt(C) +L_elast(C, A)
def l_of_phi():
    pass
# %%
def integrant_d_rs(E, r, s, l_of_phi, T):
    return E**r * l_of_phi * derivative_fermi_dist(E, T)

def d_rs(r, s, l_of_phi, T):
    return spi.quad(integrant_d_rs, 0, np.inf, args=(r, s, l_of_phi, T))

def integrant_alpha_rn(E, r, n, T):
    return E**n * E**r * derivative_fermi_dist(E, T)

def alpha_rn(r, n, T):  # runtimewarning and returns nan
    return spi.quad(integrant_alpha_rn, 0, np.inf, args=(r, n, T))[0]

def D_drei_halbe(dim, T):  # sollte so mit der Reihenfolge passen, aber nicht ganz sicher
    matrix = [[0]]
    for i in range(1, dim):
        matrix[0].append(alpha_rn(i, 3/2, T))
    for i in range(1, dim):
        matrix.append([])
        matrix[i].append(alpha_rn(i-1, 3/2, T))
        for j in range(1, dim):
            matrix[i].append(d_rs(i-1, j-1, l_of_phi, T))
    return spl.det(np.array(matrix))


def dd(dim, T):  # sollte so mit der Reihenfolge passen, aber nicht ganz sicher
    matrix = []
    for i in range(dim):
        matrix.append([])
        for j in range(dim):
            matrix[i].append(d_rs(i, j, l_of_phi, T))
    return spl.det(np.array(matrix))
# %%

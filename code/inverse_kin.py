from casadi import *
from direct_kin import directf
import numpy as np
import matplotlib.pyplot as plt
opti = Opti()

q_1 =opti.variable();q_2 =opti.variable();q_3 =opti.variable();


opti.set_initial(q_1,-30.91);opti.set_initial(q_2,-52.42);opti.set_initial(q_3,-72.68)

theta = [0.1135446771428052, 0.1552258044760527, 0.14380575473898485, -0.375]


f = directf(np.array([q_1,q_2,q_3]),theta)


p_desire = np.array([-0.3100309371948242, 0.19369974732398987, -0.036061882972717285])

opti.minimize(np.sqrt((p_desire[0]-f[0])**2+(p_desire[1]-f[1])**2+(p_desire[2]-f[2])**2))
opti.solver('ipopt');
sol = opti.solve()

print([sol.value(q_1),sol.value(q_2),sol.value(q_3)])

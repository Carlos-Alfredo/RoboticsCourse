from casadi import *
import numpy as np

def directf(Q,theta):
	q_1 = Q[0]*np.pi/180;q_2=Q[1]*np.pi/180;q_3=Q[2]*np.pi/180
	l1 = theta[0];l2 = theta[1];l3 = theta[2]
	'''
	f_1 = theta[3]
	f_2 = l1*np.sin(q_1)+l2*np.sin(q_1+q_2)+l3*np.sin(q_1+q_2+q_3);
	f_3 = l1*np.cos(q_1)+l2*np.cos(q_1+q_2)+l3*np.cos(q_1+q_2+q_3);
	'''
	f_1 = - (l1*np.cos(q_1)+l2*np.cos(q_1+q_2)+l3*np.cos(q_1+q_2+q_3))
 	f_2 = l1*np.sin(q_1)+l2*np.sin(q_1+q_2)+l3*np.sin(q_1+q_2+q_3)
	f_3 = 0
	f = f_1;f = vertcat(f,f_2);f = vertcat(f,f_3);return f

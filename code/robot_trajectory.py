import sim
import time
import math
import numpy as np
from Robot_FW import Robot_FW
clientID = sim.simxStart('127.0.0.1',19999,True,True,5000,5);
if clientID!=0:
	print('Conexão com problema')	
else:

	Robot = Robot_FW(clientID,'rollingJoint')


	res_1, cuboid0Handle=sim.simxGetObjectHandle(clientID,"Cuboid",sim.simx_opmode_blocking)
	res_2, sensorHandle = sim.simxGetObjectHandle(clientID,"sensor_1",sim.simx_opmode_blocking)
	#res_3, MajorJoint = sim.simxGetObjectHandle(clientID,"slippingJoint_rl",sim.simx_opmode_blocking)
	print(res_1)
	#res, YouBotHandle=sim.simxGetObjectHandle(clientID,"youBot",sim.simx_opmode_blocking)

	count = 1
	r=sim.simxReadProximitySensor(clientID,sensorHandle,sim.simx_opmode_streaming)
	r=sim.simxReadProximitySensor(clientID,sensorHandle,sim.simx_opmode_buffer)
	rC,cuboid_position = sim.simxGetObjectPosition(clientID, cuboid0Handle,Robot.joint2,sim.simx_opmode_streaming)
	rC,cuboid_position = sim.simxGetObjectPosition(clientID, cuboid0Handle,Robot.joint2,sim.simx_opmode_buffer)
	print(cuboid_position)
	#while True: 
		#rC,value_1 = sim.simxGetObjectPosition(clientID, Robot.joint1,  Robot.joint2, sim.simx_opmode_blocking)
		#rC,value_2 = sim.simxGetObjectPosition(clientID, Robot.joint2,  Robot.joint3, sim.simx_opmode_blocking)
		#rC,value_3 = sim.simxGetObjectPosition(clientID, Robot.joint3,  Robot.joint4, sim.simx_opmode_blocking)
		#rC,value_4 = sim.simxGetObjectPosition(clientID, Robot.joint4,  Robot.joint5, sim.simx_opmode_blocking)
		#rC,value_5 = sim.simxGetObjectPosition(clientID, cuboid0Handle, Robot.joint2, sim.simx_opmode_blocking)
		#print(f"Cube Position: {value_5}")
		#print([np.linalg.norm(value_1),np.linalg.norm(value_2),np.linalg.norm(value_3),np.linalg.norm(value_4)])
	while True:
		Robot.velocity(np.array([-60,-60,-60,-60])*np.pi/180)
		r=sim.simxReadProximitySensor(clientID,sensorHandle,sim.simx_opmode_blocking)
		if(np.linalg.norm(r[2])<0.2):
			while True:
				rC,cuboid_position = sim.simxGetObjectPosition(clientID, cuboid0Handle, Robot.joint2, sim.simx_opmode_blocking)
				print(cuboid_position)
				Robot.velocity(np.array([0,0,0,0])*np.pi/180)
				#Robot.arm_position(np.array([0,-70.886157787814092,-52.38592260080107,-72.68037262999398])*np.pi/180)
				Robot.arm_position(np.array([0,-115.67655373847052, -149.4394315134703, -15.442846468701372])*np.pi/180)
				rC,cuboid_position = sim.simxGetObjectPosition(clientID, cuboid0Handle, Robot.joint2, sim.simx_opmode_blocking)
				print(cuboid_position)
				#Robot.Adjust_grip()
				



#sim.simxSetJointTargetVelocity(clientID,MajorJoint,60*np.pi/180,sim.simx_opmode_oneshot)
#time.sleep(10)
"""
count =0
while True:	
	#returnCode,cuboid_position =  sim.simxGetObjectPosition(clientID,cuboid0Handle,-1,sim.simx_opmode_streaming)
	#returnCode,robot_position  =  sim.simxGetObjectPosition(clientID,YouBotHandle,-1,sim.simx_opmode_streaming)
	#returnCode,position = sim.simxReadProximitySensor(clientID,sensorHandle,sim.simx_opmode_streaming) 
	
	
	
	print(f"ROBOT_ POSITION: {r[2]}")
	if(np.linalg.norm(r[2])<0.2):
		
		break
"""
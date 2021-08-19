import sim

class Robot_FW():
	def __init__(self,clientID,RobotName):
		self.clientID = clientID
		returnCode1,self.joint1 = sim.simxGetObjectHandle(clientID,'YBAJ0',sim.simx_opmode_blocking)
		returnCode2,self.joint2 = sim.simxGetObjectHandle(clientID,'YBAJ1',sim.simx_opmode_blocking)
		returnCode3,self.joint3 = sim.simxGetObjectHandle(clientID,'YBAJ2',sim.simx_opmode_blocking)
		returnCode4,self.joint4 = sim.simxGetObjectHandle(clientID,'YBAJ3',sim.simx_opmode_blocking)
		returnCode5,self.joint5 = sim.simxGetObjectHandle(clientID,'YBAJ4',sim.simx_opmode_blocking)
		returnCode5,self.gjoint1 = sim.simxGetObjectHandle(clientID,'youBotGripperJoint1',sim.simx_opmode_blocking)	
		returnCode5,self.gjoint2 = sim.simxGetObjectHandle(clientID,'youBotGripperJoint2',sim.simx_opmode_blocking)	
		
		returnCode6,self.eixo_rl = sim.simxGetObjectHandle(clientID,f'{RobotName}_rl',sim.simx_opmode_blocking)
		returnCode7,self.eixo_rr = sim.simxGetObjectHandle(clientID,f'{RobotName}_rr',sim.simx_opmode_blocking)
		returnCode8,self.eixo_fl = sim.simxGetObjectHandle(clientID,f'{RobotName}_fl',sim.simx_opmode_blocking)
		returnCode9,self.eixo_fr = sim.simxGetObjectHandle(clientID,f'{RobotName}_fr',sim.simx_opmode_blocking)
		

		print([returnCode1,returnCode2,returnCode3,returnCode4,
			  returnCode6,returnCode7,returnCode8,returnCode9])
	
	def velocity(self,v):
		[rl,rr,fl,fr]=v
		
		sim.simxPauseCommunication(self.clientID,True)

		sim.simxSetJointTargetVelocity(self.clientID, self.eixo_rl,
										   rl,sim.simx_opmode_oneshot)
		sim.simxSetJointTargetVelocity(self.clientID, self.eixo_rr, 
                                            rr,sim.simx_opmode_oneshot)
		sim.simxSetJointTargetVelocity(self.clientID, self.eixo_fl, 
                                            fl,sim.simx_opmode_oneshot)
		sim.simxSetJointTargetVelocity(self.clientID, self.eixo_fr, 
                                            fr,sim.simx_opmode_oneshot)
		sim.simxPauseCommunication(self.clientID,False)

	def arm_position(self,theta):
		[theta_1,theta_2,theta_3,theta_4]=theta

		sim.simxPauseCommunication(self.clientID,True)
		sim.simxSetJointTargetPosition(self.clientID,self.joint1,
									   theta_1,sim.simx_opmode_oneshot)
		sim.simxSetJointTargetPosition(self.clientID,self.joint2,theta_2,sim.simx_opmode_oneshot)
		sim.simxSetJointTargetPosition(self.clientID, 
                                        self.joint3,theta_3,sim.simx_opmode_oneshot)
		sim.simxSetJointTargetPosition(self.clientID, 
                                       self.joint4,theta_4,sim.simx_opmode_oneshot)
		sim.simxPauseCommunication(self.clientID,False)	
	def open_grip(self,x):
		if x :
			sim.simxSetJointTargetVelocity(self.clientID,self.gjoint2,-0.04,sim.simx_opmode_oneshot)
		else:
			sim.simxSetJointTargetVelocity(self.clientID,self.gjoint2,0.04,sim.simx_opmode_oneshot)
		returnCode,position=sim.simxGetJointPosition(self.clientID,self.gjoint2,sim.simx_opmode_streaming)
		sim.simxSetJointTargetPosition(self.clientID,self.gjoint1,position*-0.5,sim.simx_opmode_oneshot)

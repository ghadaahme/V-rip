import vrep 
import math
import sys
import tkinter

def dis_connect():
    vrep.simxFinish(-1) 
    print ("FINISH !!!!")
 ###############################################################################################################   
def connect():
    vrep.simxFinish(-1) 
    clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) 
    if clientID!=-1: 
        print ("Connected to remote API server") 
    else: 
        print("Not connected to remote API server") 
        sys.exit("Could not connect")
    
    
    err1,motor_handle1 = vrep.simxGetObjectHandle(clientID,"LBR4p_joint1", vrep.simx_opmode_blocking)
    err2,motor_handle2 = vrep.simxGetObjectHandle(clientID,"LBR4p_joint2", vrep.simx_opmode_blocking)
    err3,motor_handle3 = vrep.simxGetObjectHandle(clientID,"LBR4p_joint3", vrep.simx_opmode_blocking)
    err4,motor_handle4 = vrep.simxGetObjectHandle(clientID,"LBR4p_joint4", vrep.simx_opmode_blocking)
    err5,motor_handle5 = vrep.simxGetObjectHandle(clientID,"LBR4p_joint5", vrep.simx_opmode_blocking)
    err6,motor_handle6 = vrep.simxGetObjectHandle(clientID,"LBR4p_joint6", vrep.simx_opmode_blocking)
    err7,motor_handle7 = vrep.simxGetObjectHandle(clientID,"LBR4p_joint7", vrep.simx_opmode_blocking)
########################################
    j1=vrep.simxGetJointPosition(clientID,motor_handle1, vrep.simx_opmode_blocking);
    j2=vrep.simxGetJointPosition(clientID,motor_handle2, vrep.simx_opmode_blocking);
    j3=vrep.simxGetJointPosition(clientID,motor_handle3, vrep.simx_opmode_blocking);
    j4=vrep.simxGetJointPosition(clientID,motor_handle4, vrep.simx_opmode_blocking);
    j5=vrep.simxGetJointPosition(clientID,motor_handle5, vrep.simx_opmode_blocking);
    j6=vrep.simxGetJointPosition(clientID,motor_handle6, vrep.simx_opmode_blocking);
    j7=vrep.simxGetJointPosition(clientID,motor_handle7, vrep.simx_opmode_blocking);
############################################################
    s[0].set(j1[1]*180/math.pi)
    s[1].set(j2[1]*180/math.pi)
    s[2].set(j3[1]*180/math.pi)
    s[3].set(j4[1]*180/math.pi)
    s[4].set(j5[1]*180/math.pi)
    s[5].set(j6[1]*180/math.pi)
    s[6].set(j7[1]*180/math.pi)
    #################################################
    while(1):
        targetPos1=[s[0].get()*math.pi/180,s[1].get()*math.pi/180,s[2].get()*math.pi/180,s[3].get()*math.pi/180,s[4].get()*math.pi/180,s[5].get()*math.pi/180,s[6].get()*math.pi/180]
        vrep.simxSetJointTargetPosition(clientID, motor_handle1, targetPos1[0],  vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID, motor_handle2, targetPos1[1],  vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID, motor_handle3, targetPos1[2],  vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID, motor_handle4, targetPos1[3],  vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID, motor_handle5, targetPos1[4],  vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID, motor_handle6, targetPos1[5],  vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID, motor_handle7, targetPos1[6],  vrep.simx_opmode_streaming)
        master.update_idletasks()
        master.update()
####################################################################################################################

master = tkinter.Tk()

s = [0,0,0,0,0,0,0]
s[0] = tkinter.Scale(master, from_=-180, to=180, orient=tkinter.VERTICAL ,label="J1")
s[0].pack(side=tkinter.LEFT)
s[1] = tkinter.Scale(master, from_=-180, to=180, orient=tkinter.VERTICAL,label="J2")
s[1].pack(side=tkinter.LEFT)
s[2] = tkinter.Scale(master, from_=-180, to=180, orient=tkinter.VERTICAL,label="J3")
s[2].pack(side=tkinter.LEFT)
s[3] = tkinter.Scale(master, from_=-180, to=180, orient=tkinter.VERTICAL,label="J4")
s[3].pack(side=tkinter.LEFT)
s[4] = tkinter.Scale(master, from_=-180, to=180, orient=tkinter.VERTICAL,label="J5")
s[4].pack(side=tkinter.LEFT)
s[5] = tkinter.Scale(master, from_=-180, to=180, orient=tkinter.VERTICAL,label="J6")
s[5].pack(side=tkinter.LEFT)
s[6] = tkinter.Scale(master, from_=-180, to=180, orient=tkinter.VERTICAL,label="J7")
s[6].pack(side=tkinter.LEFT)
#################################################
dis_connect = tkinter.Button(master, text="DISCONNECT", command=dis_connect)
dis_connect.pack(side=tkinter.BOTTOM)
dis_connect.pack(side=tkinter.RIGHT)
connect = tkinter.Button(master, text="CONNECT", command=connect)
connect.pack(side=tkinter.TOP)
connect.pack(side=tkinter.RIGHT)
##########################
master.mainloop()

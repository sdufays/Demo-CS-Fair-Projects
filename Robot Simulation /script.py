#!/usr/bin/env python

import sys
import rospy
from gazebo_msgs.srv import *
from geometry_msgs.msg import Pose
import tf
import pandas as pd

data = {'name': ['Gripper 1', 'Gripper 2', 'Gripper 3', 'Gripper 4', 'Gripper 5']}
df1 = pd.DataFrame(data)

def raise_arms(coef):
  try:
    set_force=rospy.ServiceProxy("/gazebo/apply_joint_effort", ApplyJointEffort)
    
    time=rospy.Time()
    duration=rospy.Duration.from_sec(-1)
    
    # Raise all robots arms
    res=set_force("simple_manipulator1::arm_gripper_joint", coef * 200.0, time, duration)
    res=set_force("simple_manipulator2::arm_gripper_joint", coef * 200.0, time, duration)
    res=set_force("simple_manipulator3::arm_gripper_joint", coef * 200.0, time, duration)
    res=set_force("simple_manipulator4::forearm_arm_joint", coef * 200.0, time, duration)
    res=set_force("simple_manipulator5::forearm_arm_joint", coef * 200.0, time, duration)

    

  except rospy.ServiceException as e:
    print ("Service call failed %s"%e)



def open_grippers(coef):
  try:
    set_force=rospy.ServiceProxy("/gazebo/apply_joint_effort", ApplyJointEffort)
    
    
    time=rospy.Time()
    duration=rospy.Duration.from_sec(-1)
    
    
    # Open all grippers
    # Manipulator1
    res=set_force("simple_manipulator1::simple_gripper1::palm_left_finger", coef * 5, time, duration)
    res=set_force("simple_manipulator1::simple_gripper1::palm_right_finger", coef * -5, time, duration)
    res=set_force("simple_manipulator1::simple_gripper1::left_finger_tip_joint", coef * 2.5, time, duration)
    res=set_force("simple_manipulator1::simple_gripper1::right_finger_tip_joint", coef * -2.5, time, duration)
    
    # Manipulator2
    res=set_force("simple_manipulator2::simple_gripper2::palm_left_finger", coef * 10.0, time, duration)
    res=set_force("simple_manipulator2::simple_gripper2::palm_right_finger", coef * -10.0, time, duration)
    res=set_force("simple_manipulator2::simple_gripper2::left_finger_tip_joint", coef * 5.0, time, duration)
    res=set_force("simple_manipulator2::simple_gripper2::right_finger_tip_joint", coef * -5.0, time, duration)
    
    # Manipulator3
    res=set_force("simple_manipulator3::simple_gripper3::palm_left_finger", coef * 10.0, time, duration)
    res=set_force("simple_manipulator3::simple_gripper3::palm_right_finger", coef * -10.0, time, duration)
    res=set_force("simple_manipulator3::simple_gripper3::left_finger_tip_joint", coef * 5.0, time, duration)
    res=set_force("simple_manipulator3::simple_gripper3::right_finger_tip_joint", coef * -5.0, time, duration)
    res=set_force("simple_manipulator3::simple_gripper3::palm_front_finger", coef * -20.0, time, duration)
    res=set_force("simple_manipulator3::simple_gripper3::palm_rear_finger", coef * 20.0, time, duration)
    res=set_force("simple_manipulator3::simple_gripper3::front_finger_tip_joint", coef * -10.0, time, duration)
    res=set_force("simple_manipulator3::simple_gripper3::rear_finger_tip_joint", coef * 10.0, time, duration)
    
    
   # Manipulator4
    res=set_force("simple_manipulator4::pr2_gripper_simplified::r_gripper_l_finger_joint", coef * 0.65, time, duration)
    res=set_force("simple_manipulator4::pr2_gripper_simplified::r_gripper_r_finger_joint", coef * 0.6, time, duration)
    
    # Manipulator5
    res=set_force("simple_manipulator5::irobot_hand::finger0/joint_base", coef * -1.0, time, duration)
    res=set_force("simple_manipulator5::irobot_hand::finger1/joint_base", coef * -1.0, time, duration)
    res=set_force("simple_manipulator5::irobot_hand::finger2/joint_base", coef * -1.75, time, duration)
    res=set_force("simple_manipulator5::irobot_hand::finger0/joint_base_rotation", coef * -1.0, time, duration)
    res=set_force("simple_manipulator5::irobot_hand::finger1/joint_base_rotation", coef * -1.0, time, duration)
    res=set_force("simple_manipulator5::irobot_hand::finger0/joint_tip", coef * -1.0, time, duration)
    res=set_force("simple_manipulator5::irobot_hand::finger1/joint_tip", coef * -1.0, time, duration)
    res=set_force("simple_manipulator5::irobot_hand::finger2/joint_tip", coef * 1.25, time, duration)


    
  
  except rospy.ServiceException as e:
    print ("Service call failed %s"%e)
    
    
def spawn_object(object_name,data_name, x, y, z, roll, pitch, yaw, diff_SIM1, diff_SIM2, diff_SIM3, diff_SIM4, diff_SIM5, extra_time):
  try:
    spawn_object=rospy.ServiceProxy("/gazebo/spawn_sdf_model", SpawnModel)
    
    # get model
    f = open('/home/user_adm/.gazebo/models/' + object_name + '/model.sdf','r')
    sdff = f.read()
    
    # define pose
    pose=Pose()
    pose.position.x=x
    pose.position.y=y
    pose.position.z=z

    quaternion = tf.transformations.quaternion_from_euler(roll, pitch, yaw)

    pose.orientation.x = quaternion[0]
    pose.orientation.y = quaternion[1]
    pose.orientation.z = quaternion[2]
    pose.orientation.w = quaternion[3]
    
    
    # Spawn object
   
    pose.position.x = x + diff_SIM1
    pose.position.y = 4
    
    res=spawn_object(object_name + "1", sdff, "", pose, "")
    
    pose.position.x = x + diff_SIM2
    pose.position.y = 2
    
    res=spawn_object(object_name + "2", sdff, "", pose, "")
    
    pose.position.x = x + diff_SIM3
    pose.position.y = 0
    
    res=spawn_object(object_name + "3", sdff, "", pose, "")
    
    pose.position.x = x + diff_SIM4
    pose.position.y = -2
    
    res=spawn_object(object_name + "4", sdff, "", pose, "")
    
    pose.position.x = x + diff_SIM5
    pose.position.y = -4
    
    res=spawn_object(object_name + "5", sdff, "", pose, "")
    
    
  except rospy.ServiceException as e:
    print ("Service call failed %s"%e)


def delete_object(object_name):
  try:
    delete_object=rospy.ServiceProxy("/gazebo/delete_model", DeleteModel)
    
   
    # Delete object
    res=delete_object(object_name + "1")
    res=delete_object(object_name + "2")
    res=delete_object(object_name + "3")
    res=delete_object(object_name + "4")
    res=delete_object(object_name + "5")
    
  except rospy.ServiceException as e:
    print ("Service call failed %s"%e)
    
def collect_result(object_name,data_name,df):
    
    df.insert(1, data_name, ["F", "F", "F", "F", "F"], True)
    
    get_model=rospy.ServiceProxy("/gazebo/get_model_state", GetModelState)
    
    res = get_model(object_name + "1", "")
    if res.pose.position.z > 0.1 :
      df.at[0, data_name] = "T"    

    res = get_model(object_name + "2", "")
    if res.pose.position.z > 0.1 :
      df.at[1, data_name] = "T"
    
    res = get_model(object_name + "3", "")
    if res.pose.position.z > 0.1 :
      df.at[2, data_name] = "T"
    
    res = get_model(object_name + "4", "")
    if res.pose.position.z > 0.1 :
      df.at[3, data_name] = "T"
    
    res = get_model(object_name + "5", "")
    if res.pose.position.z > 0.1 :
      df.at[4, data_name] = "T"
    
    print("\n")
    print(df)
    print("\n")
      

    
   
def test_object(object_name, data_name, x, y, z, roll, pitch, yaw, diff_SIM1, diff_SIM2, diff_SIM3, diff_SIM4, diff_SIM5, extra_time):

  raise_arms(1.0)
  open_grippers(1.0)
  
  rospy.sleep(2.0)
  
  # spawn object
  spawn_object(object_name, data_name, x, y, z, roll, pitch, yaw, diff_SIM1, diff_SIM2, diff_SIM3, diff_SIM4, diff_SIM5, extra_time)
  
  # Go down to gripp
  raise_arms(-1.0)
  
  rospy.sleep(2.0 + extra_time)
  
  # grip object
  open_grippers(-3.0)
  
  rospy.sleep(2.0)
  
  # raise arm
  raise_arms(1.0)
  
  rospy.sleep(3.0 + extra_time/2)
  
  # collect object position
  collect_result(object_name,data_name,df1)
  
  rospy.sleep(2.0)
  
  # Remove object
  delete_object(object_name)
  
  # Release forces
  open_grippers(2.0)
  
  raise_arms(-1.0)
  
  
    
if __name__=="__main__":
  rospy.wait_for_service("/gazebo/apply_joint_effort")
  rospy.wait_for_service("/gazebo/spawn_sdf_model")
  rospy.wait_for_service("/gazebo/delete_model")
  rospy.wait_for_service("/gazebo/get_model_state")
  
  test_object("wood_cube_5cm","Wooden box", 0.74, 0, 0, 0, 0, 0, 0.06, 0, 0, -0.04, 0,0)
  test_object("Screw", "Screw",0.74, 0, 0, 0, -1.5708, 0, 0.05, 0.0, 0, -0.025, 0,0)
  test_object("beer", "Beer", 0.74, 0, 0, 0, 0, 0, 0.05, -0.012, 0, -0.02, -0.01,0)
  test_object("nut", "Upright Nut", 0.74, 0, 0, 0, 0, 1.5708, 0.10, 0.000, 0, 0,0.01,0)
  test_object("Wheel", "Wheel",0.73, 0, 0, 0, 0, 0, 0.03, 0, 0, -0.02, 0,5.5)
  test_object("Bulb","Bulb", 0.74, 0, 0, 1.5708, 0, 0, 0.05, -0.005, 0, 0.02, 0,0)
  test_object("Mug", "Mug",0.73, 0, 0, 0, 0, 1.5708, 0.05, -0.005, 0.03, -0.005, 0,3.5)

  test_object("nose_drone", "Drone Nose", 0.74, 0, 0, 0, 0, 0, 0.13, -0.01, 0, -0.02, 0,4.5)








  


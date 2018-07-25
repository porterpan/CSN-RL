import numpy as np
import gym
import json


from scipy.interpolate import interp1d
from matplotlib import pyplot
from matplotlib.ticker import FuncFormatter
from keras.models import model_from_json


### PlaneBall: DQN, DDPG, DPPO comparison

# history 1: DQN
with open('/home/shengnan/Thesis-RL/DQN/PlaneBall/save/history8_2018-06-25 19:14:36', 'r') as f:
    pp1_1 = json.load(f)
    f.close()
with open('/home/shengnan/Thesis-RL/DQN/PlaneBall/save/history8_2018-06-26 09:17:52', 'r') as f:
    pp1_2 = json.load(f)
    f.close()
with open('/home/shengnan/Thesis-RL/DQN/PlaneBall/save/history8_2018-06-26 09:19:07', 'r') as f:
    pp1_3 = json.load(f)
    f.close()



# history 2: DDPG
with open('/home/shengnan/Thesis-RL/DDPG/PlaneBall/save/history1_2018-07-17 23:11:25', 'r') as f:
    pp2_1 = json.load(f)
    f.close()

with open('/home/shengnan/Thesis-RL/DDPG/PlaneBall/save/history1_2018-07-18 00:11:06', 'r') as f:
    pp2_2 = json.load(f)
    f.close()

with open('/home/shengnan/Thesis-RL/DDPG/PlaneBall/save/history1_2018-07-18 00:11:13', 'r') as f:
    pp2_3 = json.load(f)
    f.close()


# history 3: DPPO
with open('/home/shengnan/Thesis-RL/PPO/PlaneBall/save/history2_2018-07-25 10:03:33', 'r') as f:
    pp3_1 = json.load(f)
    f.close()

with open('/home/shengnan/Thesis-RL/PPO/PlaneBall/save/history2_2018-07-25 10:09:08', 'r') as f:
    pp3_2 = json.load(f)
    f.close()

with open('/home/shengnan/Thesis-RL/PPO/PlaneBall/save/history2_2018-07-25 10:14:34', 'r') as f:
    pp3_3 = json.load(f)
    f.close()

#with open('save/history3_2018-07-17 15:28:27', 'r') as f:
#    pp3_4 = json.load(f)
#    f.close()

#with open('save/history3_2018-07-17 15:28:35', 'r') as f:
#    pp3_5 = json.load(f)
#    f.close()



duration1 = (sum(pp1_1['duration'])+sum(pp1_2['duration'])+sum(pp1_3['duration']))/3
duration2 = (sum(pp2_1['duration'])+sum(pp2_2['duration'])+sum(pp2_3['duration']))/3
#duration3 = (sum(pp3_1['duration'])+sum(pp3_2['duration'])+sum(pp3_3['duration']))/3
duration3 = (pp3_1['duration_total']+pp3_2['duration_total']+pp3_3['duration_total'])/3#duration4 = (sum(pp4_1['duration'])+sum(pp4_2['duration'])+sum(pp4_3['duration']))/3
#duration5 = (sum(pp5_1['duration'])+sum(pp5_2['duration'])+sum(pp5_3['duration']))/3






  ### kind: 'linear’, ‘nearest’, ‘zero’, ‘slinear’, ‘quadratic, ‘cubic’
x = np.linspace(2000, 499000, num=500000)

f1_1 = (interp1d(pp1_1['nb_steps'], pp1_1['episode_reward']))(x)
f1_2 = (interp1d(pp1_2['nb_steps'], pp1_2['episode_reward']))(x)
f1_3 = (interp1d(pp1_3['nb_steps'], pp1_3['episode_reward']))(x)
exp1 = np.vstack((f1_1, f1_2, f1_3))
f_avg1 = np.average(exp1, axis=0)



f2_1 = (interp1d(pp2_1['nb_steps'], pp2_1['episode_reward']))(x)
f2_2 = (interp1d(pp2_2['nb_steps'], pp2_2['episode_reward']))(x)
f2_3 = (interp1d(pp2_3['nb_steps'], pp2_3['episode_reward']))(x)
exp2 = np.vstack((f2_1, f2_2, f2_3))
f_avg2 = np.average(exp2, axis=0)



f3_1 = (interp1d(pp3_1['steps'], pp3_1['reward']))(x)
f3_2 = (interp1d(pp3_2['steps'], pp3_2['reward']))(x)
f3_3 = (interp1d(pp3_3['steps'], pp3_3['reward']))(x)
exp3 = np.vstack((f3_1, f3_2, f3_3))
f_avg3 = np.average(exp3, axis=0)

'''
f4_1 = (interp1d(pp4_1['nb_steps'], pp4_1['episode_reward']))(x)
f4_2 = (interp1d(pp4_2['nb_steps'], pp4_2['episode_reward']))(x)
f4_3 = (interp1d(pp4_3['nb_steps'], pp4_3['episode_reward']))(x)
exp4 = np.vstack((f4_1, f4_2, f4_3))
f_avg4 = np.average(exp4, axis=0)


f5_1 = (interp1d(pp5_1['nb_steps'], pp5_1['episode_reward']))(x)
f5_2 = (interp1d(pp5_2['nb_steps'], pp5_2['episode_reward']))(x)
f5_3 = (interp1d(pp5_3['nb_steps'], pp5_3['episode_reward']))(x)
exp5 = np.vstack((f5_1, f5_2, f5_3))
f_avg5 = np.average(exp5, axis=0)

'''

pyplot.figure(num=1, figsize=(20, 10),)
pyplot.xlabel('total steps', fontsize=24)
pyplot.ylabel('rewards per episode', fontsize=24)
pyplot.title('PlaneBall: DQN, DDPG, DPPO comparison', fontsize=24)

pyplot.plot(f_avg1, 'red', label='DQN')
pyplot.plot(f_avg2, 'b', label='DDPG')
pyplot.plot(f_avg3, 'g', label='DPPO', alpha=0.7)
pyplot.legend()
pyplot.savefig('save/planeball_compare.png',bbox_inches='tight')


pyplot.figure(num=2, figsize=(8, 5),)
width = 0.2
x = np.arange(3)
duration_compare = [duration1,duration2,duration3]
fig, ax = pyplot.subplots()
rects1 = ax.bar(x, duration_compare, width)

pyplot.xticks(x, ('DQN', 'DDPG', 'DPPO'))
ax.set_ylabel('Duration')
ax.set_title('Training time')
pyplot.savefig('save/planeball_duration.png',bbox_inches='tight')


pyplot.show()
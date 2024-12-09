from crowd_nav.configs.config import ConfigNoArgs
from crowd_sim.envs import CrowdSim, CrowdSimVarNum, CrowdSimPred
from matplotlib.axes import Axes
import matplotlib.pyplot as plt

config = ConfigNoArgs()
config.sim.predict_method = 'const_vel'

env = CrowdSimPred()
env.configure(config)
env.thisSeed=0
env.nenv=1

fig, ax = plt.subplots(figsize=(7, 7))
ax.set_xlim(-10, 10) # 6
ax.set_ylim(-10, 10)
ax.set_xlabel('x(m)', fontsize=16)
ax.set_ylabel('y(m)', fontsize=16)
plt.ion()
plt.show()


env.render_axis = ax

observation = env.reset()
for i in range(1000):
    #env.calc_human_future_traj('truth')
    action = env.action_space.sample()  # User-defined policy function
    observation, reward, terminated, info = env.step(action)
    if i % 10 == 0:
        print(observation['robot_node'])

    env.render()
    if terminated:
        observation = env.reset()

env.close()

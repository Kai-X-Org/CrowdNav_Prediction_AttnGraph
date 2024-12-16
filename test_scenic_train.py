from scenic.gym import ScenicGymEnv
import scenic
from scenic.simulators.crowd_sim.simulator import CrowdSimSimulator 
import numpy as np

scenario = scenic.scenarioFromFile("/home/kxu/ScenicGym/src/scenic/simulators/crowd_sim/test.scenic",
                                   model="scenic.simulators.crowd_sim.model") # shouldn't use 2D mode?

env = ScenicGymEnv(scenario, CrowdSimSimulator(), max_steps=50)

env.reset()

render = True

episode_over = False

for i in range(3):
    while not episode_over:
        # action = env.action_space.sample_action() # dummy here ok this is not right
        action = env.action_space.sample() # dummy here ok this is not right
        observation, reward, terminated, truncated, info = env.step(action)
        # print(observation[0]['position'])
        episode_over = terminated or truncated

        if render:
            env.render()
    env.reset()
    print("finsih reset")


env.close()

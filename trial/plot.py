import pandas as pd
import matplotlib.pyplot as plt
import os

data = pd.read_csv("ddpg_cum_constraints_safety_2.csv")
# Plotting using pandas
data.plot(x='Step', y='Value', color='black', title='DDPG cumulative Constraints vs Episodes')
plt.xlabel("Episodes")
plt.ylabel("Cumulative Constraints")
plt.grid(True)
plt.savefig(os.path.join("safe-explorer", "images", "ddpg_cum_constraints_safety_2.png"))
# plt.show()

data = pd.read_csv("ddpg_reward_safety_2.csv")
# Plotting using pandas
data.plot(x='Step', y='Value', color='black', title='DDPG Episode Reward vs Episodes')
plt.xlabel("Episodes")
plt.ylabel("Mean Episodic Reward")
plt.grid(True)
plt.savefig(os.path.join("safe-explorer", "images", "ddpg_rewards_safety_2.png"))
# plt.show()
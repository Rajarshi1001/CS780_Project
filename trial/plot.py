import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the data
data = pd.read_csv("ddpg_cum_constraints_2.csv")
data2 = pd.read_csv("ddpg_cum_constraints_safety_2.csv")

# Plotting the first figure with two plots
plt.figure()
plt.plot(data['Step'], data['Value'], color='black', label='DDPG')
plt.plot(data2['Step'], data2['Value'], color='red', label='DDPG Safety')
plt.title('DDPG cumulative Constraints vs Episodes')
plt.xlabel("Episodes")
plt.ylabel("Cumulative Constraints")
plt.grid(True)
plt.legend(["DDPG only", "DDPG + safety layer"]) 
plt.savefig(os.path.join("safe-explorer", "images", "ddpg_cum_constraints_both_2.png"))
# plt.show()

# Clear the current figure to prepare for the next plot
plt.clf()

# Load the data for rewards
data = pd.read_csv("ddpg_reward_2.csv")
data2 = pd.read_csv("ddpg_reward_safety_2.csv")

# Plotting the second figure with two plots
plt.figure()
plt.plot(data['Step'], data['Value'], color='black', label='DDPG')
plt.plot(data2['Step'], data2['Value'], color='red', label='DDPG Safety')
plt.title('DDPG Episode Reward vs Episodes')
plt.xlabel("Episodes")
plt.ylabel("Mean Episodic Reward")
plt.grid(True)
plt.legend(["DDPG only", "DDPG + safety layer"]) # Add a legend
plt.savefig(os.path.join("safe-explorer", "images", "ddpg_rewards_both_2.png"))
# plt.show()

# Clear the current figure
plt.clf()

import pandas as pd
import matplotlib.pyplot as plt
import os

data = pd.read_csv("ddpg_safety_layer_100_epochs.csv")
# Plotting using pandas
data.plot(x='Step', y='Value', color='black', title='DDPG with Safety Layer Reward vs Episodes')
plt.xlabel("Episodes")
plt.ylabel("Mean Episodic Reward")
plt.grid(True)
plt.savefig(os.path.join("assets", "ddpg_safety_layer_70_epochs_pandas.png"))
plt.show()
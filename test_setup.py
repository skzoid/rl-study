import gymnasium as gym
import torch, stable_baselines3

for name in ["CartPole-v1", "LunarLander-v3", "HalfCheetah-v5"]:
    env = gym.make(name)
    obs, info = env.reset(seed=0)
    for _ in range(50):
        obs, r, terminated, truncated, info = env.step(env.action_space.sample())
        if terminated or truncated:
            obs, info = env.reset()
    print(name, "OK")
print("torch", torch.__version__, "| SB3", stable_baselines3.__version__)
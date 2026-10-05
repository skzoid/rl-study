# RL Study

A deep dive into reinforcement learning: core theory, algorithms implemented from scratch, and a final project.

**Goal:** understand RL from first principles (MDPs, Bellman equations, Q-learning, policy gradients, PPO) and apply it to a robotics-flavored project.

## Progress

- [ ] **Day 1:** MDPs, Bellman equations, multi-armed bandits
- [ ] **Day 2:** Tabular methods: Monte Carlo, TD, Q-learning, SARSA
- [ ] **Day 3:** Deep Q-Networks (DQN) from scratch
- [ ] **Day 4:** Policy gradients: REINFORCE, baselines, actor-critic
- [ ] **Day 5:** PPO and SAC, continuous control
- [ ] **Day 6:** Advanced topics (sim-to-real, offline RL, world models) + project start
- [ ] **Day 7:** Project finish, evaluation, write-up

## Repository Structure

```
rl-study/
├── notes/            # Daily notes in my own words
├── bandits/          # Epsilon-greedy bandit
├── tabular/          # Q-learning / SARSA on FrozenLake, Taxi, CliffWalking
├── dqn/              # DQN from scratch (PyTorch)
├── policy_gradient/  # REINFORCE + baseline, A2C
├── ppo_sac/          # PPO from scratch, SB3 PPO/SAC on MuJoCo
├── project/          # Final project
└── requirements.txt
```

## Setup

```bash
git clone https://github.com/skzoid/rl-study.git
cd rl-study
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# Mac/Linux
source .venv/bin/activate

python -m pip install --upgrade pip
pip install swig
pip install -r requirements.txt
python test_setup.py
```

Requires Python 3.10-3.13.

## Final Project

> *To be completed.*

**Problem:** _what task does the agent solve?_
**Algorithm and why:** _e.g. SAC + HER because continuous actions and sparse reward_
**Environment:** _e.g. Gymnasium-Robotics FetchReach_
**Key hyperparameters:** _learning rate, gamma, batch size, etc._
**Results:** _learning curves (mean ± std over 3 seeds), demo video_
**What failed and what I learned:** _honest notes_
**Next steps:** _what I'd try with more time_

## Resources

- Sutton & Barto, *Reinforcement Learning: An Introduction* (free online)
- David Silver, *Introduction to Reinforcement Learning* (YouTube)
- Hugging Face Deep RL Course
- OpenAI Spinning Up in Deep RL
- Berkeley CS285 (Sergey Levine)
- Gymnasium, Stable-Baselines3, CleanRL

## Notes

Algorithms in each folder are written from scratch where possible. Stable-Baselines3 runs are used as a baseline to compare against.
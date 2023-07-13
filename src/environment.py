import gymnasium as gym
import numpy as np
from src.constants import *
from gymnasium import spaces

# A domain reals [0,1]
# b domain reals [0,1]
# C domain reals [0,1]
# x domain integers [0,100]


class CustomEnv(gym.Env):
    """Custom Environment that follows gym interface."""

    metadata = {"render_modes": ["human"], "render_fps": 30}

    def __init__(self, A, b, C):
        super().__init__()
        # Define action and observation space
        # In our case is vector x
        self.action_space = spaces.Discrete(N_VARS, seed=42, start=0)
        self.A = A
        self.b = b
        self.C = C

    def step(self, action):
        ...
        return observation, reward, terminated, truncated, info

    def reset(self, seed=None, options=None):
        ...
        return observation, info

    def render(self):
        ...

    def close(self):
        ...
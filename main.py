import gymnasium as gym

from stable_baselines3.common.policies import Mlp
from stable_baselines3.ppo import PPO

#env = gym.make('CartPole-v1')


is_train = True



def train(model):
    model.learn(total_timesteps=25000)
    model.save("model_RL")

def eval(model):
    obs = vec_env.reset()
    while True:
        action, _states = model.predict(obs)
        obs, rewards, dones, info = vec_env.step(action)


if is_train:
    model = PPO("MlpPolicy", vec_env, verbose=1)
    train(model)
else:
    model = PPO.load("model_RL")
    eval(model)
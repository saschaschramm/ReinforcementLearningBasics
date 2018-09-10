from environment import Environment, State, Action
import random


def random_policy():
    action_index = random.randint(0, 1)
    return Action(action_index)


def simulate():
    random.seed(0)
    env = Environment()
    total_reward = 0.0
    timesteps = 1000000
    discount_rate = 0.90

    for t in range(timesteps):
        state = State.LOW

        for t in range(2):
            action = random_policy()
            state, reward = env.step(state, Action(action))
            total_reward += pow(discount_rate,t) * reward

    print("Expected return ", total_reward/timesteps)


simulate()

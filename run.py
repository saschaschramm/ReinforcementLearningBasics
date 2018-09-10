from environment import Environment, State, Action
discount_rate = 0.9
action_prob = 0.5 # random policy
timesteps = 2
env = Environment()


def state_value_function(last_state, t):
    state_value = 0
    for action in env.actions:
        for state in env.states:
            transition_prob = env.transition_prob(last_state, action, state)
            reward = env.reward(last_state, action, state)
            if t < timesteps-1:
                state_value += transition_prob * action_prob * \
                               (reward + discount_rate * state_value_function(state, t+1))
            else:
                state_value += transition_prob * action_prob * reward
    return state_value


def action_value_function(last_state, action, t):
    action_value = 0
    for state in env.states:
        transition_prob = env.transition_prob(last_state, action, state)
        reward = env.reward(last_state, action, state)
        action_value += transition_prob * (reward + discount_rate * state_value_function(state, t+1))
    return action_value


def expected_return_using_state_value_function():
    expected_return = state_value_function(State.LOW, 0)
    print("Expected return (using state-value function):", expected_return)


def expected_return_using_action_value_function():
    action_value_1 = action_value_function(State.LOW, Action.MOVE, 0)
    action_value_2 = action_value_function(State.LOW, Action.RECHARGE, 0)
    expected_return = action_value_1 * action_prob + action_value_2 * action_prob
    print("Expected return (using action-value function):", expected_return)


def main():
    expected_return_using_state_value_function()
    expected_return_using_action_value_function()


if __name__ == '__main__':
    main()

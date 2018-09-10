# Reinforcement Learning Basics

## Environment
In this project we use a simple environment to study reinforcement learning problems similar to the environment defined in the book
Reinforcement Learning: An Introduction.

Definition of the environment:
- A robot has the job to clean the room.
- The robot gets a reward when it moves.
- If the energy level is high the robot can move without risk of depleting the battery. With probability 1-alpha the
energy level reduces to low.
- If the energy level is low the robot depletes the battery with probability 1-beta. In this case the robot must be
rescued which produces a negative reward.


## Basic concepts
### Value functions

Almost all reinforcement learning algorithms 
involve estimating a value function.

#### State-value function
The state-value function is defined as the expected return of a state when the agent follows a policy.

```Python
def state_value_function(last_state, t):
    state_value = 0
    for action in env.actions:
        for state in env.states:
            transition_prob = env.transition_prob(last_state, action, state)
            reward = env.reward(last_state, action, state)
            if t < timesteps-1:
                state_value += transition_prob * action_probability * \
                               (reward + discount_rate * state_value_function(state, t+1))
            else:
                state_value += transition_prob * action_probability * reward
```

#### Action-value function
The action-value function is defined as the expected return of an action in a state when the agent follows a policy.
```Python
def action_value_function(last_state, action, t):
    action_value = 0
    for state in env.states:
        transition_prob = env.transition_prob(last_state, action, state)
        reward = env.reward(last_state, action, state)
        action_value += transition_prob * (reward + discount_rate * state_value_function(state, t+1))
```

### Policy
A policy is a mapping from states to probabilities of selecting  
each possible action. Here we assume a random policy.


## Remarks
The state-value function

```
expected_return = state_value_function(State.LOW, 0)
```
can be written in terms of the 
action-value function
```
action_value_1 = action_value_function(State.LOW, Action.MOVE, 0)
action_value_2 = action_value_function(State.LOW, Action.RECHARGE, 0)
expected_return = action_value_1 * action_probability + action_value_2 * action_probability.
```

# Run
```shell
$ python -m run
```

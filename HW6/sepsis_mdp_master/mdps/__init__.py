from gymnasium.envs.registration import register

# Registering the MDP with Gymnasium

register(
    id = 'mdps/GumbelMax-v1',
    entry_point = 'mdps.envs:GumbelMax',
    max_episode_steps = 30
)
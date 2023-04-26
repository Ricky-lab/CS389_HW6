import gymnasium as gym
import yaml
import mdps

def run_ep(env, policy):
    # Reset the environment and print the initial observation
    obs, _ =  env.reset()
    print(obs)
    
    # Run the episode until termination or truncation
    term = trunc = False
    rew_tot = 0.0
    while not (term or trunc):
        action = policy(obs)
        obs, rew, term, trunc, _ = env.step(action)
        rew_tot += rew
        print(obs, rew)

    # Print information about the reward
    if rew_tot == 1.0:
        print('Patient lived!')
    elif rew_tot == -1.0:
        print('Patient died :(')
    else:
        print('Max number of steps reached.')

    # Print information about the hidden variable (whether the patient had diabetes)
    diab_str = f'They {"had" if env.get_hidden()==1 else "did not have"} diabetes.'
    print(diab_str)

def main():
    # Opening the config file
    with open('mdps/configs/gumbel_max_diabetes/config.yml', 'r') as f:
        config = yaml.safe_load(f)

    # Creating the environment
    env = gym.make('mdps/GumbelMax-v1', config=config)

    # Creating a simple policy that does nothing
    policy = lambda x: (0, 0, 0)

    # Running a demonstration episode
    run_ep(env, policy)

if __name__ == "__main__":
    main()
from gym.envs.registration import register

register(
    id='call-v0',
    entry_point='gym_call.envs:CallEnv',
    # timestep_limit = 1000,
    # reward_threshold = 1.0,
    # nondeterministic=True
)
# register(
#     id='call-extrahard-v0',
#     entry_point='gym_call.envs:CallExtraHardEnv',
# )

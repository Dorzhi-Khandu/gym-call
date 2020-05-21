from gym.envs.registration import register

register(
    id='call-v0',
    entry_point='gym_call.envs:CallEnv',
)
register(
    id='call-extrahard-v0',
    entry_point='gym_call.envs:CallExtraHardEnv',
)
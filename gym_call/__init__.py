{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from gym.envs.registration import register\n",
    "\n",
    "register(\n",
    "    id='call-v0',\n",
    "    entry_point='gym_call.envs:CallEnv',\n",
    ")\n",
    "register(\n",
    "    id='call-extrahard-v0',\n",
    "    entry_point='gym_call.envs:CallExtraHardEnv',\n",
    ")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

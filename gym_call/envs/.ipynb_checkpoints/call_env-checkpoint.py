{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import gym\n",
    "from gym import error, spaces, utils\n",
    "from gym.utils import seeding\n",
    "\n",
    "class CallEnv(gym.Env):\n",
    "  metadata = {'render.modes': ['human']}\n",
    "\n",
    "  def __init__(self):\n",
    "    ...\n",
    "  def step(self, action):\n",
    "    ...\n",
    "  def reset(self):\n",
    "    ...\n",
    "  def render(self, mode='human'):\n",
    "    ...\n",
    "  def close(self):\n",
    "    ..."
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

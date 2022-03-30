class Environment:
    def reset(self):
        """

        :return: initial state (initial observation)
        """
        pass

    def step(self):
        """

        :return: reward, new_state, done, message
        """
        pass

    def end(self):
        """
        Environment should close any resource is currently in use for it's tasks.
        """


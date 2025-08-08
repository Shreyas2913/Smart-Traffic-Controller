import matplotlib.pyplot as plt
import os

class Visualization:
    def __init__(self, path, dpi):
        self._path = path
        self._dpi = dpi

    def save_data_and_plot(self, data, filename, xlabel, ylabel):
        """
        Produce a plot of performance of the agent over the session and save the relative data to txt
        """
        min_val = min(data)
        max_val = max(data)

        plt.rcParams.update({'font.size': 24})  # set bigger font size

        plt.plot(data)
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        plt.margins(0)
        plt.ylim(min_val - 0.05 * abs(min_val), max_val + 0.05 * abs(max_val))
        fig = plt.gcf()
        fig.set_size_inches(20, 11.25)
        fig.savefig(os.path.join(self._path, 'plot_' + filename + '.png'), dpi=self._dpi)
        plt.close("all")

        with open(os.path.join(self._path, 'plot_' + filename + '_data.txt'), "w") as file:
            for value in data:
                file.write("%s\n" % value)

    def plot_all_together(self, delay_data, queue_data, reward_data):
        """
        Generate a combined visualization for delay, queue length, and reward over episodes
        """
        episodes = list(range(1, len(delay_data) + 1))
        plt.rcParams.update({'font.size': 20})
        fig, axs = plt.subplots(3, 1, figsize=(20, 16), dpi=self._dpi)

        axs[0].plot(episodes, delay_data, color='blue')
        axs[0].set_title("Average Delay per Episode")
        axs[0].set_xlabel("Episode")
        axs[0].set_ylabel("Delay (vehicles)")

        axs[1].plot(episodes, queue_data, color='green')
        axs[1].set_title("Average Queue Length per Episode")
        axs[1].set_xlabel("Episode")
        axs[1].set_ylabel("Queue Length")

        axs[2].plot(episodes, reward_data, color='red')
        axs[2].set_title("Total Reward per Episode")
        axs[2].set_xlabel("Episode")
        axs[2].set_ylabel("Reward")

        plt.tight_layout()
        combined_path = os.path.join(self._path, "plot_combined_results.png")
        plt.savefig(combined_path)
        plt.close("all")

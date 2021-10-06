from matplotlib import pyplot as plt
import json


def main() -> None:
    with open("results.json", "r") as results_file:
        results = json.load(results_file)

    for experiment in results:
        for result_type in ["time", "comparisons"]:
            plt.figure()
            for algorithm in ["selection", "insertion", "merge", "shell"]:
                result_list = [
                    results[experiment][str(power)][algorithm][result_type]
                    for power in range(7, 16)
                ]
                plt.plot([2 ** power for power in range(7, 16)], result_list, label=algorithm)

            plt.legend()
            plt.grid()
            plt.xlabel("array length")
            plt.ylabel(result_type)
            plt.yscale("log")
            plt.title(experiment + " array")
            plt.savefig(experiment + '_' + result_type)


if __name__ == "__main__":
    main()

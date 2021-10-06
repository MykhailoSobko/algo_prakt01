import sort
import json
from random import sample, randint
from time import time


def generate_random(arr_len: int) -> list:
    arrays = []

    for _ in range(5):
        arrays.append(sample(list(range(arr_len)), arr_len))

    return arrays


def generate_increasing(arr_len: int) -> list:
    return [i for i in range(arr_len)]


def generate_decreasing(arr_len: int) -> list:
    return [i for i in reversed(range(arr_len))]


def generate_repeating(arr_len: int) -> list:
    arrays = []

    for _ in range(3):
        arrays.append([randint(1, 3) for _ in range(arr_len)])

    return arrays


def test_algorithm(algorithms: dict, algorithm: str, arr: list) -> tuple:
    start = time()

    # Choosing the algorithm and sorting the array
    current_sort = algorithms[algorithm]

    if algorithm == "merge":
        num_comps = current_sort(arr.copy(), 0, len(arr) - 1)
    else:
        num_comps = current_sort(arr.copy())

    run_time = time() - start

    return run_time, num_comps


def main() -> None:
    experiments = {
        "random": generate_random,
        "increasing": generate_increasing,
        "decreasing": generate_decreasing,
        "repeating": generate_repeating,
    }
    algorithms = {
        "selection": sort.selection_sort,
        "insertion": sort.insertion_sort,
        "merge": sort.merge_sort,
        "shell": sort.shell_sort,
    }

    powers = tuple(range(7, 16))

    results = {
        experiment: {
            power: {
                algorithm: {
                    "time": 0,
                    "comparisons": 0,
                } for algorithm in algorithms
            } for power in powers
        } for experiment in experiments
    }

    for experiment in experiments:
        for power in powers:
            # Length of the array equals 2 ** power
            generate_arr = experiments[experiment]
            arr = generate_arr(2 ** power)

            if experiment in {"random", "repeating"}:
                for array in arr:
                    for algorithm in algorithms:
                        run_time, num_comps = test_algorithm(
                            algorithms, algorithm, array
                        )

                        # Adding to the average time and comparisons
                        if experiment == "random":
                            results[experiment][power][algorithm][
                                "time"] += run_time / 5
                            results[experiment][power][algorithm][
                                "comparisons"] += num_comps / 5
                        else:
                            results[experiment][power][algorithm][
                                "time"] += run_time / 3
                            results[experiment][power][algorithm][
                                "comparisons"] += num_comps / 3
            else:
                for algorithm in algorithms:
                    run_time, num_comps = test_algorithm(
                        algorithms, algorithm, arr
                    )

                    results[experiment][power][algorithm][
                        "time"] = run_time
                    results[experiment][power][algorithm][
                        "comparisons"] = num_comps

    with open("results.json", "w") as results_file:
        json.dump(results, results_file, indent=4, sort_keys=True)


if __name__ == "__main__":
    main()

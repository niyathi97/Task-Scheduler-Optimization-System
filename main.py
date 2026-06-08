import heapq


class Task:

    def __init__(
        self,
        name,
        priority,
        deadline,
        duration,
        profit
    ):

        self.name = name
        self.priority = priority
        self.deadline = deadline
        self.duration = duration
        self.profit = profit


tasks = [

    Task("Design UI", 5, 4, 1, 100),

    Task("Database Setup", 4, 3, 1, 80),

    Task("Testing", 3, 5, 2, 60),

    Task("Documentation", 2, 6, 1, 40),

    Task("Deployment", 1, 7, 1, 30)

]


def schedule_tasks(tasks):

    heap = []

    for task in tasks:

        heapq.heappush(
            heap,
            (
                -task.priority,
                task.deadline,
                task
            )
        )

    current_time = 0

    completed = []

    missed = []

    total_profit = 0

    while heap:

        _, _, task = heapq.heappop(heap)

        current_time += task.duration

        if current_time <= task.deadline:

            completed.append(task)

            total_profit += task.profit

        else:

            missed.append(task)

    return (
        completed,
        missed,
        total_profit
    )


if __name__ == "__main__":

    completed, missed, profit = schedule_tasks(
        tasks
    )

    print("\nCOMPLETED TASKS\n")

    for task in completed:

        print(
            task.name,
            "| Priority:",
            task.priority,
            "| Profit:",
            task.profit
        )

    print("\nMISSED TASKS\n")

    for task in missed:

        print(task.name)

    print(
        "\nTOTAL PROFIT:",
        profit
    )
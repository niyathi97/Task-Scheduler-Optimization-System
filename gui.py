import tkinter as tk
from tkinter import ttk
from main import tasks, schedule_tasks


def run_scheduler():

    completed, missed, profit = schedule_tasks(tasks)

    completed_table.delete(*completed_table.get_children())
    missed_table.delete(*missed_table.get_children())

    for task in completed:

        completed_table.insert(
            "",
            "end",
            values=(
                task.name,
                task.priority,
                task.deadline,
                task.profit
            )
        )

    for task in missed:

        missed_table.insert(
            "",
            "end",
            values=(
                task.name,
                task.priority,
                task.deadline
            )
        )

    profit_label.config(
        text=f"Total Profit: {profit}"
    )

    timeline.delete("1.0", tk.END)

    current_time = 0

    timeline.insert(
        tk.END,
        "TASK EXECUTION TIMELINE\n\n"
    )

    for task in completed:

        timeline.insert(
            tk.END,
            f"{current_time}h → {current_time + task.duration}h : {task.name}\n"
        )

        current_time += task.duration


root = tk.Tk()

root.title(
    "Task Scheduler Optimization System"
)

root.geometry("1200x750")

root.configure(
    bg="#EAF4FF"
)

# Title

title = tk.Label(
    root,
    text="📅 Task Scheduler Optimization System",
    font=("Arial", 22, "bold"),
    bg="#EAF4FF",
    fg="#003366"
)

title.pack(pady=15)

# Button

schedule_btn = tk.Button(
    root,
    text="Generate Optimized Schedule",
    bg="#0066CC",
    fg="white",
    font=("Arial", 12, "bold"),
    command=run_scheduler
)

schedule_btn.pack(
    pady=10
)

# Profit

profit_label = tk.Label(
    root,
    text="Total Profit: 0",
    font=("Arial", 18, "bold"),
    bg="#EAF4FF",
    fg="green"
)

profit_label.pack(
    pady=10
)

# Completed Tasks

tk.Label(
    root,
    text="Completed Tasks",
    font=("Arial", 14, "bold"),
    bg="#EAF4FF"
).pack()

completed_columns = (
    "Task",
    "Priority",
    "Deadline",
    "Profit"
)

completed_table = ttk.Treeview(
    root,
    columns=completed_columns,
    show="headings",
    height=6
)

for col in completed_columns:

    completed_table.heading(
        col,
        text=col
    )

    completed_table.column(
        col,
        width=200,
        anchor="center"
    )

completed_table.pack(
    pady=10
)

# Missed Tasks

tk.Label(
    root,
    text="Missed Tasks",
    font=("Arial", 14, "bold"),
    bg="#EAF4FF"
).pack()

missed_columns = (
    "Task",
    "Priority",
    "Deadline"
)

missed_table = ttk.Treeview(
    root,
    columns=missed_columns,
    show="headings",
    height=4
)

for col in missed_columns:

    missed_table.heading(
        col,
        text=col
    )

    missed_table.column(
        col,
        width=250,
        anchor="center"
    )

missed_table.pack(
    pady=10
)

# Timeline

tk.Label(
    root,
    text="Execution Timeline",
    font=("Arial", 14, "bold"),
    bg="#EAF4FF"
).pack()

timeline = tk.Text(
    root,
    height=8,
    width=90,
    font=("Consolas", 10)
)

timeline.pack(
    pady=10
)

footer = tk.Label(
    root,
    text="DSA Concepts: Heap • Priority Queue • Greedy Scheduling • Sorting",
    bg="#EAF4FF",
    fg="gray",
    font=("Arial", 10)
)

footer.pack(
    pady=10
)

root.mainloop()
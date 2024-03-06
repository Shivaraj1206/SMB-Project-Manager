import tkinter as tk
from tkinter import ttk, messagebox


class Task:
    def __init__(self, name, assigned_to, deadline):
        self.name = name
        self.assigned_to = assigned_to
        self.deadline = deadline
        self.completed = False
        self.time_spent = 0

    def mark_complete(self):
        self.completed = True

    def log_time(self, time_spent):
        self.time_spent += time_spent

    def __str__(self):
        return f"{self.name} (Assigned to: {self.assigned_to}, Deadline: {self.deadline}, Completed: {self.completed}, Time Spent: {self.time_spent} hours)"


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.milestones = []
        self.team_members = set()

    def add_task(self, task):
        self.tasks.append(task)
        self.team_members.add(task.assigned_to)

    def add_milestone(self, milestone):
        self.milestones.append(milestone)

    def get_tasks_by_member(self, member):
        return [task for task in self.tasks if task.assigned_to == member]

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.completed]

    def get_time_spent(self):
        return sum(task.time_spent for task in self.tasks)

    def __str__(self):
        tasks_str = "\n".join(str(task) for task in self.tasks)
        milestones_str = "\n".join(milestone for milestone in self.milestones)
        team_members_str = ", ".join(self.team_members)
        return f"Project: {self.name}\nTasks:\n{tasks_str}\nMilestones:\n{milestones_str}\nTeam Members: {team_members_str}"


class SMBProjectManager:
    def __init__(self):
        self.projects = []
        self.team_members = set()

    def create_project(self, name):
        project = Project(name)
        self.projects.append(project)
        return project

    def add_task(self, project_name, task_name, assigned_to, deadline):
        project = self.find_project(project_name)
        if project:
            task = Task(task_name, assigned_to, deadline)
            project.add_task(task)
            self.team_members.add(assigned_to)

    def add_milestone(self, project_name, milestone):
        project = self.find_project(project_name)
        if project:
            project.add_milestone(milestone)

    def find_project(self, name):
        for project in self.projects:
            if project.name == name:
                return project
        return None

    def get_tasks_by_member(self, member):
        tasks = []
        for project in self.projects:
            tasks.extend(project.get_tasks_by_member(member))
        return tasks

    def get_completed_tasks(self):
        tasks = []
        for project in self.projects:
            tasks.extend(project.get_completed_tasks())
        return tasks

    def get_time_spent(self, project_name):
        project = self.find_project(project_name)
        if project:
            return project.get_time_spent()
        return 0


class SMBProjectManagerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("SMB Project Manager")
        self.manager = SMBProjectManager()

        # Create tabs
        self.tabs = ttk.Notebook(self.master)
        self.tabs.pack(fill="both", padx=10, pady=10)

        self.create_projects_tab()
        self.create_tasks_tab()
        self.create_reports_tab()

    def create_projects_tab(self):
        projects_tab = ttk.Frame(self.tabs)
        self.tabs.add(projects_tab, text="Projects")

        # Project list
        project_list_frame = ttk.LabelFrame(projects_tab, text="Projects")
        project_list_frame.pack(padx=10, pady=10, fill="x")

        self.project_list = tk.Listbox(project_list_frame, width=40)
        self.project_list.pack(side="left", padx=5, pady=5, fill="both", expand=True)

        project_list_scrollbar = ttk.Scrollbar(
            project_list_frame, orient="vertical", command=self.project_list.yview
        )
        project_list_scrollbar.pack(side="right", fill="y")
        self.project_list.config(yscrollcommand=project_list_scrollbar.set)

        # Create project
        create_project_frame = ttk.LabelFrame(projects_tab, text="Create Project")
        create_project_frame.pack(padx=10, pady=10, fill="x")

        project_name_label = ttk.Label(create_project_frame, text="Project Name:")
        project_name_label.pack(side="left", padx=5, pady=5)

        self.project_name_entry = ttk.Entry(create_project_frame)
        self.project_name_entry.pack(side="left", padx=5, pady=5, fill="x", expand=True)

        create_project_button = ttk.Button(
            create_project_frame, text="Create", command=self.create_project
        )
        create_project_button.pack(side="left", padx=5, pady=5)

    def create_tasks_tab(self):
        tasks_tab = ttk.Frame(self.tabs)
        self.tabs.add(tasks_tab, text="Tasks")

        # Project selection
        project_selection_frame = ttk.LabelFrame(tasks_tab, text="Select Project")
        project_selection_frame.pack(padx=10, pady=10, fill="x")

        self.selected_project_label = ttk.Label(
            project_selection_frame, text="No project selected"
        )
        self.selected_project_label.pack(side="left", padx=5, pady=5)

        # Task list
        task_list_frame = ttk.LabelFrame(tasks_tab, text="Tasks")
        task_list_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.task_list = tk.Listbox(task_list_frame, width=60)
        self.task_list.pack(side="left", padx=5, pady=5, fill="both", expand=True)

        task_list_scrollbar = ttk.Scrollbar(
            task_list_frame, orient="vertical", command=self.task_list.yview
        )
        task_list_scrollbar.pack(side="right", fill="y")
        self.task_list.config(yscrollcommand=task_list_scrollbar.set)

        # Create task
        create_task_frame = ttk.LabelFrame(tasks_tab, text="Create Task")
        create_task_frame.pack(padx=10, pady=10, fill="x")

        task_name_label = ttk.Label(create_task_frame, text="Task Name:")
        task_name_label.pack(side="left", padx=5, pady=5)

        self.task_name_entry = ttk.Entry(create_task_frame)
        self.task_name_entry.pack(side="left", padx=5, pady=5, fill="x", expand=True)

        assigned_to_label = ttk.Label(create_task_frame, text="Assigned To:")
        assigned_to_label.pack(side="left", padx=5, pady=5)

        self.assigned_to_entry = ttk.Entry(create_task_frame)
        self.assigned_to_entry.pack(side="left", padx=5, pady=5)

        deadline_label = ttk.Label(create_task_frame, text="Deadline:")
        deadline_label.pack(side="left", padx=5, pady=5)

        self.deadline_entry = ttk.Entry(create_task_frame)
        self.deadline_entry.pack(side="left", padx=5, pady=5)

        create_task_button = ttk.Button(
            create_task_frame, text="Create", command=self.create_task
        )
        create_task_button.pack(side="left", padx=5, pady=5)

        # Log time
        log_time_frame = ttk.LabelFrame(tasks_tab, text="Log Time")
        log_time_frame.pack(padx=10, pady=10, fill="x")

        task_label = ttk.Label(log_time_frame, text="Task:")
        task_label.pack(side="left", padx=5, pady=5)

        self.task_for_time_entry = ttk.Entry(log_time_frame)
        self.task_for_time_entry.pack(
            side="left", padx=5, pady=5, fill="x", expand=True
        )

        time_spent_label = ttk.Label(log_time_frame, text="Time Spent (hours):")
        time_spent_label.pack(side="left", padx=5, pady=5)

        self.time_spent_entry = ttk.Entry(log_time_frame)
        self.time_spent_entry.pack(side="left", padx=5, pady=5)

        log_time_button = ttk.Button(
            log_time_frame, text="Log Time", command=self.log_time
        )
        log_time_button.pack(side="left", padx=5, pady=5)

    def create_reports_tab(self):
        reports_tab = ttk.Frame(self.tabs)
        self.tabs.add(reports_tab, text="Reports")

        # Completed tasks
        completed_tasks_frame = ttk.LabelFrame(reports_tab, text="Completed Tasks")
        completed_tasks_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.completed_tasks_list = tk.Listbox(completed_tasks_frame, width=60)
        self.completed_tasks_list.pack(
            side="left", padx=5, pady=5, fill="both", expand=True
        )

        completed_tasks_scrollbar = ttk.Scrollbar(
            completed_tasks_frame,
            orient="vertical",
            command=self.completed_tasks_list.yview,
        )
        completed_tasks_scrollbar.pack(side="right", fill="y")
        self.completed_tasks_list.config(yscrollcommand=completed_tasks_scrollbar.set)

        # Time spent
        time_spent_frame = ttk.LabelFrame(reports_tab, text="Time Spent")
        time_spent_frame.pack(padx=10, pady=10, fill="x")

        project_label = ttk.Label(time_spent_frame, text="Project:")
        project_label.pack(side="left", padx=5, pady=5)

        self.project_for_time_entry = ttk.Entry(time_spent_frame)
        self.project_for_time_entry.pack(
            side="left", padx=5, pady=5, fill="x", expand=True
        )

        get_time_spent_button = ttk.Button(
            time_spent_frame, text="Get Time Spent", command=self.get_time_spent
        )
        get_time_spent_button.pack(side="left", padx=5, pady=5)

        self.time_spent_label = ttk.Label(time_spent_frame, text="")
        self.time_spent_label.pack(side="left", padx=5, pady=5)

    def create_project(self):
        project_name = self.project_name_entry.get()
        if project_name:
            project = self.manager.create_project(project_name)
            self.project_list.insert("end", project.name)
            self.project_name_entry.delete(0, "end")
        else:
            messagebox.showerror("Error", "Please enter a project name.")

    def create_task(self):
        selected_project = self.project_list.get(self.project_list.curselection())
        if selected_project:
            task_name = self.task_name_entry.get()
            assigned_to = self.assigned_to_entry.get()
            deadline = self.deadline_entry.get()
            if task_name and assigned_to and deadline:
                self.manager.add_task(
                    selected_project, task_name, assigned_to, deadline
                )
                self.update_task_list(selected_project)
                self.task_name_entry.delete(0, "end")
                self.assigned_to_entry.delete(0, "end")
                self.deadline_entry.delete(0, "end")
            else:
                messagebox.showerror("Error", "Please enter all task details.")
        else:
            messagebox.showerror("Error", "Please select a project.")

    def update_task_list(self, project_name):
        self.task_list.delete(0, "end")
        project = self.manager.find_project(project_name)
        if project:
            self.selected_project_label.config(text=f"Selected Project: {project_name}")
            for task in project.tasks:
                self.task_list.insert("end", str(task))

    def get_time_spent(self):
        project_name = self.project_for_time_entry.get()
        if project_name:
            time_spent = self.manager.get_time_spent(project_name)
            self.time_spent_label.config(text=f"Time Spent: {time_spent} hours")
        else:
            messagebox.showerror("Error", "Please enter a project name.")

    def log_time(self):
        selected_project = self.project_list.get(self.project_list.curselection())
        if selected_project:
            task_name = self.task_for_time_entry.get()
            time_spent = self.time_spent_entry.get()
            if task_name and time_spent.isdigit():
                project = self.manager.find_project(selected_project)
                for task in project.tasks:
                    if task.name == task_name:
                        task.log_time(int(time_spent))
                        self.update_task_list(selected_project)
                        self.task_for_time_entry.delete(0, "end")
                        self.time_spent_entry.delete(0, "end")
                        break
                else:
                    messagebox.showerror(
                        "Error", "Task not found in the selected project."
                    )
            else:
                messagebox.showerror(
                    "Error", "Please enter a valid task name and time spent."
                )
        else:
            messagebox.showerror("Error", "Please select a project.")

    def update_completed_tasks(self):
        self.completed_tasks_list.delete(0, "end")
        completed_tasks = self.manager.get_completed_tasks()
        for task in completed_tasks:
            self.completed_tasks_list.insert("end", str(task))


root = tk.Tk()
app = SMBProjectManagerGUI(root)
root.mainloop()

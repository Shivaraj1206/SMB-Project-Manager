# SMB Project Manager

## Description

SMBProjectManager is a comprehensive project management system designed specifically for Small to Medium-Sized Businesses (SMBs). It aims to streamline project management processes, improve team collaboration, and enhance productivity. This application provides a graphical user interface (GUI) built with Python's tkinter library.

## Features

* Task Tracking: Easily create and track tasks within projects. Assign tasks to team members and set deadlines. Monitor task progress and completion status.
* Time Management: Efficiently manage project timelines and schedules. Track time spent on tasks and projects. Generate time reports for analysis and optimization.
* Team Collaboration: Facilitate seamless communication among team members. Share project updates, files, and documents (not implemented in this version).
* Resource Allocation: Allocate resources effectively across projects. Monitor resource utilization and availability.
* Project Management: Create projects and define project scopes. Set project milestones and objectives. Monitor overall project progress and performance.

## Installation

1. Make sure you have Python installed on your system. This application was developed and tested with Python 3.x.
2. Clone or download the repository to your local machine.
3. Navigate to the project directory:
   cd path/to/project
4. Install the required dependencies (there are no external dependencies for this version):
   pip install tkinter

## Usage

1. Run the application:
   python smb_project_manager_gui.py
2. The SMBProjectManager GUI will open, displaying three tabs: "Projects", "Tasks", and "Reports".
3. In the "Projects" tab, you can:

* View a list of existing projects.
* Create a new project by entering the project name and clicking the "Create" button.

4. In the "Tasks" tab, you can:

* Select a project from the list of existing projects.
* View a list of tasks for the selected project.
* Create a new task by entering the task name, assigned team member, and deadline, then clicking the "Create" button.

5. In the "Reports" tab, you can:

* View a list of completed tasks.
* Get the total time spent on a specific project by entering the project name and clicking the "Get Time Spent" button.

6. To exit the application, simply close the GUI window.

## Code Structure

The code is organized into the following classes:

* Task: Represents a task with properties such as name, assigned team member, deadline, completion status, and time spent.
* Project: Represents a project with properties such as name, tasks, milestones, and team members.
* SMBProjectManager: Manages the project management system, handling operations such as creating projects, adding tasks and milestones, and retrieving data.
* SMBProjectManagerGUI: Provides the graphical user interface for the SMBProjectManager, allowing users to interact with the system through a GUI.

## Future Improvements

This implementation is a basic example, and there are several potential improvements that could be made:

* Data Persistence: Currently, the application does not persist data between runs. Implementing data persistence using a database or file storage would allow users to save and load project data.
* File Sharing: Adding the ability to share files and documents among team members would enhance collaboration.
* Authentication and Authorization: Implementing user authentication and authorization would allow for better security and access control.
* Notifications and Reminders: Adding notifications and reminders for upcoming deadlines, milestones, and other important events could improve productivity.
* Reporting and Analytics: Enhancing reporting and analytics features, such as generating custom reports and visualizations, would provide better insights into project performance.
* User Experience Improvements: Improving the user interface and experience by adding features like drag-and-drop functionality, better navigation, and more intuitive controls.

## Contributing

Contributions to the SMBProjectManager project are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the Lewis University.

## Author

- Shivaraj Chinthakindi
- Jayanth Sagar Molla
- Koushik Vunguturi

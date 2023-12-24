# Enabling Precision Control Robotic Arm
## Overview
Welcome to the "Enabling Precision Control Robotic Arm" project! This repository contains a simulation of a robotic arm, designed to offer a visually engaging and interactive experience in understanding and manipulating a tri-joint robotic arm. The simulation is built using Python and leverages libraries such as Numpy, Matplotlib, and IPyWidgets to create a dynamic, two-dimensional graphic representation of the robotic arm.

## Key Features
- **Graphical Representation:** Visualize a robotic arm with three joints (A, B, C) and a terminal device (D) in two dimensions.
- **Interactive User Interface:** Interact with the simulation by clicking on the graphic. This allows you to move the terminal device (D) to your desired location, emulating the motion of the robotic arm in real-time.
- **Live Updates:** Witness live updates of the robotic arm's positions as you interact with the graphic.
- **Data Chart:** The simulation calculates and displays a comprehensive data chart. This chart includes information about angles, positions, and angle modifications resulting from each user interaction.


## Utilized Libraries
- **Numpy:** Used for array manipulation, mathematical computations, and handling angle transformations.
- **Matplotlib:** Generates the two-dimensional graphic for visualizing the robotic arm.
- **IPyWidgets:** Provides interactive output widgets for displaying the data chart concerning angles, positions, and modifications.
- **IPython.display**: Utilized for presenting the data chart widget within the notebook.


## Functionality
- **Initialization:** The script initializes the two-dimensional graphic and the data chart widget, setting up initial positions of the joints and the terminal device based on predefined angles.
- **Plotting:** The plot_robotic_arm() function is used to render the robotic arm according to the input angles.
- **Interaction Handling:** The on_click() function manages user interactions on the graphic. It computes new positions for the joints and the terminal device in response to user clicks.
- **Data Chart Updates:** For each interaction, updated angles, positions, and angle modifications are recorded and displayed in the data chart widget.
- **Live Graphic Updates:** The robotic arm's new positions are instantly reflected on the graphic, providing a dynamic visual feedback.

## Getting Started
To set up and run this simulation:

- **Clone the Repository:** Clone this repository to your local machine using git clone   ```https://github.com/kennethcxv/-Enabling-Precision-Control-Robotic-Arm-```

- **Install Dependencies:** Install the required Python libraries (Numpy, Matplotlib, IPyWidgets)
  ```pip install numpy matplotlib ipywidgets```

- **Run the Notebook:** Open the provided Jupyter notebook in your environment and run the cells to start the simulation.

- **Interact with the Simulation:** Click on the displayed graphic to manipulate the robotic arm and observe how the arm's position and the data chart updates in real-time.

## Learning Outcomes
This project is an excellent resource for anyone interested in robotics, inverse kinematics, and data visualization using Python. It offers a hands-on approach to understanding these concepts through an interactive and visually appealing simulation.


## Contributions
I welcome contributions from the community! If you have suggestions for improvements or new features, please feel free to contribute. To do so:

- **Fork the Repository:** Click on the 'Fork' button at the top right of this page to create a copy of this repository in your GitHub account.
- **Clone Your Fork:** Clone your forked repository to your local machine.
- **Create a Branch:** Create a new branch for your modifications
  ```git checkout -b my-new-feature```
- **Make Changes and Commit:** Make your changes in your local repository and commit them
  ```git commit -am 'Add some feature```
- **Push to the Branch:** Push your changes to your fork
  ```git push origin my-new-feature```
- **Create a Pull Request:** Return to your fork on GitHub and create a new pull request.

## Reach Me
If you have any questions or would like to discuss this project further, please don't hesitate to reach out. You can contact me at 
  - Email: Kennethcxcv@gmail.com

## License
This project is licensed under the **MIT License **.

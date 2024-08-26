# PESU GPA Calculator
This is a web-based GPA calculator for PES University students. It allows students to calculate their GPA based on the grades they received in their courses. The application is built using Streamlit, a Python library for creating web applications.

## Features
- **SRN Validation**: Ensures that the entered SRN is valid before proceeding with the GPA calculation. Regular expressions have been used for implementing this feature.
- **Semester Selection**: Users can select their semester or cycle (Physics or Chemistry Cycle) to calculate their GPA. Currently works only for 1st year cycles 1st sem topics.
- **Course-wise Input**: Users can input their marks for different courses and exams including ISA1, ISA2, ESA, and other assignments or lab work.
- **SGPA Calculation**: The application calculates the SGPA (Semester Grade Point Average) based on the grades and credits of the courses. CGPA calculation isn't implemented.

## Courses Supported
- **Physics Cycle**:
  - Engineering Physics
  - Python for Computational Problem Solving
  - Engineering Mathematics
  - Elements of Electrical Engineering
  - Mechanical Engineering Sciences
  - Environmental Studies & Life Sciences
- **Chemistry Cycle**:
  - Engineering Chemistry
  - Electronic Principles and Devices
  - Engineering Mechanics-Statics
  - Constitution of India, Cyber Law and Professional Ethics
- **Common Courses**:
  - Python for Computational Problem Solving
  - Engineering Mathematics

## How to Run
1. Open your web browser and navigate to `https://pesu-gpa-calculator.streamlit.app` to access the application.
## Usage
1. Enter your SRN in the input field.
2. Select your semester or cycle from the dropdown menu.
3. Enter your marks for each course.
4. The GPA calculator will compute your SGPA based on the entered data.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## Contact
For any inquiries or issues, please contact abhranshusarkar@outlook.com or DM me on discord at sar.kar.ab.

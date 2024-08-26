import streamlit as st
import re

def main():
    st.title("PESU GPA Calculator")
    username = st.text_input("Enter your SRN:")
    if username:
        if re.search(r"^PES(1|2|3)UG\d{2}(CS|AM|EC)\d{3}$", username):
            st.success("Username is valid. You can proceed.")
            selected_option = st.selectbox("Select your semester/cycle", ['Physics Cycle', 'Chemistry Cycle'], index=None)
            if selected_option != '':
                show_entries(selected_option)
        else:
            st.error("Invalid SRN. Access denied.")

def show_entries(selected_option):
    if selected_option == 'Chemistry Cycle':
        gpa_chem()
    elif selected_option == 'Physics Cycle':
        gpa_phy()

def button_submit(to):
    if st.button("Submit"):
        st.info(f"Your GPA is {to}")

def gpa_chem():
    weighted_sum = 0

    col1, col2 = st.columns(2)
    with col1: 
        chem = get_chem()
    with col2:
        python = get_python()
    st.divider()
    col3, col4 = st.columns(2)
    with col3:
        maths = get_maths()
    with col4:
        epd = get_epd()
    st.divider()
    col5, col6 = st.columns(2)
    with col5:
        mechanics = get_mechanics()
    with col6:
        constitution = get_constitution()

    total_credits = chem[1]+python[1]+maths[1]+epd[1]+mechanics[1]+constitution[1]
    weighted_sum = chem[0]+python[0]+maths[0]+epd[0]+mechanics[0]+constitution[0]
    sgpa = weighted_sum / total_credits
    button_submit(sgpa)

def gpa_phy():
    weighted_sum = 0

    col1, col2 = st.columns(2)
    with col1:
        phy = get_phy()
    with col2:
        python = get_python()
    st.divider()
    col3, col4 = st.columns(2)
    with col3:
        maths = get_maths()
    with col4:
        elec = get_elec()
    st.divider()
    col5, col6 = st.columns(2)
    with col5:
        mechanic = get_mechanical()
    with col6:
        evs = get_evs()

    total_credits = phy[1]+python[1]+maths[1]+elec[1]+mechanic[1]+evs[1]
    weighted_sum = phy[0]+python[0]+maths[0]+elec[0]+mechanic[0]+evs[0]
    sgpa = weighted_sum / total_credits
    button_submit(sgpa)

def get_chem():
    st.markdown("### Engineering Chemistry")
    st.divider()
    credits = st.number_input("Enter the credits in Chemistry course (8th digit of course code) UE23CY151A :", min_value=1, max_value=5)
    marksi1 = st.number_input("Marks obtained in Chemistry ISA1:", value=0, step=1, format="%d", min_value=0, max_value=40)
    marksi2 = st.number_input("Marks obtained in Chemistry ISA2:", value=0, step=1, format="%d", min_value=0, max_value=40)
    markse = st.number_input("Marks obtained in Chemistry ESA:", value=0, step=1, format="%d", min_value=0, max_value=100)
    misc = st.number_input("Marks obtained in Chemistry lab/assignment:", value=0, step=1, format="%d", min_value=0, max_value=10)
    total = (markse/2) + (marksi1/2) +(marksi2/2) + misc
    gp = grade_point(total)
    sums = gp*credits
    return sums, credits

def get_python():
    st.markdown("### Python for Computational Problem Solving")
    st.divider()
    credits = st.number_input("Enter the credits in Python course (8th digit of course code) UE23CS151A:", min_value=1, max_value=5)
    marksi1 = st.number_input("Marks obtained in Python ISA1:", value=0, step=1, format="%d", min_value=0, max_value=40)
    marksi2 = st.number_input("Marks obtained in Python ISA2:", value=0, step=1, format="%d", min_value=0, max_value=40)
    markse = st.number_input("Marks obtained in Python ESA:", value=0, step=1, format="%d", min_value=0, max_value=100)
    misc = st.number_input("Marks obtained in Python project/assignment:", value=0, step=1, format="%d", min_value=0, max_value=10)
    total = (markse/2) + (marksi1/2) + (marksi2/2) + misc
    gp = grade_point(total)
    sums = gp*credits
    return sums, credits

def get_maths():
    st.markdown("### Engineering Mathematics")
    st.divider()
    credits = st.number_input("Enter the credits in Maths course (8th digit of course code) UE23MA141A :", min_value=1, max_value=5)
    marksi1 = st.number_input("Marks obatained in Maths ISA1:", value=0, step=1, format="%d", min_value=0, max_value=40)
    marksi2 = st.number_input("Marks obtained in Maths ISA2:", value=0, step=1, format="%d", min_value=0, max_value=40)
    markse = st.number_input("Marks obtained in Maths ESA:", value=0, step=1, format="%d", min_value=0, max_value=100)
    misc = st.number_input("Marks obtained in Maths assignment:", value=0, step=1, format="%d", min_value=0, max_value=10)
    total = (markse/2) + (marksi1/2) + (marksi2/2) + misc
    gp = grade_point(total)
    sums = gp*credits
    return sums, credits

def get_epd():
    st.markdown("### Electronic Principles and Devices")
    st.divider()
    credits = st.number_input("Enter the credits in EPD course (8th digit of course code) UE23EC141A :", min_value=1, max_value=5)
    marksi1 = st.number_input("Marks obatained in EPD ISA1:", value=0, step=1, format="%d", min_value=0, max_value=40)
    marksi2 = st.number_input("Marks obtained in EPD ISA2:", value=0, step=1, format="%d", min_value=0, max_value=40)
    markse = st.number_input("Marks obtained in EPD ESA:", value=0, step=1, format="%d", min_value=0, max_value=100)
    misc = st.number_input("Marks obtained in EPD assignment:", value=0, step=1, format="%d", min_value=0, max_value=10)
    total = (markse/2) + (marksi1/2) + (marksi2/2) + misc
    gp = grade_point(total)
    sums = gp*credits
    return sums, credits

def get_mechanics():
    st.markdown("### Engineering Mechanics-Statics")
    st.divider()
    credits = st.number_input("Enter the credits in Mechanics course (8th digit of course code) UE23CV131A :", min_value=1, max_value=5)
    marksi1 = st.number_input("Marks obatained in Mechanics ISA1:", value=0, step=1, format="%d", min_value=0, max_value=40)
    marksi2 = st.number_input("Marks obtained in Mechanics ISA2:", value=0, step=1, format="%d", min_value=0, max_value=40)
    markse = st.number_input("Marks obtained in Mechanics ESA:", value=0, step=1, format="%d", min_value=0, max_value=100)
    misc = st.number_input("Marks obtained in Mechanics assignment:", value=0, step=1, format="%d", min_value=0, max_value=10)
    total = (markse/2) + (marksi1/2) + (marksi2/2) + misc
    gp = grade_point(total)
    sums = gp*credits
    return sums, credits

def get_constitution():
    st.markdown("### Constitution of India, Cyber Law and Professional Ethics")
    st.divider()
    credits = st.number_input("Enter the credits in Constitution course (8th digit of course code) UE23CE111A :", min_value=1, max_value=5)
    marksi1 = st.number_input("Marks obtained in Constitution ISA1:", value=0, step=1, format="%d", min_value=0, max_value=30)
    marksi2 = st.number_input("Marks obtained in Constitution ISA2:", value=0, step=1, format="%d", min_value=0, max_value=30)
    markse = st.number_input("Marks obtained in Constitution ESA:", value=0, step=1, format="%d", min_value=0, max_value=60)
    total = ((markse/2)*50)/30 + ((marksi1/2)*25)/15 +((marksi2/2)*25)/15
    gp = grade_point(total)
    sums = gp*credits
    return sums, credits

def get_phy():
    st.markdown("### Engineering Physics")
    st.divider()
    credits = st.number_input("Enter the credits in Physics course (8th digit of course code) UE23PH151A :", min_value=1, max_value=5)
    marksi1 = st.number_input("Marks obtained in Physics ISA1:", value=0, step=1, format="%d", min_value=0, max_value=40)
    marksi2 = st.number_input("Marks obtained in Physics ISA2:", value=0, step=1, format="%d", min_value=0, max_value=40)
    markse = st.number_input("Marks obtained in Physics ESA:", value=0, step=1, format="%d", min_value=0, max_value=100)
    misc = st.number_input("Marks obtained in Physics lab/assignment:", value=0, step=1, format="%d", min_value=0, max_value=10)
    total = (markse/2) + (marksi1/2) +(marksi2/2) + misc
    gp = grade_point(total)
    sums = gp*credits
    return sums, credits

def get_elec():
    st.markdown("### Elements of Electrical Engineering")
    st.divider()
    credits = st.number_input("Enter the credits in Electrical course (8th digit of course code) UE23EE141A :", min_value=1, max_value=5)
    marksi1 = st.number_input("Marks obatained in Electrical ISA1:", value=0, step=1, format="%d", min_value=0, max_value=40)
    marksi2 = st.number_input("Marks obtained in Electrical ISA2:", value=0, step=1, format="%d", min_value=0, max_value=40)
    markse = st.number_input("Marks obtained in Electrical ESA:", value=0, step=1, format="%d", min_value=0, max_value=100)
    misc = st.number_input("Marks obtained in Electrical assignment:", value=0, step=1, format="%d", min_value=0, max_value=10)
    total = (markse/2) + (marksi1/2) + (marksi2/2) + misc
    gp = grade_point(total)
    sums = gp*credits
    return sums, credits

def get_mechanical():
    st.markdown("### Mechanical Engineering Sciences")
    st.divider()
    credits = st.number_input("Enter the credits in Mechanical course (8th digit of course code) UE23ME131A :", min_value=1, max_value=5)
    marksi1 = st.number_input("Marks obatained in Mechanical ISA1:", value=0, step=1, format="%d", min_value=0, max_value=40)
    marksi2 = st.number_input("Marks obtained in Mechanical ISA2:", value=0, step=1, format="%d", min_value=0, max_value=40)
    markse = st.number_input("Marks obtained in Mechanical ESA:", value=0, step=1, format="%d", min_value=0, max_value=100)
    misc = st.number_input("Marks obtained in Mechanical assignment:", value=0, step=1, format="%d", min_value=0, max_value=10)
    total = (markse/2) + (marksi1/2) + (marksi2/2) + misc
    gp = grade_point(total)
    sums = gp*credits
    return sums, credits

def get_evs():
    st.markdown("### Environmental Studies & Life Sciences")
    st.divider()
    credits = st.number_input("Enter the credits in Environmental Studies course (8th digit of course code) UE23EV111A :", min_value=1, max_value=5)
    marksi1 = st.number_input("Marks obtained in Environmental Studies ISA1:", value=0, step=1, format="%d", min_value=0, max_value=40)
    marksi2 = st.number_input("Marks obtained in Environmental Studies ISA2:", value=0, step=1, format="%d", min_value=0, max_value=40)
    markse = st.number_input("Marks obtained in Environmental Studies ESA:", value=0, step=1, format="%d", min_value=0, max_value=60)
    total = ((markse/2)*50)/30 + ((marksi1/2)*25)/15 +((marksi2/2)*25)/15
    gp = grade_point(total)
    sums = gp*credits
    return sums, credits

def grade_point(marks):
    if 90 <= marks <= 100:
        grade_point = 10
    elif 80 <= marks < 90:
        grade_point = 9        
    elif 70 <= marks < 80:
        grade_point = 8
    elif 60 <= marks < 70:
        grade_point = 7
    elif 50 <= marks < 60:
        grade_point = 6
    elif 40 <= marks < 50:
        grade_point = 5
    else:
        grade_point = 0
    return grade_point

if __name__ == "__main__":
    main()
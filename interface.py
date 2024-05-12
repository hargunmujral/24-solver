import streamlit as st
from solver import Solver24

def main():
    st.title("24 Game Solver")
    st.write("Enter four numbers between 1 and 13 to solve for 24.")

    nums = st.text_input("Enter four numbers, separated by commas (e.g., 1, 2, 3, 4)")

    if nums:
        num_list = nums.split(',')
        try:
            num_list = [int(num.strip()) for num in num_list]
            if len(num_list) != 4 or not all(1 <= num <= 13 for num in num_list):
                st.error("Please enter exactly four numbers, each between 1 and 13.")
            else:
                solver = Solver24(num_list)
                solutions = solver.solve()
                if solutions:
                    num_solution = len(solutions)
                    st.success(f"{num_solution} solution{'s' if num_solution > 1 else ''} found.")
                    for solution in enumerate(solutions):
                        # bullet point
                        st.write('• ', solution[1])

                else:
                    st.info("No solution found.")
        except ValueError:
            st.error("Please enter valid integers.")

if __name__ == '__main__':
    main()

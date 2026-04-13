"""
Jake Lenertz
April 2026
Simple GPA Calculator
"""

def calculate_gpa(grades):
    return sum(grades) / len(grades)

def main():
    grades = [3.5, 3.7, 4.0]
    gpa = calculate_gpa(grades)
    print("Your GPA is:", gpa)

if __name__ == "__main__":
    main()
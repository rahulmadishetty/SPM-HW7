"""To calculate the Team Effort-Hour Capacity, the below python script takes the following inputs interactively:

1) Number of Sprint Days
2) Team Member Details for each member, including:
    a) Number of days or hours off (e.g., using PTO)
    b) Number of days or hours committed to Sprint ceremonies
    c) Number of Hours/Day available (can be provided as a range)

    It calculates the total effort-hour capacity for the team based on these inputs.
"""
def compute_capacity_for_sprint():
    try:
        days_in_sprint = int(input("Specify the total days in the sprint: "))
        if days_in_sprint <= 0:
            print("Input must be a positive integer representing sprint days.")
            return

        number_of_members = int(input("How many members are in the team? "))
        if number_of_members <= 0:
            print("Input must be a positive integer representing team members.")
            return

        overall_capacity = 0
        for member_index in range(1, number_of_members + 1):
            print(f"\nInput details for member {member_index}:")
            off_hours = float(input("Total days or hours off (e.g., PTO, holidays): "))
            time_in_ceremonies = float(input("Hours dedicated to sprint ceremonies: "))
            availability_hours = input("Daily availability (hours or range like 7-9): ")

            if '-' in availability_hours:
                low, high = map(float, availability_hours.split('-'))
                avg_daily_hours = (low + high) / 2
            else:
                avg_daily_hours = float(availability_hours)

            effective_hours = (days_in_sprint - off_hours - time_in_ceremonies) * avg_daily_hours
            overall_capacity += max(effective_hours, 0)  # Prevents negative values

        print(f"\nTotal sprint capacity for the team is: {overall_capacity:.2f} hours.")

    except ValueError:
        print("Please enter valid numerical inputs. Ensure proper formatting for all entries.")

compute_capacity_for_sprint()

"""
This script will:

1) Ask for the number of sprint days and team members.
2) For each team member, it will gather data on days off, time spent in ceremonies, and available working hours per day.
3) Calculate the individual capacity considering the inputs, summing them up to get the team's total effort-hour capacity.
4) Print the total team effort-hour capacity.

Note : Ensure that the inputs are provided correctly, especially the hours per day, which can be a single number or a range (e.g., 6-8). 
If a range is provided, the script calculates the average of the two values to estimate the available hours per day.
"""

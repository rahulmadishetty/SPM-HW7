#This script will prompt the user to input the completed points for each sprint, calculate the average, and then print the result.

def compute_team_velocity():
    try:
        sprint_count = int(input("How many sprints would you like to calculate the velocity for? "))
        if sprint_count <= 0:
            print("Please enter a positive integer for the number of sprints.")
            return

        accumulated_points = 0
        for sprint in range(sprint_count):
            sprint_points = float(input(f"Input the points completed for sprint {sprint + 1}: "))
            if sprint_points < 0:
                print("Negative values for points are not allowed. Restart the program and input valid data.")
                return
            accumulated_points += sprint_points

        if sprint_count > 0:
            average_points = accumulated_points / sprint_count
            print(f"\nAverage team velocity over {sprint_count} sprints is: {average_points:.2f}")
        else:
            print("No sprints to calculate average velocity.")

    except ValueError:
        print("Please enter valid numerical inputs.")

compute_team_velocity()


"""Here is the detailed description of how exactly it works:

1) The script starts by asking the user to input the number of sprints.
2) It then prompts the user to enter the completed points for each sprint.
3) After all the points are entered, the script calculates the total sum of points and divides it by the number of sprints to get the average velocity.
4) Finally, it prints out the average velocity.

Note: We need to ensure that valid numerical values are used when the script prompts us, as it expects numbers for its calculations.
"""
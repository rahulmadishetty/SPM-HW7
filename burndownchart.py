import matplotlib.pyplot as plt

def create_burndown_chart(total_effort_hours, days_in_sprint):
    # Simulating a linear burn rate for simplicity
    daily_burn_rate = total_effort_hours / days_in_sprint
    remaining_effort = total_effort_hours
    effort_hours_remaining = []

    for day in range(days_in_sprint):
        effort_hours_remaining.append(max(0, remaining_effort))  # Ensure no negative values
        remaining_effort -= daily_burn_rate

    # Adding the final day
    effort_hours_remaining.append(0)

    # Plotting the burndown chart
    plt.figure(figsize=(10, 6))
    plt.plot(range(days_in_sprint + 1), effort_hours_remaining, marker='o', linestyle='-', color='b')
    plt.title('Sprint Burndown Chart')
    plt.xlabel('Days of Sprint')
    plt.ylabel('Remaining Effort Hours')
    plt.grid(True)
    plt.xticks(range(days_in_sprint + 1))
    plt.yticks(range(0, total_effort_hours + 10, int(total_effort_hours / 10)))
    plt.show()

# Example usage
create_burndown_chart(100, 10)  # For a 100-hour effort over a 10-day sprint

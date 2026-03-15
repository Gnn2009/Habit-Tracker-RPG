import json
import os

habit_rewards = {
    "master english": [10],
    "deep work": [9],
    "daily coding": [9],
    "strength training": [8],
    "technical reading": [8],
    "smart planning": [7],
    "optimal hydration": [7],
    "sleep hygiene": [7],
    "technical journal": [6],
    "mindfulness break": [6]
}

config_file_path = "config.json"

def update_lifetime_score(new_points_earned):
    lifetime_score = 0
    if os.path.exists(config_file_path):
        try:
            with open(config_file_path, "r") as config_file:
                saved_data = json.load(config_file)
                lifetime_score = saved_data.get("total_score", 0)
        except json.JSONDecodeError:
            lifetime_score = 0
    lifetime_score += new_points_earned
    with open(config_file_path, "w") as config_file:
        json.dump({"total_score": lifetime_score}, config_file, indent=4)
    return lifetime_score

def track_daily_habits():
    print("which habits did you complete today?")
    available_habit_names = list(habit_rewards.keys())
    for index, habit_name in enumerate(available_habit_names, start=1):
        print(f"{index}. {habit_name}")
    completed_habit_names = []
    points_earned_today = []
    while True:
        user_selection = input("\nenter the habit number (or 'n' to finish): ").strip()
        if user_selection.lower() == "n":
            break
        if user_selection.isdigit():
            selected_index = int(user_selection) - 1
            if 0 <= selected_index < len(available_habit_names):
                habit_name = available_habit_names[selected_index]
                habit_points = habit_rewards[habit_name][0]
                completed_habit_names.append(habit_name)
                points_earned_today.append(habit_points)
                print(f"registered: {habit_name} (+{habit_points} points)")
            else:
                print(f"invalid number. please enter a number between 1 and {len(available_habit_names)}.")
        else:
            print("invalid input. please enter a number or 'n'.")
    daily_total_points = sum(points_earned_today)
    new_lifetime_score = update_lifetime_score(daily_total_points)
    print("\n--- daily summary ---")
    print(f"habits completed: {completed_habit_names}")
    print(f"today's score: {daily_total_points}")
    print(f"lifetime total score (xp): {new_lifetime_score}")
    print("progress saved!")

if __name__ == "__main__":
    track_daily_habits()

habitos_exito = {
    "master english": [10],
    "deep work": [9],
    "daily coding": [9],
    "strength training": [8],
    "technical reading": [8],
    "smart_planning": [7],
    "optimal hydration": [7],
    "sleep hygiene": [7],
    "technical journal": [6],
    "mindfulness break": [6]
}

def habitCounter():
    print("Which habits did you complete today?")

    for i, habit in enumerate(habitos_exito, start=1):
        print(f"{i}. {habit}")

    completed_habit_names = []
    completed_habit_values = []
    habit_names_list = list(habitos_exito.keys())

    while True:
        user_input = input("\nEnter the habit NUMBER (or 'n' to finish): ").strip()

        if user_input.lower() == "n":
            break

        if user_input.isdigit():
            habit_index = int(user_input) - 1

            if 0 <= habit_index < len(habit_names_list):
                selected_habit = habit_names_list[habit_index]
                score_value = habitos_exito[selected_habit][0]

                completed_habit_names.append(selected_habit)
                completed_habit_values.append(score_value)

                print(f"Registered: {selected_habit} (+{score_value} points)")
            else:
                print(f"Invalid number. Please enter a number between 1 and {len(habit_names_list)}.")
        else:
            print("Invalid input. Please enter a number or 'n'.")

    print("\n--- Daily Summary ---")
    print(f"Habits: {completed_habit_names}")
    print(f"Scores: {completed_habit_values}")
    total = (sum(completed_habit_values))
    print(f"Total Score: {total}")

habitCounter()

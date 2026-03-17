import json
import os

CONFIG_FILE_PATH = "config.json"

HABIT_REWARDS = {
    "master english": 10,       # Dominar el idioma inglés
    "deep work": 9,             # Trabajo profundo y enfocado
    "daily coding": 9,          # Programación diaria
    "strength training": 8,     # Entrenamiento de fuerza/ejercicio
    "technical reading": 8,     # Lectura de material técnico
    "smart planning": 7,        # Planificación inteligente del día
    "optimal hydration": 7,     # Hidratación óptima (beber agua)
    "sleep hygiene": 7,         # Higiene del sueño/descanso adecuado
    "technical journal": 6,     # Diario técnico o bitácora de aprendizaje
    "mindfulness break": 6      # Descanso de meditación o atención plena
}

SHOP_ITEMS = {
    "Special Coffee": 25,               # Un café especial o de especialidad
    "Snack": 40,                        # Un aperitivo o botana
    "Videogames 1h": 50,                # Una hora de videojuegos
    "Series/Youtube": 40,               # Ver series o videos en YouTube
    "nap": 30,                          # Una siesta reparadora
    "Relax and movie": 150,             # Tiempo de relax viendo una película
    "Trash food": 250,                  # Comida rápida o chatarra
    "New book": 350,                    # Compra de un libro nuevo
    "Walk/hobby": 200,                  # Paseo o tiempo para un pasatiempo
    "Skin": 500,                        # Mejora estética (en juego o digital)
    "New Clothes": 800,                 # Compra de ropa nueva
    "Special Exit": 1000,               # Una salida especial o evento
    "Setup Upgrade": 2000,              # Mejora del equipo de trabajo/gaming
    "Course or certification": 3000,    # Un curso o certificación profesional
    "Free Weekend (no habits)": 5000    # Fin de semana libre de obligaciones
}

def clear_screen():
    """Clears the console screen."""
    os.system("cls" if os.name == "nt" else "clear")

def load_score() -> int:
    """Loads the total score from the configuration file."""
    if os.path.exists(CONFIG_FILE_PATH):
        try:
            with open(CONFIG_FILE_PATH, "r") as config_file:
                saved_data = json.load(config_file)
                return saved_data.get("total_score", 0)
        except json.JSONDecodeError:
            return 0
    return 0

def save_score(score: int):
    """Saves the total score to the configuration file."""
    with open(CONFIG_FILE_PATH, "w") as config_file:
        json.dump({"total_score": score}, config_file, indent=4)

def open_shop(current_score: int):
    """Handles the shop logic where users can spend their XP."""
    clear_screen()
    available_items = list(SHOP_ITEMS.keys())
    
    print("=== SHOP ===")
    for index, item_name in enumerate(available_items, start=1):
        item_cost = SHOP_ITEMS[item_name]
        print(f"{index}. {item_name} - {item_cost} XP")
    
    while True:
        print(f"\nYou have {current_score} XP available.")
        user_selection = input("Enter the item number (or 'n' to finish): ").strip()
        
        if user_selection.lower() == "n":
            break
            
        if user_selection.isdigit():
            selected_index = int(user_selection) - 1
            
            if 0 <= selected_index < len(available_items):
                item_name = available_items[selected_index]
                item_cost = SHOP_ITEMS[item_name]
                
                if item_cost <= current_score:
                    current_score -= item_cost
                    save_score(current_score)
                    print(f"You bought '{item_name}' for {item_cost} XP!")
                    print(f"Score updated. New balance: {current_score} XP")
                else:
                    print(f"Not enough points. It costs {item_cost} XP and you have {current_score} XP.")
            else:
                print("Invalid item number. Try again.")
        else:
            print("Invalid input. Please enter a number or 'n'.")

def track_daily_habits():
    """Tracks completed habits for the day and updates the total score."""
    clear_screen()
    print("Which habits did you complete today?")
    
    available_habits = list(HABIT_REWARDS.keys())
    for index, habit_name in enumerate(available_habits, start=1):
        habit_points = HABIT_REWARDS[habit_name]
        print(f"{index}. {habit_name} (+{habit_points} XP)")
        
    completed_habits = []
    points_earned_today = 0
    
    while True:
        user_selection = input("\nEnter the habit number (or 'n' to finish): ").strip()
        
        if user_selection.lower() == "n":
            break
            
        if user_selection.isdigit():
            selected_index = int(user_selection) - 1
            if 0 <= selected_index < len(available_habits):
                habit_name = available_habits[selected_index]
                habit_points = HABIT_REWARDS[habit_name]
                
                if habit_name not in completed_habits:
                    completed_habits.append(habit_name)
                    points_earned_today += habit_points
                    print(f"Registered: {habit_name} (+{habit_points} points)")
                else:
                    print(f"You already registered '{habit_name}' today.")
            else:
                print(f"Invalid number. Please enter a number between 1 and {len(available_habits)}.")
        else:
            print("Invalid input. Please enter a number or 'n'.")
            
    current_lifetime_score = load_score()
    new_lifetime_score = current_lifetime_score + points_earned_today
    save_score(new_lifetime_score)
    
    clear_screen()
    print("--- Daily Summary ---")
    print(f"Habits completed: {', '.join(completed_habits) if completed_habits else 'None'}")
    print(f"Today's score: {points_earned_today}")
    print(f"Lifetime total score (XP): {new_lifetime_score}")
    print("Progress saved!")
    
    if new_lifetime_score >= 25:
        print("\nWant to shop? [y/n]")
        user_choice = input().strip().lower()
        if user_choice == "y":
            open_shop(new_lifetime_score)
    else:
        print("\nSee you later!")

def main():
    track_daily_habits()

if __name__ == "__main__":
    main()

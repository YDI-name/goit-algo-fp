import random


def simulate_dice_rolls(num_rolls):
    # Словник для підрахунку кількості випадінь кожної суми (від 2 до 12)
    sums_count = {i: 0 for i in range(2, 13)}

    # Імітація кидків
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll_sum = dice1 + dice2
        sums_count[roll_sum] += 1

    # Обчислення ймовірностей у відсотках
    probabilities = {k: (v / num_rolls) * 100 for k, v in sums_count.items()}
    return probabilities


def main():
    num_rolls = 1_000_000  # Велика кількість кидків для більшої точності
    mc_probs = simulate_dice_rolls(num_rolls)

    # Аналітичні ймовірності згідно з умовою
    analytical_probs = {
        2: 2.78,
        3: 5.56,
        4: 8.33,
        5: 11.11,
        6: 13.89,
        7: 16.67,
        8: 13.89,
        9: 11.11,
        10: 8.33,
        11: 5.56,
        12: 2.78,
    }

    # Виведення результатів у вигляді таблиці
    print(f"Результати симуляції методом Монте-Карло ({num_rolls} кидків):\n")
    print(f"{'Сума':<6} | {'Монте-Карло (%)':<18} | {'Аналітична (%)':<15}")
    print("-" * 45)

    for i in range(2, 13):
        print(f"{i:<6} | {mc_probs[i]:<18.2f} | {analytical_probs[i]:<15.2f}")


if __name__ == "__main__":
    main()

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    """
    Жадібний алгоритм.
    Вибирає страви, максимізуючи співвідношення калорій до вартості.
    """
    # Рахуємо співвідношення калорій/вартість та сортуємо за спаданням
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    chosen_items = []
    total_cost = 0
    total_calories = 0

    for item, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            chosen_items.append(item)
            total_cost += info["cost"]
            total_calories += info["calories"]

    return chosen_items, total_calories, total_cost


def dynamic_programming(items, budget):
    """
    Алгоритм динамічного програмування (0/1 Knapsack).
    Знаходить оптимальний набір страв для максимізації калорійності.
    """
    item_names = list(items.keys())
    n = len(item_names)

    # Створюємо таблицю DP [кількість предметів + 1] x [бюджет + 1]
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Заповнюємо таблицю DP
    for i in range(1, n + 1):
        item = item_names[i - 1]
        cost = items[item]["cost"]
        calories = items[item]["calories"]

        for w in range(1, budget + 1):
            if cost <= w:
                # Беремо максимум між тим, щоб НЕ брати страву, і тим, щоб ВЗЯТИ її
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                # Якщо вартість страви перевищує поточний бюджет, ми її не беремо
                dp[i][w] = dp[i - 1][w]

    # Відновлюємо вибрані страви з таблиці DP (Backtracking)
    chosen_items = []
    w = budget
    max_calories = dp[n][budget]
    res = max_calories

    for i in range(n, 0, -1):
        if res <= 0:
            break
        # Якщо значення відрізняється від значення з попереднього рядка,
        # отже ми взяли цю страву
        if res != dp[i - 1][w]:
            item = item_names[i - 1]
            chosen_items.append(item)
            res -= items[item]["calories"]
            w -= items[item]["cost"]

    # Рахуємо загальну вартість оптимального набору
    total_cost = sum(items[item]["cost"] for item in chosen_items)

    return chosen_items, max_calories, total_cost


# Тестування роботи обох алгоритмів
if __name__ == "__main__":
    budget = 100
    print(f"Бюджет: {budget}\n")

    print("--- Жадібний алгоритм ---")
    greedy_items, greedy_calories, greedy_cost = greedy_algorithm(items, budget)
    print(f"Вибрані страви: {greedy_items}")
    print(f"Загальні калорії: {greedy_calories}")
    print(f"Загальна вартість: {greedy_cost}\n")

    print("--- Динамічне програмування ---")
    dp_items, dp_calories, dp_cost = dynamic_programming(items, budget)
    print(f"Вибрані страви: {dp_items}")
    print(f"Загальні калорії: {dp_calories}")
    print(f"Загальна вартість: {dp_cost}")

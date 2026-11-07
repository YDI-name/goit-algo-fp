import turtle
import math


def draw_pythagoras_tree(t, length, level):

    # Рекурсивна функція для малювання каркасу дерева Піфагора.
    # Базовий випадок: якщо рівень 0, припиняємо малювання
    if level == 0:
        return

    # Крок 1: Малюємо поточну гілку (стовбур)
    t.forward(length)

    # Обчислюємо довжину наступних гілок (length * √2 / 2)
    next_length = length * math.sqrt(2) / 2

    # Крок 2: Малюємо ліву гілку
    t.left(45)
    draw_pythagoras_tree(t, next_length, level - 1)

    # Крок 3: Малюємо праву гілку
    # Щоб перейти від лівої гілки до правої, повертаємо на 90 градусів праворуч
    t.right(90)
    draw_pythagoras_tree(t, next_length, level - 1)

    # Крок 4: Повертаємо черепашку у вихідне положення та орієнтацію
    t.left(45)
    t.backward(length)


def main():
    # Запит рівня рекурсії у користувача
    try:
        level = int(
            input("Введіть рівень рекурсії для дерева Піфагора (рекомендовано 5-12): ")
        )
    except ValueError:
        print("Помилка: потрібно ввести ціле число.")
        return

    # Налаштування вікна
    screen = turtle.Screen()
    screen.title("Фрактал 'Дерево Піфагора'")
    screen.setup(width=800, height=700)
    screen.tracer(0)

    # Налаштування черепашки
    t = turtle.Turtle()
    t.hideturtle()
    t.color("brown")
    t.pensize(1)

    # Переміщуємо черепашку в початкову позицію (вниз екрану)
    t.penup()
    t.setposition(200, -100)
    t.left(90)  # Повертаємо вгору
    t.pendown()

    # Запуск рекурсивного малювання (початкова довжина стовбура - 150)
    draw_pythagoras_tree(t, 60, level)

    # Відображаємо готовий малюнок на екрані
    screen.update()
    print(f"Готово! Дерево Піфагора (рівень {level}) побудовано у новому вікні.")

    # Залишаємо вікно відкритим до кліку мишкою
    screen.exitonclick()


if __name__ == "__main__":
    main()

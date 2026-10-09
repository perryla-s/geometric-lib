# **Документация проекта Geometric Lib**

### Проект представляет собой библеотеку на языке Python для вычислений площади и периметра базовых фигур (кругом, квадратом, прямоугольником, треугольником)

## **Описание функций**

### *Вычисление площади:*
#### Circle: S = πR²
#### Rectangle: S = ab
#### Square: S = a²
#### Triangle: S = ah/2

### *Вычисление периметра:*

#### Circle: P = 2πR
#### Rectangle: P = 2a + 2b
#### Square: P = 4a
#### Triangle P = a + b + c

# **Примеры вызова функций**
## **Площади**
### circle.py
### area(5)
### Результат: 78.53981633974483
---
### rectangle.py
### area(3, 4)
### Результат: 12
---
### square.py
### area(5)
### Результат: 25
---
### triangle.py
### area(10, 5)
### Результат: 25.0
---
## **Периметры**

### circle.py
### perimeter(5)
### Результат: 31.41592653589793
---
### rectangle.py
### perimeter(3, 4)
### Результат: 14
---
### square.py
### perimeter(5)
### Результат: 20
---
### triangle.py
### perimeter(3, 4, 5)
### Результат: 12

# **История изменения проекта**

- `0391dbb` Added triangle.py and fixed perimetr calculation in rectangle.py
- `7520c26` added new file rectangle.py
- `d078c8d` (origin/main, origin/HEAD, main) L-03: Docs added
- `8ba9aeb` L-03: Circle and square added
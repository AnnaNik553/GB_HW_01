# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarters = {1: {'x': [0, float('inf')], 'y': [0, float('inf')]},
            2: {'x': [0, float('-inf')], 'y': [0, float('inf')]},
            3: {'x': [0, float('-inf')], 'y': [0, float('-inf')]},
            4: {'x': [0, float('inf')], 'y': [0, float('-inf')]}
            }
print(quarters[int(input('Введите номер четверти плоскости '))])

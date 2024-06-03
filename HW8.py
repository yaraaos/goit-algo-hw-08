import heapq

def min_cost_to_connect_cables(cables):
    # Створюємо мін-купу з довжин кабелів
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Поки у купі більше одного кабеля
    while len(cables) > 1:
        # Виймаємо два найменших елементи
        first_min = heapq.heappop(cables)
        second_min = heapq.heappop(cables)
        
        # Об'єднуємо їх
        combined_length = first_min + second_min
        
        # Додаємо витрати на об'єднання до загальних витрат
        total_cost += combined_length
        
        # Поміщаємо новий об'єднаний кабель назад у купу
        heapq.heappush(cables, combined_length)
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print("Мінімальні витрати на об'єднання кабелів:", min_cost_to_connect_cables(cables))

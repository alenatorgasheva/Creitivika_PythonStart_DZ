# Задание
# Сделай так, чтобы рисунок двигался по горизонтали (справа налево <-)
# Подсказка: используй переменную и команду translate()

def setup():
    size(600, 600)
    background(210,240,255)
    noStroke()
    
def draw():
    # крыша
    fill(190,50,70)
    triangle(500,400, 550,325, 600,400)
    # стены
    fill(255,190,10)
    rect(515,400, 70,70)
    # дверь    
    fill(85,85,85)
    rect(535,420, 30,50)

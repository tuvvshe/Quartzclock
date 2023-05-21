import tkinter as tk
import time
import math

# Tsagiin shinechlel
def update_clock():
    # Odoogiin tsag
    current_time = time.strftime("%H:%M:%S")
    
    # Tsagiin labeliig uurchluh
    clock_label.config(text=current_time)
    
    # Tsagiin zuug uurchluh
    update_clock_hands()
    
    # Daraagiin shinechlelliig neg second iin draa 
    root.after(1000, update_clock)

# Tsagiin zuug shinechleh
def update_clock_hands():
    # Odoo tsag
    current_time = time.localtime()
    
    # Tsagiin zuunii hudulguuniig bodoh
    second_angle = math.radians(current_time.tm_sec * 6)
    minute_angle = math.radians((current_time.tm_min * 6) + (current_time.tm_sec * 0.1))
    hour_angle = math.radians((current_time.tm_hour * 30) + (current_time.tm_min * 0.5))
    
    # Tsagiin zuug toiroh hudulguunuur shinechleh
    canvas.itemconfigure(second_hand, angle=math.degrees(second_angle))
    canvas.itemconfigure(minute_hand, angle=math.degrees(minute_angle))
    canvas.itemconfigure(hour_hand, angle=math.degrees(hour_angle))

# Main tsonh hiih
root = tk.Tk()
root.title("Quartz Clock")

# Tsagiig haruulah shine label uusgeh
clock_label = tk.Label(root, font=("Helvetica", 24))
clock_label.pack()

# Tsagiin zuug zurah shine canvas uusgeh
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Tsagiin nuuriig zurah
clock_radius = 100
canvas.create_oval(100, 100, 200, 200, outline="black")

# Tsagiin zuug zurah
second_hand = canvas.create_line(150, 150, 150, 50, width=1)
minute_hand = canvas.create_line(150, 150, 150, 70, width=2)
hour_hand = canvas.create_line(150, 150, 150, 90, width=4)

# Tsagiig shinechleh
update_clock()

# Main event loop ehluulel
root.mainloop()
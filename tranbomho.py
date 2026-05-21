import tkinter as tk
import random


def create_window():
    popup = tk.Toplevel()
    popup.geometry("320x160")  
    popup.title("Tràn ngập bộ nhớ...")

    # Nền sáng hơn để phối hợp với màu trái tim
    frame = tk.Frame(popup, bg='#FFD1DC', padx=2, pady=2)  
    frame.pack(expand=True, fill='both', padx=10, pady=10)

    inner_frame = tk.Frame(frame, bg='#FFC0CB')  # Nền hồng nhạt
    inner_frame.pack(expand=True, fill='both', padx=5, pady=5)

    label = tk.Label(inner_frame, text="Nhớ nhớ nhớ em!!!", bg='#FFC0CB', font=("Noto Sans", 16, "italic"), fg="white")
    label.pack(expand=True)

    x = random.randint(0, popup.winfo_screenwidth() - 320)
    y = random.randint(0, popup.winfo_screenheight() - 160)
    popup.geometry(f"320x160+{x}+{y}")
    add_hearts(popup)


def add_hearts(window):
    canvas = tk.Canvas(window, bg='#FFC0CB', highlightthickness=0)  # Nền nhạt hơn
    canvas.pack(fill='both', expand=True)
    hearts = []

    def create_heart():
        x = random.randint(50, 270)
        y = 130
        size = 9  # Kích thước trái tim
        # Đổi màu trái tim theo hiệu ứng gradient
        heart_color = random.choice(["#FFB6C1", "#FFA6C9", "#FF8DA1"])
        heart = draw_heart(canvas, x, y, size, heart_color)
        hearts.append(heart)
        window.after(500, create_heart)

    def move_hearts():
        for heart in hearts[:]:
            for part in heart:
                canvas.move(part, 0, -5)
            if canvas.coords(heart[2])[1] < 0:  # Nếu phần dưới trái tim ra khỏi màn hình
                for part in heart:
                    canvas.delete(part)
                hearts.remove(heart)
        window.after(50, move_hearts)

    create_heart()
    move_hearts()


def draw_heart(canvas, x, y, size, color):
    """
    Vẽ trái tim bằng cách kết hợp 2 cung tròn và 1 tam giác.
    """
    left_arc = canvas.create_arc(
        x - size, y - size, x, y + size, 
        start=0, extent=190, style="pieslice", fill=color, outline=color
    )
    right_arc = canvas.create_arc(
        x, y - size, x + size, y + size, 
        start=0, extent=190, style="pieslice", fill=color, outline=color
    )
    bottom_triangle = canvas.create_polygon(
        x - size, y, x + size, y, x, y + size * 1.5, 
        fill=color, outline=color
    )
    return left_arc, right_arc, bottom_triangle


def create_windows_with_delay(count=50, delay=200):
    if count > 0:
        create_window()
        root.after(delay, create_windows_with_delay, count-1, delay)


def on_click():
    create_windows_with_delay()


def main_window():
    global root
    root = tk.Tk()
    root.geometry("420x210")
    root.title("Tmai needs the remedy.")

    # Nền phối hợp với màu trái tim
    root.configure(bg='#FFD1DC')  

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = 420
    window_height = 210
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))

    root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    button = tk.Button(root, text="Anh Muốn nói là...", font=("Noto Sans", 24), command=on_click, bg='#FFB6C1', fg="white")
    button.pack(expand=True)

    root.mainloop()


main_window()
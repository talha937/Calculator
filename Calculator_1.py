import tkinter as tk
from tkinter import font


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("CalcMate- Where Numbers Meet Clarity")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Professional Color Scheme
        self.bg_primary = "#1a1a2e"      # Dark navy blue
        self.bg_secondary = "#16213e"    # Darker blue
        self.accent_color = "#0f4c75"    # Professional blue
        self.highlight_color = "#3282b8" # Bright blue
        self.text_light = "#eaeaea"      # Off-white
        self.operator_color = "#e94560"  # Elegant red
        self.equals_color = "#00d9ff"    # Cyan
        
        self.root.configure(bg=self.bg_primary)
        
        self.expression = ""
        self.input_text = tk.StringVar()
        
        # Create UI
        self.create_display()
        self.create_buttons()
    
    def create_display(self):
        display_frame = tk.Frame(self.root, bg=self.bg_primary)
        display_frame.pack(expand=True, fill="both", padx=20, pady=(30, 10))
        
        display_font = font.Font(family="Segoe UI", size=32, weight="bold")
        
        display = tk.Entry(
            display_frame,
            textvariable=self.input_text,
            font=display_font,
            bg=self.bg_secondary,
            fg=self.text_light,
            bd=0,
            justify="right",
            insertbackground=self.highlight_color,
            relief="flat"
        )
        display.pack(expand=True, fill="both", ipady=20, ipadx=10)
    
    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg=self.bg_primary)
        button_frame.pack(expand=True, fill="both", padx=20, pady=(10, 30))
        
        button_font = font.Font(family="Segoe UI", size=18, weight="bold")
        
        buttons = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]
        
        for i, row in enumerate(buttons):
            for j, button in enumerate(row):
                # Determine button color
                if button in ['C', '⌫']:
                    bg_color = self.operator_color
                    hover_color = "#ff6b81"
                elif button in ['/', '*', '-', '+', '%']:
                    bg_color = self.accent_color
                    hover_color = self.highlight_color
                elif button == '=':
                    bg_color = self.equals_color
                    hover_color = "#5ce1e6"
                else:
                    bg_color = self.bg_secondary
                    hover_color = self.accent_color
                
                # Special styling for last row
                if i == 4:
                    if button == '0':
                        btn = tk.Button(
                            button_frame,
                            text=button,
                            font=button_font,
                            bg=bg_color,
                            fg=self.text_light,
                            bd=0,
                            activebackground=hover_color,
                            activeforeground=self.text_light,
                            cursor="hand2",
                            relief="flat",
                            command=lambda x=button: self.click(x)
                        )
                        btn.grid(row=i, column=0, columnspan=2, sticky="nsew", padx=3, pady=3)
                    else:
                        btn = tk.Button(
                            button_frame,
                            text=button,
                            font=button_font,
                            bg=bg_color,
                            fg=self.text_light,
                            bd=0,
                            activebackground=hover_color,
                            activeforeground=self.text_light,
                            cursor="hand2",
                            relief="flat",
                            command=lambda x=button: self.click(x)
                        )
                        col = 2 if button == '.' else 3
                        btn.grid(row=i, column=col, sticky="nsew", padx=3, pady=3)
                else:
                    btn = tk.Button(
                        button_frame,
                        text=button,
                        font=button_font,
                        bg=bg_color,
                        fg=self.text_light,
                        bd=0,
                        activebackground=hover_color,
                        activeforeground=self.text_light,
                        cursor="hand2",
                        relief="flat",
                        command=lambda x=button: self.click(x)
                    )
                    btn.grid(row=i, column=j, sticky="nsew", padx=3, pady=3)
        
        # Configure grid weights for responsiveness
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.grid_columnconfigure(j, weight=1)
    
    def click(self, item):
        if item == 'C':
            self.expression = ""
            self.input_text.set("")
        elif item == '⌫':
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif item == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(item)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
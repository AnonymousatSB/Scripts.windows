import tkinter as tk
import random
from datetime import datetime

class FakecTrader:
    def __init__(self, root):
        self.root = root
        self.root.title("cTrader Simulator (Fake)")
        self.balance = 10000.00
        self.price = 1.1000
        self.btc_price = 30000.00  # initial BTC price
        self.is_admin = False      # admin access flag

        self.create_ui()
        self.update_price_loop()
        self.update_btc_price()
        self.root.bind("<Configure>", self.handle_resize)

    def create_ui(self):
        # Balance
        self.balance_label = tk.Label(self.root, text=f"Saldo: €{self.balance:,.2f}", font=("Arial", 14))
        self.balance_label.pack(pady=10)

        # EURUSD Price
        self.price_label = tk.Label(self.root, text=f"EURUSD: {self.price:.5f}", font=("Consolas", 16), fg="green")
        self.price_label.pack()

        # BTC Price
        self.btc_label = tk.Label(self.root, text=f"BTCUSD: ${self.btc_price:,.2f}", font=("Consolas", 16), fg="orange")
        self.btc_label.pack()

        # Show BTC Price Button
        btc_btn = tk.Button(self.root, text="Show BTC Price", command=self.show_btc_price, width=15, bg="#f7931a", fg="black")
        btc_btn.pack(pady=5)

        # Buy/Sell Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        buy_btn = tk.Button(button_frame, text="Buy", command=self.buy, width=10, bg="green", fg="white")
        buy_btn.grid(row=0, column=0, padx=10)

        sell_btn = tk.Button(button_frame, text="Sell", command=self.sell, width=10, bg="red", fg="white")
        sell_btn.grid(row=0, column=1, padx=10)

        # Log output - bigger default size
        self.log_box = tk.Text(self.root, height=16, width=70)
        self.log_box.pack(pady=10)
        self.log("cTrader booted at " + datetime.now().strftime("%H:%M:%S"))

        # Command Entry
        self.cmd_entry = tk.Entry(self.root, width=40)
        self.cmd_entry.pack(pady=5)
        self.cmd_entry.bind("<Return>", self.run_command)
        self.cmd_entry.insert(0, "You should like to use /bic!")

    def update_price_loop(self):
        # Simulate EURUSD price updates
        change = random.uniform(-0.0003, 0.0003)
        self.price = max(1.05, min(1.20, self.price + change))
        self.price_label.config(text=f"EURUSD: {self.price:.5f}")
        self.root.after(1000, self.update_price_loop)

    def update_btc_price(self):
        # Simulate BTC price change every 1.5 seconds
        change = random.uniform(-200, 200)
        self.btc_price = max(1000, self.btc_price + change)
        self.btc_label.config(text=f"BTCUSD: ${self.btc_price:,.2f}")
        self.root.after(1500, self.update_btc_price)

    def show_btc_price(self):
        self.log(f"Current BTC Price: ${self.btc_price:,.2f}")

    def buy(self):
        self.balance -= 100
        self.update_ui("Buy")

    def sell(self):
        self.balance += 100
        self.update_ui("Sell")

    def update_ui(self, action):
        self.balance_label.config(text=f"Saldo: €{self.balance:,.2f}")
        self.log(f"{action} @ {self.price:.5f} | Novo saldo: €{self.balance:,.2f}")

    def log(self, msg):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_box.insert(tk.END, f"[{timestamp}] {msg}\n")
        self.log_box.see(tk.END)

    def run_command(self, event):
        cmd = self.cmd_entry.get().strip()
        self.cmd_entry.delete(0, tk.END)

        if cmd.startswith("/c balance="):
            try:
                value = float(cmd.split("=")[1])
                self.balance = value
                self.update_ui("Comando /c executado")
            except:
                self.log("Erro: formato inválido. Use /c balance=12345")

        elif cmd.startswith("/btc="):
            try:
                value = float(cmd.split("=")[1])
                self.btc_price = value
                self.btc_label.config(text=f"BTCUSD: ${self.btc_price:,.2f}")
                self.log(f"Comando /btc executado. Novo preço do BTC: ${self.btc_price:,.2f}")
            except:
                self.log("Erro: formato inválido. Use /btc=42000")

        elif cmd.startswith("/admin "):
            password = cmd.split(" ", 1)[1]
            if password == "root123":
                self.is_admin = True
                self.log("Admin access granted.")
            else:
                self.log("Invalid admin password.")

        elif cmd == "/wipebalance":
            if self.is_admin:
                self.balance = 0
                self.btc_price = 0
                self.price = 0
                self.balance_label.config(text=f"Saldo: €0.00")
                self.btc_label.config(text=f"BTCUSD: $0.00")
                self.price_label.config(text=f"EURUSD: 0.00000")
                self.log("Admin wiped ALL values: balance, BTC and EURUSD set to 0.")
            else:
                self.log("Access denied. Use /admin first.")

        elif cmd == "/bic":
            self.log("Available Commands:")
            self.log("/c balance=[amount] – sets your fake balance")
            self.log("/btc=[amount] – sets BTC fake price")
            self.log("/admin [password] – login as admin")
            self.log("/wipebalance – admin only: sets balance to €0 and prices to 0")
            self.log("/bic – shows this command list")
            self.log("/help – fake help center")
            self.log("/login – simulate login")
            self.log("/reset – resets your balance to 10,000")
            self.log("/flip – coin flip")
            self.log("/info – fake platform info")
            self.log("/ping – shows latency")
            self.log("/version – show fake app version")
            self.log("/support – contact fake support")

        elif cmd == "/help":
            self.log("Help Center: Visit https://fake.ctrader/help")

        elif cmd == "/login":
            self.log("Login: User authenticated successfully (fake)")

        elif cmd == "/reset":
            self.balance = 10000.00
            self.update_ui("Balance reset")

        elif cmd == "/flip":
            result = random.choice(["Heads", "Tails"])
            self.log(f"Coin flip result: {result}")

        elif cmd == "/info":
            self.log("Fake cTrader running in simulation mode.")

        elif cmd == "/ping":
            latency = random.randint(10, 200)
            self.log(f"Ping: {latency}ms")

        elif cmd == "/version":
            self.log("Fake cTrader v0.1.3 (Simulated Build)")

        elif cmd == "/support":
            self.log("Contact fake support at support@fakectrader.com")

        else:
            self.log(f"Comando desconhecido: {cmd}")

    def handle_resize(self, event):
        width = self.root.winfo_width()
        height = self.root.winfo_height()

        # Resize thresholds
        if width > 900 or height > 700:
            font_big = ("Arial", 20)
            font_price = ("Consolas", 24)
            entry_width = 60
            log_height = 22
            log_width = 90
        else:
            font_big = ("Arial", 14)
            font_price = ("Consolas", 16)
            entry_width = 40
            log_height = 16
            log_width = 70

        # Apply sizes
        self.balance_label.config(font=font_big)
        self.price_label.config(font=font_price)
        self.btc_label.config(font=font_price)
        self.cmd_entry.config(width=entry_width)
        self.log_box.config(height=log_height, width=log_width)

# Run
root = tk.Tk()
app = FakecTrader(root)
root.mainloop()

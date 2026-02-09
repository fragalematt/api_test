import requests
import tkinter as tk
from datetime import datetime

def trackBitcoin():
    try:
        url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()

        price = data["USD"]
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        labelPrice.config(text=f"{price:,.2f} USD")
        labelTime.config(text=f"Last Updated: {now}")

    except Exception as e:
        labelPrice.config(text="Error fetching price")
        labelTime.config(text=str(e))


    # schedule next run if refreshing is enabled//built in AI helped here
    if is_refreshing:
        canvas.after(refresh_interval_sec * 1000, trackBitcoin)

canvas = tk.Tk()
canvas.geometry("400x400")
canvas.title("Bitcoin Tracker")

f1 = ("Arial", 20, "bold")
f2 = ("Arial", 18, "bold")
f3 = ("Arial", 16, "normal")

label = tk.Label(canvas, text="Bitcoin Price", font=f1)
label.pack(pady=20)

labelPrice = tk.Label(canvas, font=f2, text="Loading...")
labelPrice.pack(pady=20)

labelTime = tk.Label(canvas, font=f3, text="")
labelTime.pack(pady=20)
#used built in AI for this part to learn from an example
# automatic refresh settings
refresh_interval_sec = 30
is_refreshing = True

def set_interval():
    global refresh_interval_sec
    try:
        val = int(entryInterval.get())
        if val < 1:
            val = 1
        refresh_interval_sec = val
        entryInterval.delete(0, tk.END)
        entryInterval.insert(0, str(refresh_interval_sec))
    except Exception:
        pass

def start_refresh():
    global is_refreshing
    if not is_refreshing:
        is_refreshing = True
        trackBitcoin()

def stop_refresh():
    global is_refreshing
    is_refreshing = False

# controls for refresh interval and start/stop
frame = tk.Frame(canvas)
frame.pack(pady=10)

entryInterval = tk.Entry(frame, width=6)
entryInterval.insert(0, str(refresh_interval_sec))
entryInterval.grid(row=0, column=0)

btnSet = tk.Button(frame, text="Set sec", command=set_interval)
btnSet.grid(row=0, column=1, padx=5)

btnStart = tk.Button(frame, text="Start", command=start_refresh)
btnStart.grid(row=0, column=2, padx=5)

btnStop = tk.Button(frame, text="Stop", command=stop_refresh)
btnStop.grid(row=0, column=3, padx=5)

# IMPORTANT: start the first fetch
trackBitcoin()

canvas.mainloop()
import tkinter as tk
from tkinter import messagebox
import joblib

# Load model
model = joblib.load("crop_model.pkl")

def predict_crop():
    try:
        N = int(entry_N.get())
        P = int(entry_P.get())
        K = int(entry_K.get())
        temp = float(entry_temp.get())
        humidity = float(entry_humidity.get())
        ph = float(entry_ph.get())
        rainfall = float(entry_rainfall.get())

        data = [[N, P, K, temp, humidity, ph, rainfall]]
        prediction = model.predict(data)[0]

        messagebox.showinfo("Prediction", f"🌱 Recommended Crop: {prediction}")

    except:
        messagebox.showerror("Error", "❌ Please enter valid inputs.")

# ---------------- Tkinter GUI ---------------- #
root = tk.Tk()
root.title("🌾 Crop Recommendation System")

# Window size and fixed position (centered)
window_width = 450
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
root.resizable(False, False)  # fixed size

# Styling
bg_color = "#E8F6F3"
label_font = ("Arial", 12, "bold")
entry_font = ("Arial", 12)
button_font = ("Arial", 13, "bold")

root.configure(bg=bg_color)

# Labels and Entry fields
labels = ["Nitrogen (N)", "Phosphorus (P)", "Potassium (K)", 
          "Temperature (°C)", "Humidity (%)", "pH", "Rainfall (mm)"]

entries = []

for i, text in enumerate(labels):
    tk.Label(root, text=text, font=label_font, bg=bg_color).grid(row=i, column=0, padx=10, pady=8, sticky="w")
    entry = tk.Entry(root, font=entry_font, width=18)
    entry.grid(row=i, column=1, padx=10, pady=8)
    entries.append(entry)

entry_N, entry_P, entry_K, entry_temp, entry_humidity, entry_ph, entry_rainfall = entries

# Predict Button
predict_btn = tk.Button(root, text="🔍 Predict Crop", command=predict_crop,
                        bg="#27AE60", fg="white", font=button_font, relief="raised", padx=10, pady=5)
predict_btn.grid(row=len(labels), columnspan=2, pady=20)

# Run App
root.mainloop()

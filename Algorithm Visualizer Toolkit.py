import tkinter as tk
from tkinter import ttk, messagebox
import time
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
class AlgorithmVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Algorithm Visualizer Toolkit")
        self.state("zoomed")  
        self.config(bg="#e8f0fe")
        title_label = tk.Label(self, text="Algorithm Visualizer Toolkit",
                               font=("Helvetica", 26, "bold"), bg="#1a73e8", fg="white", pady=20)
        title_label.pack(fill="x")
        main_frame = tk.Frame(self, bg="#e8f0fe", padx=40, pady=40)
        main_frame.pack(fill="both", expand=True)
        input_frame = tk.LabelFrame(main_frame, text="Input Data", bg="#ffffff", font=("Helvetica", 14, "bold"),
                                    padx=20, pady=20, relief="groove", labelanchor="n", bd=4, fg="#1a73e8")
        input_frame.pack(fill="x", pady=10)
        self.input_box = ttk.Entry(input_frame, font=("Helvetica", 13))
        self.input_box.pack(fill="x", pady=5)
        self.input_box.insert(0, "Enter numbers separated by commas (e.g., 5,3,8,2)")
        algo_frame = tk.LabelFrame(main_frame, text="Algorithm Selection", bg="#ffffff", font=("Helvetica", 14, "bold"),
                                   padx=20, pady=20, relief="groove", labelanchor="n", bd=4, fg="#1a73e8")
        algo_frame.pack(fill="x", pady=10)
        ttk.Label(algo_frame, text="Choose Category:", font=("Helvetica", 12)).pack(pady=5)
        self.category = ttk.Combobox(algo_frame, values=["Searching", "Sorting"], state="readonly", font=("Helvetica", 12))
        self.category.pack(pady=5)
        self.category.bind("<<ComboboxSelected>>", self.update_options)
        ttk.Label(algo_frame, text="Select Algorithm:", font=("Helvetica", 12)).pack(pady=5)
        self.algorithm = ttk.Combobox(algo_frame, state="readonly", font=("Helvetica", 12))
        self.algorithm.pack(pady=5)
        ttk.Button(algo_frame, text="Run Algorithm", command=self.run_algorithm, style="Accent.TButton").pack(pady=10, ipadx=10, ipady=5)
        output_frame = tk.LabelFrame(main_frame, text="Output", bg="#ffffff", font=("Helvetica", 14, "bold"),
                                     padx=20, pady=20, relief="groove", labelanchor="n", bd=4, fg="#1a73e8")
        output_frame.pack(fill="both", expand=True, pady=10)
        self.output_box = tk.Text(output_frame, height=15, font=("Consolas", 12), wrap="word", bg="#f1f3f4", fg="#202124")
        self.output_box.pack(fill="both", expand=True)
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Accent.TButton", background="#1a73e8", foreground="white", font=("Helvetica", 12, "bold"))
        style.map("Accent.TButton", background=[("active", "#1558b0")])
    def update_options(self, event):
        if self.category.get() == "Searching":
            self.algorithm['values'] = ["Linear Search", "Binary Search"]
        else:
            self.algorithm['values'] = ["Bubble Sort", "Quick Sort", "Merge Sort"]
    def run_algorithm(self):
        try:
            data = list(map(int, self.input_box.get().replace(
                "Enter numbers separated by commas (e.g., 5,3,8,2)", "").split(",")))
        except:
            messagebox.showerror("Error", "Please enter valid integers separated by commas.")
            return
        algo_type = self.algorithm.get()
        self.output_box.delete(1.0, tk.END)
        if not algo_type:
            messagebox.showwarning("Warning", "Please select an algorithm.")
            return
        start = time.time()
        if algo_type == "Linear Search":
            key = simple_input(self, "Enter element to search:")
            idx = linear_search(data, key)
            result = f"Element found at index {idx}" if idx != -1 else "Element not found."
            complexity = "Time: O(n), Space: O(1)"
        elif algo_type == "Binary Search":
            key = simple_input(self, "Enter element to search:")
            data.sort()
            idx = binary_search(data, key)
            result = f"Sorted Data: {data}\nElement found at index {idx}" if idx != -1 else "Element not found."
            complexity = "Time: O(log n), Space: O(1)"
        elif algo_type == "Bubble Sort":
            sorted_data = bubble_sort(data.copy())
            result = f"Sorted Data: {sorted_data}"
            complexity = "Time: O(n²), Space: O(1)"
        elif algo_type == "Quick Sort":
            sorted_data = quick_sort(data.copy())
            result = f"Sorted Data: {sorted_data}"
            complexity = "Time: O(n log n), Space: O(log n)"
        elif algo_type == "Merge Sort":
            sorted_data = merge_sort(data.copy())
            result = f"Sorted Data: {sorted_data}"
            complexity = "Time: O(n log n), Space: O(n)"
        else:
            result, complexity = "Invalid selection", ""
        end = time.time()
        elapsed = round(end - start, 5)
        self.output_box.insert(tk.END, f"Algorithm: {algo_type}\n\nInput: {data}\n\n{result}\n\n"
                                       f"Complexity: {complexity}\nExecution Time: {elapsed} sec")
def simple_input(root, msg):
    popup = tk.Toplevel(root)
    popup.title("Input Required")
    popup.geometry("350x180")
    popup.config(bg="#e8f0fe")
    tk.Label(popup, text=msg, bg="#e8f0fe", font=("Helvetica", 12, "bold")).pack(pady=10)
    entry = ttk.Entry(popup, font=("Helvetica", 12))
    entry.pack(pady=5)
    result = {'val': None}
    def submit():
        try:
            result['val'] = int(entry.get())
            popup.destroy()
        except:
            messagebox.showerror("Error", "Please enter a valid integer.")
    ttk.Button(popup, text="Submit", command=submit).pack(pady=10)
    popup.wait_window()
    return result['val']
if __name__ == "__main__":
    app = AlgorithmVisualizer()
    app.mainloop()
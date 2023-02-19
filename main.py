from tkinter import messagebox


# def frequency_map(text, k):
#     freq = {}
#     n = len(text)
#     for i in range(n - k + 1):
#         pattern = text[i:i + k]
#         freq[pattern] = 0
#
#     for i in range(n - k + 1):
#         j = text[i:i + k]
#         freq[j] += 1
#     return freq

def frequency_map(text, k):
    freq = {}                           # Initialize dictionary
    n = len(text)                       # text_len
    for i in range(n-k+1):              # sliding pattern start index
        pattern = text[i:i+k]           # Search for this pattern
        count = 0                       # Initialize pattern matching count
        for j in range(n - k + 1):      # Sliding text start index
            if text[j:j+k] == pattern:  # Text substring matches pattern
                count += 1              # Count matching pattern
        freq[pattern] = count           # How many found?
    return freq


text = 'CGATATATCCATAG'
k = 3

frequencyMap = frequency_map(text, k)

title = "Frequency Map"
messagebox.showinfo(title, f"The frequency map is {frequencyMap}")

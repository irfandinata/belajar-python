import time

def animate_line(text, delay=0.07):  # 0.07 detik/huruf → pas
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

lyrics = [
    ("cinta ini hanya untukmu", 2),
    ("kau bukan main", 4),
    ("bersamamu aku hadir", 6),
    ("selamanya hingga akhir", 8),
    ("terimakasih tuk semua rasa", 10),
    ("yang kau berikan untukku", 12),
]

start_time = time.time()
for line, lyrics_time in lyrics:
    while time.time() - start_time < lyrics_time:
        time.sleep(0.1)
    animate_line(line, delay=0.07)  # lebih enak dibaca
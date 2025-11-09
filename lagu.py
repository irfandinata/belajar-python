import time
def animate_line(text, delay=0.08):

    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

lyrics =[
             ("cinta ini hanya untukmu",8),
             ("kau bukan main",7),
             ("bersamamu aku hadir",7),
             (" selamanya hingga akhir",5),
             ("terimakasih tuk semua rasa",9),
             (" yang kau berikan untukku",8),
        ]
    


start_time = time.time()
    for line, lyrics_time in lyrics: 
     while time.time() - start_time < lyrics_time:
      time.sleep(0.1)

        animate_line(line, delay=0.006)
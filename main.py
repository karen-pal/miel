import subprocess
import random
import time
from pynput import keyboard


video_directory = "selectedclips/"  # Change this to the path of your video directory
video_file_list = [
    'P1010118_libre.mp4',
    'P1010118_saltar_linea.mp4',
    'P1010119_compartir.mp4',
    'P1010119_marchar.mp4',
    'P1010120_resistencia.mp4',
    'P1010120_solidaridad.mp4',
    'P1010121_estallido.mp4',
    'P1010121_revolucion.mp4',
    'P1010122_comunitario.mp4',
    'P1010122_manifestacion.mp4',
    'P1010123_olla.mp4',
    'P1010123_revolucion.mp4',
    'P1010124_linea.mp4',
    'P1010124_miedo.mp4',
    'P1010125_resistencia.mp4',
    'P1010125_solidaridad.mp4',
    'P1010126_olla.mp4',
    'P1010126_resistencia.mp4',
]

video_words_dict = {
    'P1010118_libre.mp4':"¿Qué es ser libre?\nNo tener cadenas\n\n",
    'P1010118_saltar_linea.mp4':"¿Cómo se cruza la primera línea?\nSaltando\n\n",
    'P1010119_compartir.mp4':"¿A qué huele la olla comunitaria?\nA compartir.\n\n",
    'P1010119_marchar.mp4':"¿Qué te hace marchar?\nLa Voluntad\n\n",
    'P1010120_resistencia.mp4':"¿Qué es un punto de resistencia para ti?\nUn lugar donde las personas se defienden las unas de las otras.\n\n",
    'P1010120_solidaridad.mp4':"Qué es la solidaridad? \nPensar en el otro así como pienso en mi mismo.\n\n",
    'P1010121_estallido.mp4': "Para ti que es un estallido?\nUn estallido es cuando algo ya no puede contener lo que lleva adentro y se convierte en un caos porque explota\n\n",
    'P1010121_revolucion.mp4':" Para ti que es revolución?\nuna revolución es cuando entra una idea a cambiar esquemas\n\n",
    'P1010122_comunitario.mp4':"Para ti que es lo comunitario?\nPara mí lo comunitario es tener ese sentimiento de amor por el compartir.Lo comunitario es apreciar nuestra cultura.\n\n",
    'P1010122_manifestacion.mp4':"¿Qué es una manifestación pacífica para ti?\nUna manifestación pacífica es un lugar que podemos habitar con nuestra forma de expresión más libre. Un espacio donde podemos ser lo que queremos ser y decir lo que merecemos.\n\n",
    'P1010123_olla.mp4':" A que huele una olla comunitaria para ti?\n A que huele una olla comunitaria... Huele al amor, huele al deseo de compartir, huele al deseo de querer estar en comunidad y una mejoría para el entorno\n\n",
    'P1010123_revolucion.mp4':"¿Cómo haces resistencia? \n Como hago resistencia, siento que lo hago desde varias partes de mi vida, en específico en la comunidad, tratando de llevar el arte... resistir día a día, desde lo que me apasióna, poderlo compartir. Siento que eso hace parte de tener resistencias desde el ámbito artístico",
    'P1010124_linea.mp4':"¿ Cómo crees que se puede  cruzar la primera línea?\nUff. Es una decisión difícil,  cruzar la primera línea implica riesgo, implica sobre todo tomar la decisión, poder enfrentarse con lo que está del otro lado y decir… Puta yo tengo que pasar eso y ser mejor, tengo que superar esas cosas que están allá.\n\n",
    'P1010124_miedo.mp4':"Qué miedos has perdido? \nMiedo a la muerte, yo siento que en últimas todos vamos a morir, y entonces,  como… Como vivo y cómo aprovecho el tiempo que tengo sin dejar  de pensar  en, Ah!! mañana me voy a morir. ¿Bueno  si mañana muero que  hago ahora? . Es más eso.\n\n",
    'P1010125_resistencia.mp4':"¿Cómo haces resistencia?\nPues… ¿Cómo hago resistencia?. No sé,  yo creo  que el estar aquí parada, viva, es como resistencia. Porque creo que  todo lo que me ha pasado… pues  yo creo que es un milagro que  yo esté aquí. Creo que eso es como resistencia. Estar aquí, ahora, respirando.\n\n",
    'P1010125_solidaridad.mp4':"¿Para ti qué es la solidaridad?\nPonerme en los zapatos de los demás.\n\n",
    'P1010126_olla.mp4':"¿Para ti a qué huele una olla comunitaria?\nA amor, a muchas personas, a sancocho, a Cali.\n\n",
    'P1010126_resistencia.mp4':"¿Para ti que es un punto de resistencia?\nCreo que es un lugar donde… donde se habita desde la fuerza, desde la potencia que sacamos cuando… cuando ya no podemos aguantar algo y nos quedamos  ahí. Solo resistiendo.\n\n",

        }



delay=5
overlap_count = 4  # Number of overlapping videos
screen_number = 1
sequential_mode = True
def on_key_release(key):
    #print(key)
    global delay, overlap_count, sequential_mode

    if key == keyboard.Key.esc:
        return False  # Stop listener

    if key == keyboard.Key.right:
        delay += 1  # Increase delay
    elif key == keyboard.Key.left and delay > 1:
        delay -= 1  # Decrease delay, ensure it doesn't go below 1
    elif key == keyboard.Key.up:  # Use the up key to increase overlap count
        overlap_count += 1
        print("overlap_count: ",overlap_count)
    elif key == keyboard.Key.down:  # Use the down key to decrease overlap count
        if overlap_count > 1:
            overlap_count -= 1
        print("overlap_count: ",overlap_count)
    elif key == keyboard.Key.space:  # Use the space key to toggle between modes
        sequential_mode = not sequential_mode
        print("secuential_mode: ",sequential_mode)

# Create a listener to capture keyboard input
listener = keyboard.Listener(on_release=on_key_release)
listener.start()

def play_random_video():
    random_video_file = random.choice(video_file_list)
    video_source = f"{video_directory}{random_video_file}"

    text = video_words_dict[random_video_file]

    print(text)
    # Set a random position for the video window
    window_x = random.randint(0, 1920)  # Adjust these values as needed
    window_y = random.randint(0, 1080)  # Adjust these values as needed

    mpv_command = [
        "mpv",
        video_source,
        #"--no-audio",  # Mute audio
        "--autofit=640x360", #1920x1080",  # Adjust to your desired video dimensions
        f"--geometry={window_x}:{window_y}",  # Set the window position
        "--on-all-workspaces",
        "--keep-open=no",  # Close mpv when playback ends
        "--no-osc",  # Disable on-screen controller
        "--no-input-default-bindings",  # Disable default input bindings
        "--screen=1",  # Set the specific screen
        "--no-border"  # Hide the video outline

    ]

    mpv_process = subprocess.Popen(mpv_command, stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    mpv_process.wait()

def overlap_mode(overlap_count):
    video_processes = []

    while True:
        # Ensure that there are always `overlap_count` videos playing
        if sequential_mode:
            return
        while len(video_processes) < overlap_count:
            if sequential_mode:
                return
            random_video_file = random.choice(video_file_list)
            text = video_words_dict[random_video_file]

            print(text)
            video_source = f"{video_directory}{random_video_file}"

            # Set a random position for the video window
            window_x = random.randint(0, 1920)  # Adjust these values as needed
            window_y = random.randint(0, 1080)  # Adjust these values as needed

            mpv_command = [
                "mpv",
                video_source,
                #"--no-audio",  # Mute audio
                #"--autofit=1920x1080",  # Adjust to your desired video dimensions
                "--autofit=640x360", #1920x1080",  # Adjust to your desired video dimensions
                f"--geometry={window_x}:{window_y}",  # Set the window position
                f"--screen={screen_number}",  # Set the specific screen
                "--on-all-workspaces",
                "--keep-open=no",  # Close mpv when playback ends
                "--no-osc",  # Disable on-screen controller
                "--no-input-default-bindings",  # Disable default input bindings
                "--no-border"  # Hide the video outline
            ]

            mpv_process = subprocess.Popen(mpv_command, stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            video_processes.append(mpv_process)

        # Check if any video processes have finished and replace them
        for i in range(len(video_processes)):
            if sequential_mode:
                return
            if video_processes[i].poll() is not None:
                random_video_file = random.choice(video_file_list)
                video_source = f"{video_directory}{random_video_file}"

                text = video_words_dict[random_video_file]

                print(text)
                # Set a random position for the new video window
                window_x = random.randint(0, 1920)  # Adjust these values as needed
                window_y = random.randint(0, 1080)  # Adjust these values as needed

                mpv_command = [
                    "mpv",
                    video_source,
                    #"--no-audio",  # Mute audio
                    #"--autofit=1920x1080",  # Adjust to your desired video dimensions
                    "--autofit=640x360", #1920x1080",  # Adjust to your desired video dimensions
                    f"--geometry={window_x}:{window_y}",  # Set the window position
                    f"--screen={screen_number}",  # Set the specific screen

                    "--on-all-workspaces",
                    "--keep-open=no",  # Close mpv when playback ends
                    "--no-osc",  # Disable on-screen controller
                    "--no-input-default-bindings",  # Disable default input bindings
                    "--no-border"  # Hide the video outline
                ]

                mpv_process = subprocess.Popen(mpv_command, stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
                video_processes[i] = mpv_process

        # Sleep for a short duration to prevent high CPU usage
        time.sleep(delay)

# Call overlap_mode with the desired overlap_count


while True:
    print("secuential_mode: ",sequential_mode)
    if sequential_mode:
        play_random_video()
        print(delay)
        time.sleep(delay)  # Use the current delay
         
    else:
        overlap_mode(overlap_count)


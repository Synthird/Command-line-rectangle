width_string: str = ""


def display_error():
    print("Cannot print a rectangle!")
    print("Probably because you entered:")
    print("a) Decimals\nb) Letters\nc) Symbols\nd) Spaces between numbers\ne) you typed a zero")
    raise SystemExit


def ask_question(prompt: str):
    print(f"--- What is the {prompt} of the rectangle? ---")
    try:
        number: int = int(input(f"{prompt.capitalize()}: "))
        if number > 0:
            return number
        else:
            raise ValueError
    except:
        display_error()


width: int = ask_question("width")
height: int = ask_question("height")

for _ in range(width):
    width_string = f"{width_string}."

for _ in range(height):
    print(width_string)

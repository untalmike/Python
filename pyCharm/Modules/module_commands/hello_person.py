def hello(name, lang):
    greetings = {
        "en": "Hello",
        "es": "Hola",
        "fr": "Bonjour",
        "de": "Hallo",
        "it": "Ciao",
        "pt": "Olá",
        "ru": "Привет",
        "zh": "你好",
        "ja": "こんにちは",
        "ko": "안녕하세요",
        "ar": "مرحبا",
        "hi": "नमस्ते",
        "tr": "Merhaba",
        "nl": "Hallo",
    }
    msg = f"{greetings[lang]} {name}!"
    print(msg)

# This script provides a personal greeting based on the provided name.
if __name__ == "__main__":

    import argparse # parser for command line arguments

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    # add an argument for the name of the person to greet
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="Name of the person to greet."
    )

    # add an argument for the language of the greeting
    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["en", "es", "fr", "it"], help="Language of the person to greet."
    )

    args = parser.parse_args()

    hello(args.name, args.lang)
    # when you run this script, you must provide an -h or --help option
    # to see the help message, or provide a name with -n or --name option
    # if no name is provided, it will raise an error
    # msg = f"Hello, {args.name}!"
    # print(msg) # send error message to stdout

    # so, you can run in command line like this:
    # python hello_person.py -n John
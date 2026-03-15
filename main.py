import argparse

from tkinterdnd2 import TkinterDnD

from decode_transliterate.gui import App
from decode_transliterate.processor import process_text


def run_gui():

    root = TkinterDnD.Tk()

    app = App(root)

    root.mainloop()


def run_cli(text: str, lang: str):

    result = process_text(text, lang)

    print(result)


def main():

    parser = argparse.ArgumentParser(
        description="Decode HTML entities and transliterate text"
    )

    parser.add_argument(
        "--cli",
        help="Run in CLI mode with provided text"
    )

    parser.add_argument(
        "--lang",
        default="ru",
        help="Language code (ru, el, uk)"
    )

    args = parser.parse_args()

    if args.cli:
        run_cli(args.cli, args.lang)
    else:
        run_gui()


if __name__ == "__main__":
    main()
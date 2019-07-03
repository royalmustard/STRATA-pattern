import sys
import Converter, UI


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    ui = UI.UI
    conv = Converter.Converter
    conv.load_image(ui.getPath())
    conv.convert_image_to_bmp()


if __name__ == "__main__":
    main()
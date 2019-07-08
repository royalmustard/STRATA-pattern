import sys
import UI


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    ui = UI.UI()


if __name__ == "__main__":
    main()
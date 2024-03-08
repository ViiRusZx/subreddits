from source.lib.parser import Parser

parser = Parser()


def main() -> None:
    print("Начали собирать данные:\n ТОП коментаторов\n")
    parser.print_top_authors_in_comments()
    print("***********************\n\n ТОП авторов постов\n")
    parser.print_top_authors_in_posts()


if __name__ == "__main__":
    main()

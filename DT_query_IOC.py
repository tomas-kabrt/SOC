import re
import logging as log
import IOC_file_extraction

verbose = True


def main():
    if verbose:
        log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        log.info("Verbose output.")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s")

    ioc, unknown = IOC_file_extraction.main()

    print(ioc)
    print(unknown)
    return ioc


if __name__ == "__main__":
    main()

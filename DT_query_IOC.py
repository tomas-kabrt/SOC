import re
import logging as log
import IOC_file_extraction

verbose = True


def generate_DT_query(ioc, source):

    return True


def main():
    if verbose:
        log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        log.info("Verbose output.")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s")

    ioc = IOC_file_extraction.main()

    log.info(ioc)

    generate_DT_query(ioc, "IP")

if __name__ == "__main__":
    main()

import re
import logging as log

verbose = True

def extractIOCfromFile():
    i = 0
    ioc = {}
    for line in open("ioc.txt", 'r'):
        i += 1
        parsed_ioc = line.split()
        var1 = parsed_ioc[0]

        if re.fullmatch(r'(?:https?://)?(?:www\.)?[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9]\.[a-zA-Z]{2,}', var1):
            log.info("Line %d contains string %s was detected as a domain." % (i, var1))
            ioc[var1] = 'domain'
        elif re.fullmatch(
                r'(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])',
                var1):
            log.info("Line %d contains string %s was detected as an IP." % (i, var1))
            ioc[var1] = 'IP'
        elif re.fullmatch(r'[a-f0-9]{32}([a-f0-9]{8})?([a-f0-9]{24})?', var1):
            log.info("Line %d contains string %s was detected as an hash." % (i, var1))
            ioc[var1] = 'hash'
        else:
            log.info("Line %d contains string %s was detected as a unknown." % (i, var1))
            ioc[var1] = 'unkown'

    return ioc



def main():
    if verbose:
        log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        log.info("Verbose output.")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s")

    ioc = extractIOCfromFile()

    print(ioc)


if __name__ == "__main__":
    main()

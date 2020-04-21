import re
import logging as log

verbose = False

def extractIOCfromFile():
    i = 0
    ioc = {}
    ioc['ip'] = []
    ioc['domain'] = []
    ioc['md5'] = []
    ioc['sha1'] = []
    ioc['sha256'] = []
    ioc['unknown'] = []

    for line in open("ioc.txt", 'r'):
        i += 1
        parsed_ioc = line.split()
        if parsed_ioc:
            var1 = parsed_ioc[0]

            m = re.search(r'^(?:https?://)?(?:www\.)?([a-zA-Z0-9][a-zA-Z0-9-.]{1,61}[a-zA-Z0-9]\.[a-zA-Z]{2,}|(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])+)', var1)
            if m:
                var1 = m.group(1)
                if re.fullmatch(r'(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])', var1):
                    log.info("Line %d contains string %s was detected as an IP." % (i, var1))
                    ioc['ip'].append(var1)
                else:
                    log.info("Line %d contains string %s was detected as a domain." % (i, var1))
                    ioc['domain'].append(var1)
            elif re.fullmatch(
                    r'(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])',
                    var1):
                log.info("Line %d contains string %s was detected as an IP." % (i, var1))
                ioc['ip'].append(var1)
            elif re.fullmatch(r'[a-fA-F0-9]{32}', var1):
                log.info("Line %d contains string %s was detected as a md5 hash." % (i, var1))
                ioc['md5'].append(var1)
            elif re.fullmatch(r'[a-fA-F0-9]{40}', var1):
                log.info("Line %d contains string %s was detected as a sha1 hash." % (i, var1))
                ioc['sha1'].append(var1)
            elif re.fullmatch(r'[a-fA-F0-9]{64}', var1):
                log.info("Line %d contains string %s was detected as a sha256 hash." % (i, var1))
                ioc['sha256'].append(var1)
            else:
                log.info("Line %d contains string %s was detected as a unknown." % (i, var1))
                #ioc['unknown'].append(var1)

    return ioc



def main():
    if verbose:
        log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        log.info("Verbose output.")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s")

    ioc = extractIOCfromFile()

    return ioc


if __name__ == "__main__":
    main()

import sys
import re
import logging as log

verbose = False

def extractIOCfromFile(fname):
    i = 0
    ioc = {'ip': {}, 'domain': {}, 'md5': {}, 'sha1': {}, 'sha256': {}, 'unknown': {}}

    try:
        f = open(fname, 'r')
    except OSError:
        print("Could not open/read file:" + fname)
        exit(1)

    for line in f:
        i += 1
        line = line.replace("[.]", ".")
        parsed_ioc = line.split()
        if parsed_ioc:
            var1 = parsed_ioc[0]

            m = re.search(r'^(?:h[tx]{2}ps?:\/\/)?(?:www\.)?((?:[a-zA-Z0-9]+\.)+[a-zA-Z]{2,}|(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])+)', var1)
            if m:
                var1 = m.group(1)
                if re.fullmatch(r'(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])', var1):
                    log.info("Line %d contains string %s was detected as an IP." % (i, var1))
                    ioc['ip'][var1] = None
                else:
                    log.info("Line %d contains string %s was detected as a domain." % (i, var1))
                    ioc['domain'][var1] = None
            elif re.fullmatch(
                    r'(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])',
                    var1):
                log.info("Line %d contains string %s was detected as an IP." % (i, var1))
                ioc['ip'][var1] = None
            elif re.fullmatch(r'[a-fA-F0-9]{32}', var1):
                log.info("Line %d contains string %s was detected as a md5 hash." % (i, var1))
                ioc['md5'][var1] = None
            elif re.fullmatch(r'[a-fA-F0-9]{40}', var1):
                log.info("Line %d contains string %s was detected as a sha1 hash." % (i, var1))
                ioc['sha1'][var1] = None
            elif re.fullmatch(r'[a-fA-F0-9]{64}', var1):
                log.info("Line %d contains string %s was detected as a sha256 hash." % (i, var1))
                ioc['sha256'][var1] = None
            else:
                log.info("Line %d contains string %s was detected as an unknown." % (i, var1))
                #ioc['unknown'].append(var1)

    ioc_list = {'ip': list(dict.fromkeys(ioc['ip'])), 'domain': list(dict.fromkeys(ioc['domain'])),
                'md5': list(dict.fromkeys(ioc['md5'])), 'sha1': list(dict.fromkeys(ioc['sha1'])),
                'sha256': list(dict.fromkeys(ioc['sha256'])), 'unknown': list(dict.fromkeys(ioc['unknown']))}
    return ioc_list


def main(argv):
    if len(argv) != 2:
        print('(+) usage: %s [ioc_file_name]' % argv[0])
        print('(+) eg: %s "ioc.txt"' % argv[0])
        sys.exit(-1)

    fname = argv[1]
    if verbose:
        log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        log.info("Verbose output.")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s")

    ioc = extractIOCfromFile(fname)

    return ioc


if __name__ == "__main__":
    main(sys.argv)

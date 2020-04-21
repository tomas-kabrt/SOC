import re
import logging as log
import IOC_file_extraction

verbose = True


def generate_DT_query(iocs, source):
    query = ''

    DT_query_mapping = {'ip': 'dest_ip:', 'md5': 'md5:', 'sha256': 'sha256:', 'domain': 'host:'}
    for ioc in iocs[source]:
        if query == '':
            query = '@fields.%s%s' % (DT_query_mapping[source], ioc)
        else:
            query += ' OR @fields.%s%s' % (DT_query_mapping[source], ioc)

    print(query)
    return True


def main():
    if verbose:
        log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        log.info("Verbose output.")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s")

    ioc = IOC_file_extraction.main()

    log.info(ioc)

    generate_DT_query(ioc, "ip")

if __name__ == "__main__":
    main()

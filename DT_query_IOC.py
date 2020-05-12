import logging as log
import IOC_file_extraction
from colorama import Fore, Back, Style

verbose = False
DT_Queries = True
fname = "ioc.txt"


def format_text(title, item):
    if item:
        cr = '\r\n'
        section_break = cr + "*" * 20 + cr
        title = str(title)
        item = str(item)
        text = Style.BRIGHT + Fore.GREEN + title + Fore.RESET + section_break + item + section_break
    else:
        text = ''
    return text


# format_query take in the account the 3k limit for advance search query lenght and devide the query into multiple queris if needed
def format_query(title, item):
    if item:
        cr = '\r\n'
        section_break = cr + "*" * 20 + cr
        title = str(title)
        item = str(item)
        text = Style.BRIGHT + Fore.GREEN + title + Fore.RESET + section_break + item + section_break
    else:
        text = ''
    return text


def generate_DT_query(iocs, source):
    query = ''
    line_number = 1

    DT_query_mapping = {'ip': 'dest_ip:', 'md5': 'md5:', 'sha256': 'sha256:', 'domain': 'host:*'}
    for ioc in iocs[source]:
        if query == '':
            query = '@fields.%s%s' % (DT_query_mapping[source], ioc)
        else:
            if len(query) > line_number * 2800:
                query += '\r\n@fields.%s%s' % (DT_query_mapping[source], ioc)
                line_number += 1
            else:
                query += ' OR @fields.%s%s' % (DT_query_mapping[source], ioc)

    return query


def main():
    if verbose:
        log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        log.info("Verbose output.")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s")

    ioc = IOC_file_extraction.main(["IOC_File_extraction", "%s" % fname])

    log.info(ioc)

    if DT_Queries:
        print(format_text("Extracted IP addresses in the DT query:", generate_DT_query(ioc, "ip")))
        print(format_text("Extracted Domain in the DT query:", generate_DT_query(ioc, "domain")))
        print(format_text("Extracted MD5 hashes in the DT query:", generate_DT_query(ioc, "md5")))
        print(format_text("Extracted SHA256 hashes in the DT query:", generate_DT_query(ioc, "sha256")))


if __name__ == "__main__":
    main()

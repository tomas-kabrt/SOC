import logging as log
import IOC_file_extraction
from colorama import Fore, Back, Style

verbose = False
DT_Queries = True
fname = "ioc.txt"

def fromat_text(title, item):
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

    DT_query_mapping = {'ip': 'dest_ip:', 'md5': 'md5:', 'sha256': 'sha256:', 'domain': 'host:*'}
    for ioc in iocs[source]:
        if query == '':
            query = '@fields.%s%s' % (DT_query_mapping[source], ioc)
        else:
            query += ' OR @fields.%s%s' % (DT_query_mapping[source], ioc)

    return query


def main():
    if verbose:
        log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        log.info("Verbose output.")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s")

    ioc = IOC_file_extraction.main(["IOC_File_extraction", "%s" %fname])

    log.info(ioc)

    if DT_Queries:
        print(fromat_text("Extracted IP addresses in the DT query:", generate_DT_query(ioc, "ip")))
        print(fromat_text("Extracted Domain in the DT query:", generate_DT_query(ioc, "domain")))
        print(fromat_text("Extracted MD5 hashes in the DT query:", generate_DT_query(ioc, "md5")))
        print(fromat_text("Extracted SHA256 hashes in the DT query:", generate_DT_query(ioc, "sha256")))

if __name__ == "__main__":
    main()

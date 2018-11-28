""" Assignment 01 in SC-T-308-PRLA """
from collections import Counter
import re
from pprint import pprint

LS_ORIGINAL_4 = """alarm            hidraw1             ppp     sda2      tty16  tty4   tty63      ttyS25   vcs8
ashmem           hpet                psaux   sda3      tty17  tty40  tty7       ttyS26   vcsa
autofs           input               ptmx    sda4      tty18  tty41  tty8       ttyS27   vcsa1
binder           kmsg                pts     sdb       tty19  tty42  tty9       ttyS28   vcsa2
block            libmtp-2-1.8.2      ram0    sdb1      tty2   tty43  ttyACM0    ttyS29   vcsa3
bsg              log                 ram1    sdb2      tty20  tty44  ttyACM1    ttyS3    vcsa4
btrfs-control    loop0               ram10   sdb5      tty21  tty45  ttyACM2    ttyS30   vcsa5
bus              loop1               ram11   serial    tty22  tty46  ttyprintk  ttyS31   vcsa6
cdc-wdm0         loop2               ram12   sg0       tty23  tty47  ttyS0      ttyS4    vcsa63
cdc-wdm1         loop3               ram13   sg1       tty24  tty48  ttyS1      ttyS5    vcsa7
cdc-wdm2         loop4               ram14   shm       tty25  tty49  ttyS10     ttyS6    vcsa8
char             loop5               ram15   snapshot  tty26  tty5   ttyS11     ttyS7    vga_arbiter
console          loop6               ram2    snd       tty27  tty50  ttyS12     ttyS8    vhost-net
core             loop7               ram3    stderr    tty28  tty51  ttyS13     ttyS9    video0
cpu              loop-control        ram4    stdin     tty29  tty52  ttyS14     uinput   watchdog
cpu_dma_latency  mapper              ram5    stdout    tty3   tty53  ttyS15     urandom  watchdog0
disk             mcelog              ram6    tpm0      tty30  tty54  ttyS16     v4l      watchdog1
dri              mei                 ram7    tty       tty31  tty55  ttyS17     vcs      watchdog2
ecryptfs         mem                 ram8    tty0      tty32  tty56  ttyS18     vcs1     zero
fb0              net                 ram9    tty1      tty33  tty57  ttyS19     vcs2
fb1              network_latency     random  tty10     tty34  tty58  ttyS2      vcs3
fd               network_throughput  rfkill  tty11     tty35  tty59  ttyS20     vcs4
full             null                rtc     tty12     tty36  tty6   ttyS21     vcs5
fuse             nvram               rtc0    tty13     tty37  tty60  ttyS22     vcs6
fw0              oldmem              sda     tty14     tty38  tty61  ttyS23     vcs63
hidraw0          port                sda1    tty15     tty39  tty62  ttyS24     vcs7"""


LS_ORIGINAL_3 = """Bill Bailey                                George Carlin
Billy Connolly                             Jimmy Carr
Chris Rock                                 Jon Richardson
Dara O'Briain                              Jon Richardson - Funny Magnet
Dara O'Briain - Craic Dealer               Kevin Smith
Dara O'Briain - Live at the Theatre Royal  Lee Mack
Dara O'Briain - Talks Funny                Louis CK
Dara O'Briain - This Is The Show           Michael McIntyre -Showtime
Dave Allen                                 Michael Mcintyre
Dylan Moran                                Neil Delamere
Dylan Moran - Like, Totally                Russell Howard
Dylan Moran - Monster                      Tim Minchin
Dylan Moran - What It Is Live              Tim Minchin - Ready For This
Ed Byrne                                   Tim Minchin - So Fucking Rock Live
Ed Byrne - Different Class Live            Tommy Tiernan
Ed Byrne - Pedantic And Whimsical          Tommy Tiernan - 'Cracked' Live at Vicar Street
Eddie Izzard                               Tommy Tiernan - Loose
Ellen DeGeneres"""

LS_ORIGINAL_2 = """bac kups  cache  crash  games  lib  local  lock  log  mail  met rics  opt  run  spool  tmp  www"""

LS_ORIGINAL = """acpid.pid     console-kit-daemon.pid  lock        pm-utils      sdp                      upstart-socket-bridge.pid
acpid.socket  crond.pid               mdm.pid     postgresql    sendsigs.omit.d          upstart-udev-bridge.pid
apache2       crond.reboot            mdm_socket  pppconfig     shm                      user
apache2.pid   cups                    motd        resol vconf   udev                     utmp
avahi-daemon  dbus                    mount       rsyslogd.pid  udisks                   wicd
console       dhclient.pid            network     samba         udisks2                  wpa_supplicant
ConsoleKit    initramfs               plymouth    screen        upstart-file-bridge.pid"""


LIST_X = ['acpid.pid',
          'console-kit-daemon.pid',
          'lock',
          'pm-utils',
          'sdp',
          'upstart-socket-bridge.pid',
          'acpid.socket',
          'acrond.pid',
          'mdm.pid',
          'postgresql',
          'sendsigs.omit.d',
          'upstart-udev-bridge.pid',
          'apache2',
          'crond.reboot',
          'mdm_socket',
          'pppconfig',
          'shm',
          'user',
          'apache2.pid',
          'cups',
          'motd',
          'resolvconf',
          'udev',
          'utmp',
          'avahi-daemon',
          'dbus',
          'mount',
          'rsyslogd.pid',
          'udisks',
          'wicd',
          'console',
          'dhclient.pid',
          'network',
          'samba',
          'udisks2',
          'wpa_supplicant',
          'ConsoleKit',
          'initramfs',
          'plymouth',
          'screen',
          'upstart-file-bridge.pid']


def cdo(string):
    """ Takes a string, sortes it and then returns a sorted string. """
    temp = sorted(string.split())
    return ' '.join(temp)


def duplicates(lis):
    """ Takes a list and returns the duplicates in the list. """
    counter = Counter(lis)
    return [x for x in counter if counter[x] > 1]


def flatten(lis):
    """ Take a list and flatten it. """
    temp_zip = zip(sorted(lis), range(len(lis)))
    temp_dict = {k: v for (k, v) in temp_zip}
    flat_list = []
    for num in lis:
        flat_list.append(temp_dict.get(num))
    return flat_list


def rm_duplicates(lis):
    """ Takes a list, removes duplicates and returns it sorted. """
    a_set = set(lis)
    return sorted(a_set)


def scramble(lis1, lis2):
    """ Takes two lists, one as values and the other as indies. Then sorts
    the value list according to the indies and returns a list. """
    temp_zip = zip(range(len(lis1)), lis1)
    temp_dict = {k: v for (k, v) in temp_zip}
    scrambled = []
    for num in lis2:
        scrambled.append(temp_dict.get(num))
    return scrambled


def excel_index(column):
    """ Takes a string and returns what column it would be in Excel. """
    letters = list(column.upper())
    power = len(column) - 1
    index = 0
    for letter in letters:
        index += 26**power * (ord(letter) - 64)
        power -= 1
    return index


def birthdays(string):
    """ Takes a multiline string and returns the numbers that represent
    the same dates."""
    kt_list = string.split()
    kt_filtered = [x for x in kt_list if x != '']
    kt_filtered = sorted(kt_filtered)
    bday_list = []
    for idx_i in kt_filtered:
        for idx_j in kt_filtered:
            if idx_i[0:4] == idx_j[0:4] and idx_i[4:] != idx_j[4:]:
                bday_list.append(idx_i)
                break
    final_list = set()
    for kennit in bday_list:
        string = kennit[0:4]
        temp = []
        for ktt in bday_list:
            if ktt.startswith(string):
                temp.append(ktt)
        final_list.add(tuple(temp))
    return list(final_list)


def filter_cleaner(string):
    return re.sub(r'~', '-', string)


def process_ls(string):
    """ Takes a multiline string and returns a sorted list. """
    reg_ex_str_0 = re.sub(r'\n', '}  ', string)
    reg_ex_str_1 = re.sub(r'(\s\s)|(\s{1}[^-]\s{1})', '?', reg_ex_str_0)
    # reg_ex_str_2 = re.sub(r'-', '~', reg_ex_str_1)
    reg_ex_list = re.split(r'\?', reg_ex_str_1)
    list_filtered = [x.strip() for x in reg_ex_list if x != '']
    row_end_index, mod_remainder = 0, 0
    for idx, line in enumerate(list_filtered):
        if line.find('}') != -1:
            list_min_length = (len(list_filtered) // (idx + 1))
            row_end_index = idx + 1
            mod_remainder = len(list_filtered) % (idx + 1)
            print(len(list_filtered),
                  list_min_length,
                  row_end_index,
                  mod_remainder,
                  idx)
            break
    processed_list, counter, processing = [], 0, True
    while processing:
        if row_end_index != 0:
            end_mark = list_min_length
            if counter < mod_remainder:
                end_mark += 1
            for idx in range(counter, len(list_filtered), row_end_index):
                list_filtered[idx] = list_filtered[idx].replace('}', '')
                processed_list.append(list_filtered[idx])
            counter += 1
            if counter == row_end_index:
                processing = False
        else:
            processed_list = list_filtered
            processing = False
    return processed_list
    # return [filter_cleaner(x) for x in processed_list]



# pprint(process_ls(LS_ORIGINAL))
# pprint(process_ls(LS_ORIGINAL_2))
# pprint(process_ls(LS_ORIGINAL_3))
pprint(process_ls(LS_ORIGINAL_4))


# print(process_ls(LS_ORIGINAL))
# print(process_ls(LS_ORIGINAL_2))
# print(process_ls(LS_ORIGINAL_3))
# print(process_ls(LS_ORIGINAL_4))

# print(LS_ORIGINAL_4)

# r'(\s\s)|(\n)|(\b\s([^-][\B]))|(([\B][^-])\s\b)', '?', string)
# r'(\s\s)|(\n)|(\b\s\B)|(\B\s\b)', '?', string)
# list_sorted = sorted(list_filtered, key=str.lower)
# for idx in range(len(list_sorted)):
# list_sorted[idx] = re.sub(r'~', r'-', list_sorted[idx])
# reg_ex_str_2 = re.sub(r'-', r'~', reg_ex_str_1)

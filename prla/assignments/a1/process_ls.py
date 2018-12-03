from itertools import zip_longest, chain


def process_ls(s):
    rs = s.splitlines()
    lis = [r.split('  ') for r in rs]
    for i, _ in enumerate(lis):
        lis[i] = [x.strip() for x in lis[i] if x != '']
    return [x for x in chain.from_iterable(zip_longest(*lis)) if x is not None]


print(process_ls("""acpid.pid     console-kit-daemon.pid  lock        pm-utils      sdp                      upstart-socket-bridge.pid
acpid.socket  crond.pid               mdm.pid     postgresql    sendsigs.omit.d          upstart-udev-bridge.pid
apache2       crond.reboot            mdm_socket  pppconfig     shm                      user
apache2.pid   cups                    motd        resolvconf    udev                     utmp
avahi-daemon  dbus                    mount       rsyslogd.pid  udisks                   wicd
console       dhclient.pid            network     samba         udisks2                  wpa_supplicant
ConsoleKit    initramfs               plymouth    screen        upstart-file-bridge.pid"""))

#define _GNU_SOURCE
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <dlfcn.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/utsname.h>
#include <stdarg.h>  // for va_start, va_arg, va_end

// Updated spoofed /etc/os-release content
static const char spoofed_os_release[] =
"NAME=\"SteamOS\"\n"
"PRETTY_NAME=\"SteamOS\"\n"
"VERSION_CODENAME=holo\n"
"ID=steamos\n"
"ID_LIKE=arch\n"
"ANSI_COLOR=\"1;35\"\n"
"HOME_URL=\"https://www.steampowered.com/\"\n"
"DOCUMENTATION_URL=\"https://support.steampowered.com/\"\n"
"SUPPORT_URL=\"https://support.steampowered.com/\"\n"
"BUG_REPORT_URL=\"https://support.steampowered.com/\"\n"
"LOGO=steamos\n"
"VARIANT_ID=steamdeck\n"
"VERSION_ID=3.6.20\n"
"BUILD_ID=20241030.1\n"
"STEAMOS_DEFAULT_UPDATE_BRANCH=stable\n";

// Updated spoofed /etc/lsb-release content (simplified to match the new info)
static const char spoofed_lsb_release[] =
"DISTRIB_ID=SteamOS\n"
"DISTRIB_RELEASE=3.6.20\n"
"DISTRIB_CODENAME=holo\n"
"DISTRIB_DESCRIPTION=\"SteamOS 3.6.20\"\n";

static const char spoofed_product_name[] = "Steam Deck\n";
static const char spoofed_board_name[] = "SteamDeckBoard\n";
static const char spoofed_bios_vendor[] = "Valve\n";
static const char spoofed_sys_vendor[] = "Valve\n";

struct spoof_file {
    const char *path;
    const char *content;
};

static struct spoof_file spoof_files[] = {
    { "/etc/os-release", spoofed_os_release },
    { "/etc/lsb-release", spoofed_lsb_release },
    { "/sys/class/dmi/id/product_name", spoofed_product_name },
    { "/sys/class/dmi/id/board_name", spoofed_board_name },
    { "/sys/class/dmi/id/bios_vendor", spoofed_bios_vendor },
    { "/sys/class/dmi/id/sys_vendor", spoofed_sys_vendor },
    { NULL, NULL }
};

// Helper to find spoofed content by path
static const char *get_spoofed_content(const char *path) {
    for (int i = 0; spoof_files[i].path != NULL; i++) {
        if (strcmp(path, spoof_files[i].path) == 0) {
            return spoof_files[i].content;
        }
    }
    return NULL;
}

// ---------- Hook fopen ----------

typedef FILE *(*orig_fopen_f_type)(const char *pathname, const char *mode);

FILE *fopen(const char *pathname, const char *mode) {
    static orig_fopen_f_type orig_fopen = NULL;
    if (!orig_fopen) {
        orig_fopen = (orig_fopen_f_type)dlsym(RTLD_NEXT, "fopen");
    }

    const char *spoof = get_spoofed_content(pathname);
    if (spoof) {
        // Create a temporary FILE * from memory for the spoofed content
        return fmemopen((void *)spoof, strlen(spoof), mode);
    }

    return orig_fopen(pathname, mode);
}

// ---------- Hook open ----------

typedef int (*orig_open_f_type)(const char *pathname, int flags, ...);

int open(const char *pathname, int flags, ...) {
    static orig_open_f_type orig_open = NULL;
    if (!orig_open) {
        orig_open = (orig_open_f_type)dlsym(RTLD_NEXT, "open");
    }

    const char *spoof = get_spoofed_content(pathname);
    if (spoof) {
        int pipefd[2];
        if (pipe(pipefd) == -1) {
            // fallback to original open if pipe fails
            va_list args;
            va_start(args, flags);
            int fd;
            if (flags & O_CREAT) {
                mode_t mode = va_arg(args, mode_t);
                fd = orig_open(pathname, flags, mode);
            } else {
                fd = orig_open(pathname, flags);
            }
            va_end(args);
            return fd;
        }
        write(pipefd[1], spoof, strlen(spoof));
        close(pipefd[1]);
        return pipefd[0];
    }

    va_list args;
    va_start(args, flags);
    int fd;
    if (flags & O_CREAT) {
        mode_t mode = va_arg(args, mode_t);
        fd = orig_open(pathname, flags, mode);
    } else {
        fd = orig_open(pathname, flags);
    }
    va_end(args);

    return fd;
}

// ---------- Hook read ----------

typedef ssize_t (*orig_read_f_type)(int fd, void *buf, size_t count);

ssize_t read(int fd, void *buf, size_t count) {
    static orig_read_f_type orig_read = NULL;
    if (!orig_read) {
        orig_read = (orig_read_f_type)dlsym(RTLD_NEXT, "read");
    }
    return orig_read(fd, buf, count);
}

// ---------- Hook uname ----------

typedef int (*orig_uname_f_type)(struct utsname *buf);

int uname(struct utsname *buf) {
    static orig_uname_f_type orig_uname = NULL;
    if (!orig_uname) {
        orig_uname = (orig_uname_f_type)dlsym(RTLD_NEXT, "uname");
    }

    int ret = orig_uname(buf);
    if (ret == 0) {
        strncpy(buf->sysname, "Linux", sizeof(buf->sysname));
        strncpy(buf->nodename, "steamdeck", sizeof(buf->nodename));
        strncpy(buf->release, "6.5.0-valve23-1-neptune-65-g385b5e207ae2", sizeof(buf->release));
        strncpy(buf->version, "#1 SMP PREEMPT_DYNAMIC SteamOS", sizeof(buf->version));
        strncpy(buf->machine, "x86_64", sizeof(buf->machine));
    }
    return ret;
}

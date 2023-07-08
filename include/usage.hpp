#ifndef __USAGE__
#define __USAGE__

#include <iostream>

static void usage()
{
    std::cout   << "Usage: keysound [OPTION]...\n"
                << "Play sound while pressed keyboard keys.\n"
                << "\n"
                << "  -f, --file=WAV_FILE        play sound use FILE\n"
                << "  -j, --json=JSON_FILE       config keyboard sound by json\n"
                << "  -d, --dir=DIR              config keyboard sound by direction\n"
                << "  -l, --log=LOG_FILE         log file (not implemented)\n"
                << "  -D, --daemon               run in background\n"
                << "  -k, --kill                 stop all\n"
                << "  -v  --verbose              print key presses\n"
                << "  -?, -h, --help             help\n";
}

#endif

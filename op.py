import time
import os
z= 1
a=[ " "
,"               China Red                                                 "
,"        __________    __________                       _____              "
,"       /$_$_$_$_$/    |$|$_$_$_$\                     /####.\__           "
,"      /$/             |$|      \$\                   /######/             "
,"     /$/              |$|       |$|                 /#####/               "
,"     |$|              |$|______/$/                 /|#####\   ____  ____  "
,"     |$|              |$|$_$_$_$/                 /#|####\ \ /####\/####\ "
,"     |$|              |$|\$\                        |####|\  |/  \##/  \| "
,"     |$|              |$| \$\                        \###\       /#/      "
,"     \$\              |$|  \$\                        \###\_____/#/       "
,"      \$\_________    |$|   \$\                        \#########/        "
,"       \$_$_$_$_$/    |$|    \$\                                          "
,"                                                                          "
]
for _ in range(12):
    z+=1  
    time.sleep(0.016666666667)
    print(a[z])
time.sleep(1.5)
import sys

from mcdreforged.__main__ import main

if __name__ == '__main__':
	sys.exit(main())
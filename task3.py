good = r"""
          __
         /\ `.
         2^)_|
         \`/(_
           )/,`.
        __((  \/
       /.--|_.L\\_
           \, \ \=
           / ,/L
          7 (\ \...,_
          | | \____| )
          ]_|      `\)
          /_)  SK
         `"
"""
bad = r"""
                        ,////,
                        /// 6|
                        //  _|
                       _/_,-'
                  _.-/'/   \   ,/;,
               ,-' /'  \_   \ / _/
               `\ /     _/\  ` /
                 |     /,  `\_/
                 |     \'
 pb  /\_        /`      /\
   /' /_``--.__/\  `,. /  \
  |_/`  `-._     `\/  `\   `.
            `-.__/'     `\   |
                          `\  \
                            `\ \
                              \_\__
                               \___)
"""
guard_awake = False
if not guard_awake:
    outcome = "Shadow: Let's tiptoe past quietly."
    print(good)
else:
    outcome = "Doom: Oh No!!! Run!!!"
    print(bad)
print(outcome)
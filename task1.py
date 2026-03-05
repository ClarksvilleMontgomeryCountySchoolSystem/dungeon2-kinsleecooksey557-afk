good = r"""
       .
      / )
      ) /
     (.;
      )
     (.
      ,---Q
     |_/ |_
     |____/
     |    |
     |    |
     |++++|
     |".".|
     |++++|
     |    |
     |____|   arm
"""
bad = r"""

               ,-=-.
              /     )
             (  c/=(
              `-( _/
              _/ (_
            /  `-- )
          <  ,   ) )>
        /  \/ \   (/\
      / ,'    )    \  \
  -=` /      /     |    \
   \-`      /      |   '\|
           <_./    \
          /        |
         /   ,     \
        <,_./      |
       /           |
      /_           |
     |  ``--.__.-='!
     | /         \ !
'`'"' ("" '`'`"' `) \_'"'`"" "``''"''`" "'"`'''
    (_ \_        '"`=-'`"               `" "
  '"" `-'`"            '"'`'
         '`'"'                     '""`'"
"""
torch_lit = True
if torch_lit:
    outcome = "Flicker: Thank goodness I can see!"
    print(good)
else:
    outcome = "Doom: Welp. Looks like we're going blind."
    print(bad)
print(outcome)
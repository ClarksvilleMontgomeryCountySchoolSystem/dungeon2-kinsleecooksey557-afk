good = r"""
-=[ key ]=-  4/99
         .--.
        /.-. '----------.
        \'-' .--"--""-"-'
     jgs '--'
"""
bad = r"""
      ______
   ,-' ;  ! `-.
  / :  !  :  . \
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|
"""
has_key = True
if not has_key:
    outcome = "Doom: I need to find a way to get this door open."
    print(bad)
else:
    outcome = "Click: Here goes nothing."
    print(good)
print(outcome)
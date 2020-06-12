from mcrcon import MCRcon

def warn_players():

    with MCRcon("45.35.98.71", "V7FG8sjA", 28016) as mcr:
        resp = mcr.command("broadcast server restarting in 30 seconds")
        print(resp)

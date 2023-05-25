import menuTemplate as mt

x = mt.menu_handler()
mt.signal.signal(mt.signal.SIGINT, mt.sigint_handler)

while True:
    x.menuExecution()
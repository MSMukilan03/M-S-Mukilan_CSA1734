def reflex_agent(location, status):
    if status == "Dirty":
        return "Suck"
    return "Right" if location == "A" else "Left"
 
def run(env, location, steps=6):
    print("Initial:", env, "agent at", location)
    for t in range(1, steps + 1):
        action = reflex_agent(location, env[location])
        if action == "Suck":
            env[location] = "Clean"
        elif action == "Right":
            location = "B"
        else:
            location = "A"
        print("Step %d: action=%-5s -> agent at %s, world=%s" % (t, action, location, env))
 
run({"A": "Dirty", "B": "Dirty"}, "A")

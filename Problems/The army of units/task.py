enemies_num = int(input())
if enemies_num >= 1000:
    print("legion")
elif 500 <= enemies_num < 1000:
    print("swarm")
elif 50 <= enemies_num < 500:
    print("horde")
elif 10 <= enemies_num < 50:
    print("pack")
elif 1 <= enemies_num < 10:
    print("few")
elif enemies_num < 1:
    print("no army")

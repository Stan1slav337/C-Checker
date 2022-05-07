import subprocess, os

exepath = os.getcwd() + "\main.exe"
path = "\\".join(
    exepath.split("\\")[:-1:])

name = 1

while True:

    try:
        fin = open(str(path + '\\' + "%01d" % name) + '.in', 'r')
    except:
        break
    fout = open(str(path + '\\' + "%01d" % name) + '.out', 'r')

    p = subprocess.Popen(exepath, stdin=fin, stdout=subprocess.PIPE)
    p_out = p.communicate()[0].decode('utf-8')
    l1 = list(p_out.split("\n"))
    l2 = fout.readlines()

    if l1[-1] == '':
        l1.pop()

    fin = open(str(path + '\\' + "%01d" % name) + '.in', 'r')
    print("Test: #" + str(name))
    print("Input:")
    print("".join(fin.readlines()) + "\n")
    print("Output:")
    print(p_out + '\n')
    print("Answer:")
    print("".join(l2) + '\n')

    ok = True

    if len(l1) == len(l2):
        for line1, line2 in [(l1[i], l2[i]) for i in range(len(l2))]:
            ok = ok and line1[:len(line1) - 1] == line2[:len(line2) - 1]
    else:
        ok = False

    print("Verdict: " + ("OK" if ok else "WRONG ANSWER") + "\n")

    if not ok:
        break

    name += 1

input()

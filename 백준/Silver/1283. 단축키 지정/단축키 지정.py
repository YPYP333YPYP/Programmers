N = int(input())

strings = []

for _ in range(N):
    strings.append(str(input()))


sdict = dict()

for string in strings:
    ch = ""
    if " " in string:
        tmp_list = string.split(" ")
        for i,val in enumerate(tmp_list):
            start = val[0].upper()
            if start not in sdict:
                tmp_list[i] = list(tmp_list[i])
                sdict[start] = val
                ch = val[0]
                tmp_list[i][0] = f"[{ch}]"
                tmp_list[i] = ("".join(tmp_list[i]))
                print(" ".join(tmp_list))
                break

        if ch == "":
            for v in string:
                if v != " ":
                    tmp = v.upper()

                    if tmp not in sdict:
                        sdict[tmp] = string
                        ch = v
                        break
                    else:
                        continue

            nlist = list(string)
            for v in nlist:
                if ch == v:
                    idx = nlist.index(ch)
                    nlist[idx] = f"[{ch}]"
                    break

            print("".join(nlist))
    else:
        for v in string:
            tmp = v.upper()

            if tmp not in sdict:
                sdict[tmp] = string
                ch = v
                break
            else: continue

        nlist = list(string)
        for v in nlist:
            if ch == v:
                idx = nlist.index(ch)
                nlist[idx] = f"[{ch}]"
                break

        print("".join(nlist))



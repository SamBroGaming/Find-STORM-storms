x = False
y = 0
z = 0
ind = ""
dict_1 = {}
sshws = 185/2.55
pressure = 880
dict_2 = {0 : 'NA', 1 : 'EP', 2 : 'WP', 3 : 'NI', 4 : 'SI', 5 : 'SP'}
for j in range(10):
    with open(F"STORM_DATA_IBTRACS_SP_1000_YEARS_{j}.txt", "r") as f:
        data = f.read()
        data = data.split('\n')
        for i in range(len(data)-1):
            row = data[i].split(',')
            ind = str(j) + "_" + str(row[0]).strip() + "_" + str(row[2]).strip()
            if float(row[8].strip()) > sshws:
                if ind not in dict_1.keys():
                    dict_1[ind] = float(row[8].strip())
                else:
                    dict_1[ind] = dict_1[ind] + 1
                    if dict_1[ind] < float(row[8].strip()):
                        dict_1[ind] = float(row[8].strip())
    for i in dict_1.keys():
            print(dict_1[i])

    print(len(dict_1))

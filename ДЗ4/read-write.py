import json

i = 0
with open("purchase_log.txt") as f:
    for line in f:
        line = line.strip()

        dict_parchase_log = json.loads(line)
        # print(dict_parchase_log)
        with open("purchases.csv", "a") as f2:
            f2.write(
                f"{dict_parchase_log['user_id']},{dict_parchase_log['category']}\n"
            )
        # i += 1
        # if i > 5:
        #    break

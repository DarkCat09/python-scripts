print("")
print("*** EXERCISE BRUTEFORCE ***")
print("")

light_count = 120
lamps_in_chnd = 1
lamps_in_scn = 3

chnd_lamps_count = 0
scn_lamps_count = 0
solved = False

for chnd_count in range(light_count+1):
	for scn_count in range(light_count+1):
		#if (chnd_count + scn_count) > light_count:
			#continue
		chnd_lamps_count = lamps_in_chnd * chnd_count
		scn_lamps_count = lamps_in_scn * scn_count
		solved = (chnd_lamps_count == scn_lamps_count) and (chnd_lamps_count > 0) and (scn_lamps_count > 0)
		print(chnd_lamps_count, chnd_count, scn_lamps_count, scn_count, solved)
		if (solved):
			print("OK")
			break
	if (solved):
		break

print("")
print("Finished")
input("")

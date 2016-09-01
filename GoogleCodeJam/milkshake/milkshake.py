
def solve(case, ms_types, customers):
   result = [0] * ms_types
	
   solved = False
   impossible = False
   while not solved and not impossible:
	restart = False
	for customer in customers:
		unsatisfied = []
		for type_shake, malted in customer:
			if result[type_shake-1] == malted:
				unsatisfied = []
				break #one satisfied, move to the next customer
			else:
				unsatisfied.append((type_shake, malted))
		
		for t, m in unsatisfied:
			if m == 1:
				result[t-1] = 1
				restart = True
				break

		if restart:
			break
		
		if len(unsatisfied) > 0:
			impossible = True
			break

	if not restart and not impossible:
		solved = True

   if solved:
   	print "Case #%d: %s" % (case, ' '.join(map(str, result)))
   else:
	print "Case #%d: IMPOSSIBLE" % case

def main():
	cases = int(raw_input())
	for case in range(cases):
		ms_types = int(raw_input())
		n_customers = int(raw_input())
		customers = []
		for c in range(n_customers):
			cinfo = map(int, str(raw_input()).split())
			customer = []
			for l in range(1, cinfo[0]*2, 2):
				customer.append((cinfo[l], cinfo[l+1]))
			customers.append(customer)
	
		solve(case+1, ms_types, customers)

if __name__ == "__main__":
	main()

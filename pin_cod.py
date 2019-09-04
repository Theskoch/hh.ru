#!/usr/bin/env python3
import datetime


def start(pin):

	len_v = len(pin)

	if len_v <=8:

		mass1=[[-1]]*len_v

		for i in range(len_v):
			if pin[i] == '0':
				mass1 [i] = [0,8]
			
			elif pin[i] == '1':
				mass1 [i] = [1,2,4]

			elif pin[i] == '2':
				mass1 [i] = [1,2,3,5]

			elif pin[i] == '3':
				mass1 [i] = [2,3,6]

			elif pin[i] == '4':
				mass1 [i] = [1,4,5,7]

			elif pin[i] == '5':
				mass1 [i] = [2,4,5,6,8]

			elif pin[i] == '6':
				mass1 [i] = [3,5,6,9]

			elif pin[i] == '7':
				mass1 [i] = [4,7,8]

			elif pin[i] == '8':
				mass1 [i] = [0,5,7,8,9]

			elif pin[i] == '9':
				mass1 [i] = [6,8,9]

		mass = []

		for i in range(len(mass1[0])):
			g = str(mass1[0][i])

			if len_v>1:
				for j in range(len(mass1[1])):
					g = g[0] + str(mass1[1][j])

					if len_v>2:
						for h in range(len(mass1[2])):
							g = g[0:2] + str(mass1[2][h])

							if len_v>3:
								for q in range(len(mass1[3])):
									g = g[0:3] + str(mass1[3][q])

									if len_v>4:
										for p in range(len(mass1[4])):
											g = g[0:4] + str(mass1[4][p])

											if len_v>5:
												for t in range(len(mass1[5])):
													g = g[0:5] + str(mass1[5][t])

													if len_v>6:
														for u in range(len(mass1[6])):
															g = g[0:6] + str(mass1[6][u])

															if len_v>7:
																for u in range(len(mass1[7])):
																	g = g[0:7] + str(mass1[7][u])
																	mass.append(g)
															else:
																mass.append(g)
													else:
														mass.append(g)
											else:
												mass.append(g)
									else:
										mass.append(g)
							else:
								mass.append(g)
					else:
						mass.append(g)
			else:
				mass.append(g)
	

	print(','.join(mass))

	return


pin = input()
dex = datetime.datetime.now().time()
start(pin)
dex_2= datetime.datetime.now().time()
print (dex)
print(dex_2)
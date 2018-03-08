from time import sleep, clock, time

def main():
	startTime = time()
	print(startTime)
	sleep(5)
	print("done!")
	endTime = time()
	print(endTime)
	totalTime = endTime - startTime
	print(totalTime)


if __name__ == "__main__":
	main()
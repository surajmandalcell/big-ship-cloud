# Python program to illustrate the concept
# of threading
# importing the threading module
import threading


def print_cube(num):
	print(num)


def print_square(link,num):
	print(link)
	print(num)


if __name__ =="__main__":
	# creating thread
	t1 = threading.Thread(target=print_square, args=("linksss",10))
	t2 = threading.Thread(target=print_cube, args=(10,))

	# starting thread 1
	t1.start()
	# starting thread 2
	t2.start()

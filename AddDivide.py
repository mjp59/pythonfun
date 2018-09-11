def main():
 	mid = add_three(3, 5, 10)
 	ans = divide_bythree(mid)
 	print(ans)

def add_three(v1, v2, v3):
	
 	p = v1 + v2 + v3
 	
 	return p
 
def divide_bythree(v1):
	p = v1 / 3
	return p

if __name__== "__main__":
	 main()
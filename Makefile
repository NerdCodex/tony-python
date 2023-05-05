default:
	pyinstaller --name tony --onefile tony.py
	cp dist/tony /bin
	rm -rf build/ dist/ tony.spec

clean:
	rm /bin/tony
	clear

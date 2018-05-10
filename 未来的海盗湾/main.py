import requests
from bs4 import BeautifulSoup
from flask import Flask,render_template,request

app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def index():
	if request.method == 'GET':
		return render_template('index.html')
	elif request.method == 'POST':
		#种子搜索部分
		seach_name = request.form.get('search')
		seach_link = []
		seach_data_name = []
		import_data=[]
		
		for i in range(1,2):
			html = 'http://www.btrabbit.net/search/'+str(seach_name)+'/default-'+str(i)+'.html'
			r = requests.get(html,timeout=10)
			r.encoding = r.apparent_encoding
			soup = BeautifulSoup(r.text,"html.parser")
			div_all = soup.find_all('div',class_='search-item detail-width')

			for each in div_all:
				
			
				seach_data_name.append(each.get_text())
				
				for s in each.find_all('a'):
					
					seach_link.append(s.get('href'))
		for super_man in range(2,30,3):
			print(seach_link[super_man])
			import_data.append(seach_link[super_man])
			
			
		return render_template('main.html',seach_data_name=seach_data_name,import_data=import_data)
			
if __name__ =="__main__":
	app.debug = True
	app.run(host="0.0.0.0")
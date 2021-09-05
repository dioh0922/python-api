import markovify					#マルコフ連鎖で文章を生成するライブラリ

#教師データのファイルを指定して文章を生成する処理
def generate_model(mode):
	#現代語訳の孫子全文を読み出す
	f_name = "token_chn.txt"
	if(mode == "jpn"):
		f_name = "token_jpn.txt"

	text = read_file_text(f_name)
	#tokenizer = Tokenizer()
	#str = split_part_of_speach(text)

	model = markovify.NewlineText(text)	#1行ごとに読んでマルコフ連鎖のモデルとする

	return model

#ファイルを読み出す処理
def read_file_text(f_name):
	with open(f_name, encoding="utf-8") as fs:
		text = fs.read()

	return text

import emoji

top = 0
bot = 0
meio = 0
N = int(input('Informe o tamanho da figura: '))
n_of_black_hearts = 0
black_heart = emoji.emojize(":black_circle:")
n_of_purple_hearts = int(N/2)
purple_heart = emoji.emojize(":purple_heart:")


while top < N/2:
	print(n_of_black_hearts * black_heart, n_of_purple_hearts * purple_heart + purple_heart + n_of_purple_hearts * purple_heart, n_of_black_hearts * black_heart)
	top += 1
	n_of_black_hearts += 1
	n_of_purple_hearts -= 1

while meio < N/2:
	print(n_of_black_hearts * black_heart, purple_heart, n_of_black_hearts * black_heart)
	meio += 1

#n_of_purple_hearts --> 0
#n_of_black_hearts --> 5

n_of_black_hearts = n_of_black_hearts - 1
n_of_purple_hearts = n_of_purple_hearts + 1
while bot < N/2:
	print(n_of_black_hearts * black_heart,n_of_purple_hearts * purple_heart + purple_heart + n_of_purple_hearts * purple_heart , n_of_black_hearts * black_heart)
	bot += 1
	n_of_black_hearts -= 1
	n_of_purple_hearts += 1

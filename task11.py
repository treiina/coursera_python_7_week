# Выборы президента, почему-то так и не принято курсерой...
inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
info = inFile.read().splitlines()
voices_spreading = {}.fromkeys(info, 0)
for i in info:
    voices_spreading[i] += 1
list_voices_spreading = list(voices_spreading.items())
list_voices_spreading.sort(key=lambda x: x[1], reverse=True)
if int(list_voices_spreading[0][1])/len(info) > 0.5:
    print(list_voices_spreading[0][0], file=outFile)
else:
    print(list_voices_spreading[0][0], list_voices_spreading[1][0], sep='\n', file=outFile)
inFile.close()
outFile.close()

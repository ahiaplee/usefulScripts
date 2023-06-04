""" Script to create batch file with commands to cut and convert music compilations into individual mp3s
"""

data = [
["00:00:00", "Hello World - JustinOverFlow"],
["00:03:33", "FooBar - FooSmith"],
]

f = open("extract1.bat", "w", encoding='utf-8')
f.write("chcp 65001\n")
f.write("chcp\n")
for i in range(len(data)):
    if(i + 1) == len(data):
        break
    command = "ffmpeg -i source.mp4 -ss {startTime} -to {endTime} -q:a 0 -map a {trackName}.mp3\n".format(
            startTime = data[i][0], endTime = data[i+1][0], trackName = data[i][1]
        )
    print(command)
    f.write(command)

f.close()

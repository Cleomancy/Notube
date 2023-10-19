import os
import random
# opening the file in read mode 
set_playlist = open(input("name of list")+".m3u", "r") 
  
# reading the file 
data = set_playlist.read() 
  
# replacing end splitting the text  
# when newline ('\n') is seen. 
data_into_list = data.split("\n")
random.shuffle(data_into_list)
set_playlist.close() 

end = open("random.m3u","w")
for i in data_into_list:
	end.write(i+"\n")
end.close()
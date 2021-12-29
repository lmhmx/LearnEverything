# repeatwork.py

you can change the `command` in the file and excute it in your python environment.

# passwd.py

* the tool give you the chance that encode your passwd yourself. Since the code is open, you can make sure that the encoding is absolutely safe.

## introduction

the code encode your message by a passwd by change the message and the passwd to a number. the passwd number is used to seed the random and the generate the extend passwd string with a large length. then the extend passwd can be changed into a number and multiply it with the message number. We store the result of the number in a file. When we want to decode the file, we need to input the passwd so that we can get the extend passwd number. Then we divide the passwd number by the file number to get the message. 

> I don't check the difficulty and the passwd conflicts of the algorithm. **Be careful of this**.

## usage 

* -p: change the passwd
* -a+itemname: add an item to your passwd table
* -e+itemname: edit an item
* -l: list all the items, but hide the passwd
* -w+item: list all the items that contains the item. Support **\*** to reprsent everything
* -t+time: give the watching time before clear the screen
* -d+item: delete an item
* -s+size: give the length of the passwd to be extended
* -n+newsize: give the length of the new passwd to be extended if you want to update the passwd
* -i+inputfile: give the inputfile to be decoded
* -o+outputfile: give the outputfile of the passwd. **Note: this export the orginal passwd, be careful**

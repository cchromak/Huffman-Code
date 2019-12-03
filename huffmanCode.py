from heapq import heappush, heappop, heapify
from collections import defaultdict
 
def encode(n): #passing a dictionary
    heap = [[wt, [sym, ""]] for sym, wt in n.items()] 
    heapify(heap)               # .items lets retrive value and key
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
 
txt = """Is this the real life?
Is this just fantasy?
Caught in a landslide,
No escape from reality.

Open your eyes,
Look up to the skies and see,
I'm just a poor boy, I need no sympathy,
Because I'm easy come, easy go,
Little high, little low,
Any way the wind blows doesn't really matter to me, to me.

Mama, just killed a man,
Put a gun against his head,
Pulled my trigger, now he's dead.
Mama, life had just begun,
But now I've gone and thrown it all away.

Mama, ooh,
Didn't mean to make you cry,
If I'm not back again this time tomorrow,
Carry on, carry on as if nothing really matters.

Too late, my time has come,
Sends shivers down my spine,
Body's aching all the time.
Goodbye, everybody, I've got to go,
Gotta leave you all behind and face the truth.

Mama, ooh (any way the wind blows),
I don't wanna die,
I sometimes wish I'd never been born at all.

I see a little silhouetto of a man,
Scaramouche, Scaramouche, will you do the Fandango?
Thunderbolt and lightning,
Very, very frightening me.
(Galileo) Galileo.
(Galileo) Galileo,
Galileo Figaro
Magnifico-o-o-o-o.

I'm just a poor boy, nobody loves me.
He's just a poor boy from a poor family,
Spare him his life from this monstrosity.

Easy come, easy go, will you let me go?
Bismillah! No, we will not let you go. (Let him go!)
Bismillah! We will not let you go. (Let him go!)
Bismillah! We will not let you go. (Let me go!)
Will not let you go. (Let me go!)
Never let you go (Never, never, never, never let me go)
Oh oh oh oh
No, no, no, no, no, no, no
Oh, mama mia, mama mia (Mama mia, let me go.)
Beelzebub has a devil put aside for me, for me, for me.

So you think you can stone me and spit in my eye?
So you think you can love me and leave me to die?
Oh, baby, can't do this to me, baby,
Just gotta get out, just gotta get right outta here.

(Ooooh, ooh yeah, ooh yeah)

Nothing really matters,
Anyone can see,
Nothing really matters,
Nothing really matters to me.

Any way the wind blows."""

n = defaultdict(int)
for ch in txt:
    n[ch] += 1

huff = encode(n)

print ("Symbol\tWeight\tHuffman Code")
for p in huff:
    print ("%s\t%s\t%s" % (p[0], n[p[0]], p[1]))
dic = {}

for p in huff:
    dic[p[0]] = p[1] # creates dictionary of symbols and their coresponding bit

print()
print('Here is the newly created huffcode put into a dictionary:')
print (dic)

huffstr = ''
for n in txt:
    huffstr = huffstr + dic[n] # creates string of bits

print()
print('Here is the code put together as a string:')
print (huffstr)


inv_dic = {y:x for x,y in dic.items()}
print()
print('Here is the fliped dictionary to be used to read and decode the code:')
print (inv_dic)  # creates flipped dictionary where bits are first, then symbols
print()

print('Here are the decoded lyrics:')
def decode(inv_dic, huffstr):  #this function passes the flipped dictionary and string
    hold = ''                   # empty string to temporarily hold the bit code to check if it's in the dictionary           
    for i in huffstr:           # loop to walk through string
        hold += i
        if hold in inv_dic:     # checks if in dictionary
            print(inv_dic[hold], end='')  #if it is it prints it
            hold = ''           #brings hold back to an empty string once completed

    
decode(inv_dic, huffstr)
        
        
    



import re

pattern= r"India+[a-z]"
text= '''
Amid growing calls for ending the outsourcing of work to Indian firms, it is yet unclear if Trump is 
considering imposing restrictions on the same.
However, conservatives in the US are voicing their opposition to outsourcing work to Indian companies.
“Countries must pay for the privilege of providing services remotely to the US, the same way as goods. 
Apply across industries, levelled as necessary per country,” right-wing commentator Jack Poso said
The Trump supporter’s post on X also raised a stereotype about Indian call centres that supposedly pose 
language barriers for foreigners. However, the data paints a different picture.
Pew Research has proved that around 84% of Indians above 5 years of age are proficient in English. 
This population includes 28% people who interact only in English at home and 56% who speak another language at home 
but speak English very well, Hindustan Times reported.
'''
match = re.search(pattern,text)
matchitr= re.finditer(pattern,text)
# print(match)
count=0
for m in matchitr:
    print(m)
    count+=1
    print(f"Having count: {count}")
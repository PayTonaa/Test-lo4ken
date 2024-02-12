# dictionary =
# A changeable, unordered collection of unique key: value pairs Fast because they use hashing, allow us to access a value quickly


capitals = {'USA' : 'Wahigton',
            'Polska':'Warszawa',
            'Chiny':'Pekin',
            'Rosja':'Moskwa'}

capitals.update({'Germany':'Berlin'}) # dodaje klucz
capitals.update({'USA':'New York'}) # zaminia wartość klucza
capitals.pop('China') #usuwa określony
capitals.clear() #usuwa wszystko

print(capitals['Rosja'])
print(capitals.get('Germany')) #sprawdza czy cos jest w moim słowniku
print(capitals.keys()) # tylko klucze
print(capitals.values()) # tylko argumenty
print(capitals.items()) # wszystko

for key,value in capitals.items():
    print(key, value)
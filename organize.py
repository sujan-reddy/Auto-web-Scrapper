import os

dept=['AD','AE','AI','AM','CS','CV','EC','EE','IS','ME']
year=['19','20','21','22']


for d in dept:
    for y in year:
        path='TEXTFILES LOG/'+d + '/' + y + '/INDIVIDUAL TEXT FILES'
        # f=open('TEXTFILES LOG/'+d + '/' + y + '/TOTAL TEXT FILE NO NULL.txt','a+')
        for filename in os.listdir(path):
            individual_file=open(path+'/'+filename)
            content=individual_file.read()
            content.strip(' \n')
            if (content.split(' ')[1] != 'null'):
                # f.write(content + '\n')
                print(content)
  


        


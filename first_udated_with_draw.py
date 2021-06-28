from drawUpdated import *
#no_seg=[]
#p=[]
#memory=[]
#process=[]
def holes_map(start_add,size,total_size):
    #startadd=[]
    #size=[]
    #total_size=t
    print ('start add',start_add)
    print ('size',size)
    print ('mem size',total_size)

    count_oldp=0
    memory=[]
    flag =0
    i=0
    j=0
    while i<len(start_add):
    #for i in range(0,len(start_add)):
        #make holes map (name,address,size)

        if j<len(start_add):
            if (j)!=len(start_add)-1 and start_add[j]+size[j]==start_add[j+1] :
                memory.append((i, start_add[j], size[j]+size[j+1], 'h'))
                #i+=1
                flag=1
            elif flag==0:
                memory.append((i,start_add[j],size[j],'h'))


        if i==0 and start_add[i] !=0:
            memory.append((count_oldp,0,start_add[i],'o'))
            count_oldp += 1
        if i==len(start_add)-1:
            memory.append((count_oldp,start_add[i] + size[i],total_size-(start_add[i] + size[i]),'o'))
            count_oldp += 1
        elif (start_add[i] + size[i])<start_add[i+1]:
            memory.append((count_oldp,start_add[i] + size[i],start_add[i+1]-(start_add[i] + size[i]),'o'))
            count_oldp += 1
        if flag==1:
            j+=1
            flag=0
        i+=1
        j+=1
    memory = sorted(memory, key=lambda k: [k[1], k[0], k[2],k[3]])
    print("mem",memory)
    return memory #ADDED



def process_map(p,no_seg,name,size): #inputs       #function to take the input process attributes:noofsegment,size,name bs shayleen al attributes delwa2ty
    #process_no=0  #name---> p []  no ---> num of seg []  name --> name of seg[] size --> size of seg[]
    #p=[6,7] #num of procces
    #no_seg=[2,1]
    #name=['code','stack','data']
    #size=[5,5,10]
    print('p',p)
    print ('no_seg',no_seg)
    print('arr of names',name)
    print('size',size)
    process=[] #list for the input processes
    count=0 #variable to make the loop iterate on all segments badal j
      #(process_no,name,size)
    for i in range(0,len(no_seg)):
        for j in range(0,no_seg[i]): # i no of process and j no of segment
            process.append((i,j,name[i][j],size[i][j],p[i]))
            #process.append((i,j,name[count],size[count],p[i])) #f'P{i}' is a concatination method between leter p and integer i
            #count +=1
    return process



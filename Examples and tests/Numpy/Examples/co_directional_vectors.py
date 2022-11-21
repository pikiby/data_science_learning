import numpy as np
a = np.array([23, 34, 27])
b = np.array([-54, 1,  46])
c = np.array([46, 68, 54])

# Пишите здесь команды, который помогут
# найти ответы на вопросы
def co_directional_vectors(*args):
    lenvec = len(args)
    for i in range(0,lenvec):
        if i == lenvec:
                break
        for j in range(i+1,lenvec):
            veclen = np.linalg.norm(args[i]+args[j])
            vecsumlen = np.linalg.norm(args[i]) + np.linalg.norm(args[j])
            if veclen == vecsumlen:
                print ('{} and {} is equel'.format(args[i], args[j]))
        
co_directional_vectors (a,b,c)


def distance_between_vectors (*args):
    lenvec = len(args)
    for i in range(0,lenvec):
        if i == lenvec:
                break
        for j in range(i+1,lenvec):
            vec_distence = np.linalg.norm(args[i] - args[j])
            if vec_distence >= 100:
                print ('The distance between {} and {} is equel or more then 100'.format (args[i], args[j]))
            
            
distance_between_vectors (a,b,c)

def perpendicular_vectors (*args):
    lenvec = len(args)
    for i in range(0,lenvec):
        if i == lenvec:
                break
        for j in range(i+1,lenvec):
            vec_perpendicular = np.dot(args[i],args[j])
            if vec_perpendicular == 0:
                print ('{} and {} is perpendicular'.format (args[i], args[j]))
                
perpendicular_vectors (a,b,c)
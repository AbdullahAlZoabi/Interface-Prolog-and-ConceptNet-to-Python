from ConceptNetInterface import GetAllEdges

from pyswip import Prolog

import string


prolog = Prolog()


def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


Edges = GetAllEdges("word",1,100,False)


for edge in Edges:

    Start = edge.Get_StartNode().lower()
    End = edge.Get_EndNode().lower()
    Relation = edge.Get_Relation().lower()

    Con1 = Start.isalpha()
    Con2 = End.isalpha()

    if  (Con1 and Con2):

        Con3 = isEnglish(Start)
        Con4 = isEnglish(End)

        if (Con3 and Con4):
            Fact = Relation+"("+Start+","+End+")"
            prolog.assertz(Fact)
            

#Some Prolog Queries

#x = list(prolog.query("isa(Y,X)"))

#x = list(prolog.query("isa(Y,X),relatedto(X,Z)"))

#x = list(prolog.query("isa(X,'word')"))

x = list(prolog.query("synonym(X,Y)"))


for i in x:
    print i

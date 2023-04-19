
class person_movie:
    def __init__(self):
        self.person_name=""
        self.person_id=0
        self.person_movie_id={}
        self.person_movie_list=[]
    def getPersonId(self):
        return self.person_id
    def setPersonId(self,id):
        self.person_id=id
    def setPersonName(self,name):
        self.person_name=name
    def getPersonName(self):
        return self.person_name
    def setPersonMovieID(self,movie_id,movie_list):
        if(movie_id not in self.person_movie_id.keys() ):
            self.person_movie_id[movie_id]=movie_list
    def getPersonMovieID_List(self,movie_id):
        if(movie_id not in self.person_movie_id.keys() ):
            return self.person_movie_id[movie_id]
    def getPersonMovieList(self,movie_id):
        movie_id_list=list(self.person_movie_id.keys())
        if(movie_id in movie_id_list):
            return self.person_movie_id[movie_id]
    def setPersonMovieList(self,movie_name,genre):
        self.person_movie_list.append(movie_name)
        self.person_movie_list.append(genre)
    def getPerson_info(self,movie_ID):
        print("ID ",self.getPersonId())
        print("Name ",self.getPersonName())
        print("MovieList",self.getPersonMovieList(movie_ID))
        
    #def Menu_Info
        
    
p = person_movie()
p.setPersonName("Amit")
p.setPersonId(1)
p.setPersonMovieID(101,['Jurassic Park','Thriller'])
#p.setPersonMovieList('Jurassic Park','Thriller')
movie_id=p.getPersonMovieID_List(101)
p.getPerson_info(movie_id)


        
